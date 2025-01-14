import json
import re
import os

def nav_order_dict_gen(ticker_sec_path):
    with open(ticker_sec_path, 'r') as f:
        data = json.load(f)
    
    output = {}
    
    i = 1
    for key, value in data.items():
        output[value["ticker"]] = i
        i += 1

    return output

def parse_md_file(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Start parsing from the first line with ##
    start_line = next((i for i, line in enumerate(lines) if line.startswith("##")), None)
    if start_line is None:
        raise ValueError("Input file format is incorrect: No line starting with ##.")

    first_line = lines[start_line].strip()
    regex = re.compile(
    r"## (.+?) \((\w+(?:-\w+)?)\)\s*\|\s*Moat:\s*(\d(?:\.\d)?)\s*/\s*5\s*\|\s*Understandability:\s*(\d(?:\.\d)?)\s*/\s*5\s*\|\s*Balance Sheet Health:\s*(\d(?:\.\d)?)\s*/\s*5",
    re.IGNORECASE
)

    match = regex.match(first_line)
    if not match:
        print(first_line)
        raise ValueError("Input file format is incorrect.")

    title, ticker, moat, understandability, balance_sheet_health = match.groups()
    next_line = start_line + 1
    if len(lines[next_line].strip()) == 0:
        next_line += 1

    description = lines[next_line].strip()
    print(description)

    return title, ticker, int(moat), int(understandability), int(balance_sheet_health), description, next_line + 1

def generate_markdown(title, ticker, moat, understandability, balance_sheet_health, description, nav_order_dict):
    markdown = f"""---
title: {title} ({ticker})
layout: default
nav_order: {nav_order_dict[ticker]}
---

# {title}
{{: .fs-9 }}

{{: .label .label-purple }}

Moat: {moat}/5

{{: .label .label-blue }}

Understandability: {understandability}/5

{{: .label .label-green }}

Balance Sheet Health: {balance_sheet_health}/5

{description}
{{: .fs-6 .fw-300 }}

[Investor Relations](https://www.google.com/search?q={ticker}+investor+relations){{: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }}
[Previous Earnings Calls](https://discountingcashflows.com/company/{ticker}/transcripts/){{: .btn .fs-5 .mb-4 .mb-md-0 }}

---

{{: .warning }}
>The moat, understandability, and balance sheet health scores reflect a conservative evaluation to ensure a margin of safety in any assessment.
"""
    return markdown

docs = [os.path.join("docs", d) for d in os.listdir("docs") if d.endswith(".md")]

for input_file in docs:
    print(f"Processing: {input_file}")

    try:
        title, ticker, moat, understandability, balance_sheet_health, description, ltr = parse_md_file(input_file)
    except Exception as e:
        print(e)
        continue

    try:
        nav_order_dict = nav_order_dict_gen("tickers.json")
    except Exception as e:
        print(e)
        continue

    markdown_output = generate_markdown(title, ticker, moat, understandability, balance_sheet_health, description, nav_order_dict)

    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Replace the first few lines with the new markdown content
    with open(input_file, 'w') as file:
        file.write(markdown_output)
        file.write("\n\n")

        callouts = ['{: .highlight }', '{: .note }', '{: .new }', '{: .important }', '{: .warning }']
        wrong_callouts = ['{: .highlight}', '{: .note}', '{: .new}', '{: .important}', '{: .warning}']

        # Create a mapping from wrong callouts to correct ones
        callout_mapping = dict(zip(wrong_callouts, callouts))

        for line in lines[ltr:]:
            modified_line = line  # Start with the original line

            # # Check for both correct and wrong callouts
            for callout in callouts + wrong_callouts:
                 if callout in line.strip():
                    correct_callout = callout_mapping.get(callout, callout)  # Normalize to correct callout
                    print(f"{correct_callout} detected.")
                     # Remove the callout from the line and prepend the normalized callout

                    if len(line.strip().split()) > 1:
                        modified_line = f"{correct_callout}\n{line.replace(callout, '').strip()}\n"

                    #modified_line = modified_line.replace(">  ", "")
                    break  # Exit the loop after finding the first matching callout

            file.write(modified_line)  # Write the modified line once, outside the callout loop

