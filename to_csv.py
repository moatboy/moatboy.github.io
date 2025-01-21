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

def get_pe_ratio(ticker):
    stock = yf.Ticker(ticker)
    return round(float(stock.info['trailingPE']), 1) if 'trailingPE' in stock.info else None

def extract_data_from_md(md_content):
    """Extract data from a single markdown file content."""
    moat_match = re.search(r"Moat: (\d+(?:\.\d+)?)", md_content)
    understandability_match = re.search(r"Understandability: (\d+(?:\.\d+)?)", md_content)
    balance_sheet_health_match = re.search(r"Balance Sheet Health: (\d+(?:\.\d+)?)", md_content)

    return {
        "moat": moat_match.group(1) if moat_match else "N/A",
        "understandability": understandability_match.group(1) if understandability_match else "N/A",
        "balance_sheet_health": balance_sheet_health_match.group(1) if balance_sheet_health_match else "N/A",
    }

def load_existing_tickers(output_csv):
    """Load existing tickers from the CSV file."""
    if not os.path.exists(output_csv):
        return set()
    
    with open(output_csv, "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        return {row["ticker"] for row in reader}

def process_md_files(input_directory, output_csv):
    """Process all .md files in the directory and write to CSV."""
    existing_tickers = load_existing_tickers(output_csv)
    rows = []
    for file_name in tqdm(os.listdir(input_directory), total=len(os.listdir(input_directory))):
        if file_name.endswith(".md"):
            ticker = file_name.split(".")[0]
            if ticker in existing_tickers:
                continue  # Skip if the ticker is already processed

            with open(os.path.join(input_directory, file_name), "r", encoding="utf-8") as file:
                md_content = file.read()
                data = extract_data_from_md(md_content)
                data["ticker"] = ticker
                data["marketcap"] = get_market_cap(data["ticker"])
                data["pe_ratio"] = get_pe_ratio(data["ticker"])

                if data["moat"] != "N/A" and data["understandability"] != "N/A" and data["balance_sheet_health"] != "N/A":
                    rows.append(data)

    # Append new data to the CSV
    with open(output_csv, "a", newline='', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["ticker", "moat", "understandability", "balance_sheet_health", "marketcap", "pe_ratio"])
        if not existing_tickers:  # Write header if CSV is new
            writer.writeheader()
        writer.writerows(rows)

# Set input directory and output CSV file
input_directory = "docs/"
output_csv = "moatboy.csv"

# Process markdown files
process_md_files(input_directory, output_csv)
