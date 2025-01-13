import os
import csv
import re
import yfinance as yf
from tqdm import tqdm

def format_large_number(number):
    if number >= 1_000_000_000_000:
        return f"{number / 1_000_000_000_000:.1f}T"  # Trillions
    elif number >= 1_000_000_000:
        return f"{number / 1_000_000_000:.1f}B"  # Billions
    elif number >= 1_000_000:
        return f"{number / 1_000_000:.1f}M"  # Millions
    elif number >= 1_000:
        return f"{number / 1_000:.1f}K"  # Thousands
    else:
        return str(number)  # No formatting needed

def get_market_cap(ticker):
    stock = yf.Ticker(ticker)
    return format_large_number(stock.info['marketCap']) if 'marketCap' in stock.info else None

def get_share_count(ticker):
    stock = yf.Ticker(ticker)
    return stock.info.get("sharesOutstanding", None)

def get_digits(number_with_letters):
    # Use regex to find all digits in the input string
    digits = re.findall(r'\d+', number_with_letters)
    # Join the digits and convert to an integer
    return int(''.join(digits))

def normalize_pessimistic_value(value):
    """Normalize the Pessimistic value to a consistent format (e.g., 123B, 45M, 67K)."""
    value = value.strip()
    # Replace long forms with short forms (case insensitive)
    value = re.sub(r"\b(trillion|T)\b", "T", value, flags=re.IGNORECASE)
    value = re.sub(r"\b(billion|B)\b", "B", value, flags=re.IGNORECASE)
    value = re.sub(r"\b(million|M)\b", "M", value, flags=re.IGNORECASE)
    value = re.sub(r"\b(thousand|K)\b", "K", value, flags=re.IGNORECASE)
    # Remove spaces between number and suffix
    value = re.sub(r"(\d+)\s*([TBMK])", r"\1\2", value)
    return value.replace('"', '').replace(",", ".").replace("$", '')

def extract_data_from_md(md_content):
    """Extract data from a single markdown file content."""
    moat_match = re.search(r"Moat: (\d+)", md_content)
    management_match = re.search(r"Management: (\d+)", md_content)
    catalyst_match = re.search(r"Catalyst: (\d+)", md_content)
    pessimistic_value_match = re.search(r"Pessimistic value:\s*(.+)", md_content)
    
    pessimistic_value = (
        normalize_pessimistic_value(pessimistic_value_match.group(1))
        if pessimistic_value_match else "N/A"
    )
    
    return {
        "moat": moat_match.group(1) if moat_match else "N/A",
        "management": management_match.group(1) if management_match else "N/A",
        "catalyst": catalyst_match.group(1) if catalyst_match else "N/A",
        "pessimisticvalue": pessimistic_value if pessimistic_value[0].isdigit() else pessimistic_value[1:],
    }

def process_md_files(input_directory, output_csv):
    """Process all .md files in the directory and write to CSV."""
    rows = []
    for file_name in tqdm(os.listdir(input_directory), total = len(os.listdir(input_directory))):
        if file_name.endswith(".md"):
            with open(os.path.join(input_directory, file_name), "r", encoding="utf-8") as file:
                md_content = file.read()
                data = extract_data_from_md(md_content)
                data["ticker"] = file_name.split(".")[0]
                data["marketcap"] = get_market_cap(data["ticker"])
                share_count = get_share_count(data["ticker"])

                if "share" in data["pessimisticvalue"] and share_count is not None:
                    # get all digits
                    data["pessimisticvalue"] = format_large_number(get_digits(data["pessimisticvalue"]) * share_count)

                if data["pessimisticvalue"].endswith(("M", "B", "K", "T")) and data["marketcap"] is not None and data["ticker"] != "MET":
                    rows.append(data)
    
    # Write extracted data to CSV
    with open(output_csv, "w", newline='', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["ticker", "management", "catalyst", "moat", "pessimisticvalue", "marketcap"])
        writer.writeheader()
        writer.writerows(rows)

# Set input directory and output CSV file
input_directory = "docs/"
output_csv = "moatboy.csv"

# Process markdown files
process_md_files(input_directory, output_csv)
