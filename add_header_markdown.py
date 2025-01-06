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

    # Extract first line with title, ticker, moat, and valuation
    first_line = lines[0].strip()
    regex = re.compile(
        r"## (.+?) \((\w+(?:-\w+)?)\)\s*\|\s*Moat:\s*(\d)\s*/\s*5\s*\|\s*Valuation:\s*(N/A|Fair Value = Market Price|[^\d\s]*[\d,.]+(?: \([^\)]+\))?)\s*(Billion|Million|Trillion|per share|/share)?",
        re.IGNORECASE
    )

    match = regex.match(first_line)

    if not match:
        print(first_line)
        raise ValueError("Input file format is incorrect.")
    else:
        print(match.groups())

    if len(match.groups()) == 5:
        title, ticker, moat, valuation, scale = match.groups()
        formatted_valuation = f"{valuation} {scale}" if scale is not None else f"{valuation}"
    elif len(match.groups()) == 4:
        title, ticker, moat, valuation = match.groups()
        formatted_valuation = f"{valuation}"
    else:
        return

    # Format valuation with scale

    # Extract description from the second line
    description = lines[2].strip()
    ltr = 3 if lines[3] is not "\n" else 4

    if len(description.split()) < 5:
        description = lines[4].strip()
        ltr = 5 if lines[5] is not "\n" else 6

    return title, ticker, int(moat), formatted_valuation, description, ltr

def generate_markdown(title, ticker, moat, valuation, description, nav_order_dict):
    markdown = f"""---
title: {title} ({ticker})
layout: default
nav_order: {nav_order_dict[ticker]}
---

# {title}
{{: .fs-9 }}

{{: .label .label-purple }}

Moat: {moat}/5

{{: .label .label-yellow }}

Pessimistic value: {valuation.replace("Trillion", "T").replace("Billion", "B"). replace("Million", "M").replace("million", "M").replace("billion", "B").replace("trillion", "T")}

{description}
{{: .fs-6 .fw-300 }}

[Investor Relations](https://www.google.com/search?q={ticker}+investor+relations){{: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }}
[Previous Earnings Calls](https://discountingcashflows.com/company/{ticker}/transcripts/){{: .btn .fs-5 .mb-4 .mb-md-0 }}

---

{{: .warning }} 
>The moat rating and valuation are meant to reflect a pessimistic outlook, signaling potential competitive pressures and limited growth. This ensures that some margin of safety is already baked in.
"""
    return markdown

docs = [os.path.join("docs", d) for d in os.listdir("docs") if d.endswith(".md")]

for input_file in docs:
    print(f"Processing: {input_file}")

    try:
        title, ticker, moat, valuation, description, ltr = parse_md_file(input_file)
    except Exception as e:
        print(e)
        continue

    try:
        nav_order_dict = nav_order_dict_gen("tickers.json")
    except:
        continue

    ticker = input_file.split('/')[1].split('.')[0]
    markdown_output = generate_markdown(title, ticker, moat, valuation, description, nav_order_dict)

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

            # Check for both correct and wrong callouts
            for callout in callouts + wrong_callouts:
                if callout in line.strip():
                    correct_callout = callout_mapping.get(callout, callout)  # Normalize to correct callout
                    print(f"{correct_callout} detected.")
                    # Remove the callout from the line and prepend the normalized callout
                    modified_line = f"{correct_callout}\n{line.replace(callout, '').strip()}\n"
                    break  # Exit the loop after finding the first matching callout

            file.write(modified_line)  # Write the modified line once, outside the callout loop

