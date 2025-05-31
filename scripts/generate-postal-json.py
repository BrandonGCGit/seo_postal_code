# Run with: python3 scripts/generate-postal-json.py

import requests
import json
import re
from bs4 import BeautifulSoup
import os

def normalize_text(text):
    """Normalize text by removing extra whitespace, footnotes, and special characters."""
    if not text:
        return ""
    
    # Remove footnotes (numbers in parentheses or superscript)
    text = re.sub(r'\(\d+\)', '', text)
    text = re.sub(r'\[\d+\]', '', text)
    text = re.sub(r'\*', '', text)
    
    # Strip whitespace and normalize spaces
    text = text.strip()
    text = ' '.join(text.split())
    
    return text

def debug_table_structure(table, table_index):
    """Debug function to print table structure for analysis."""
    print(f"\n--- DEBUG: Table {table_index + 1} Structure ---")
    rows = table.find_all('tr')
    print(f"Total rows: {len(rows)}")
    
    for i, row in enumerate(rows[:5]):  # Show first 5 rows
        cells = row.find_all(['td', 'th'])
        print(f"Row {i + 1}: {len(cells)} cells")
        if cells:
            cell_texts = [normalize_text(cell.get_text())[:50] for cell in cells[:4]]
            print(f"  Content: {cell_texts}")

def scrape_postal_codes():
    """Scrape postal codes from the Costa Rica postal codes website."""
    url = "https://www.soyfreelancer.com/blog/codigos-postales-costa-rica/"
    
    print(f"Scraping data from: {url}")
    
    try:
        # Send GET request to the website
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        postal_codes_data = []
        
        # Look for tables containing postal code data
        tables = soup.find_all('table')
        
        if not tables:
            print("No tables found on the page. Looking for alternative structures...")
            # Try to find div or other structures that might contain the data
            content_divs = soup.find_all('div', class_=['content', 'post-content', 'entry-content'])
            for div in content_divs:
                tables.extend(div.find_all('table'))
        
        print(f"Found {len(tables)} table(s) on the page")
        
        for table_index, table in enumerate(tables):
            print(f"\nProcessing table {table_index + 1}...")
            
            # Debug table structure
            debug_table_structure(table, table_index)
            
            rows = table.find_all('tr')
            
            # For each table, the first row should contain the province name
            # Second row is the header (Cantón, Distrito, Código Postal)
            # Subsequent rows contain the data
            
            current_province = ""
            
            for row_index, row in enumerate(rows):
                cells = row.find_all(['td', 'th'])
                
                if len(cells) >= 3:
                    cell_texts = [normalize_text(cell.get_text()) for cell in cells]
                    
                    # Check if this is the province header row (first row, usually spans columns)
                    if row_index == 0 and len(cell_texts) >= 1 and cell_texts[0]:
                        # This should be the province name
                        province_candidate = cell_texts[0]
                        # Validate it's a known Costa Rican province
                        known_provinces = ['San José', 'Alajuela', 'Cartago', 'Heredia', 'Guanacaste', 'Puntarenas', 'Limón']
                        if province_candidate in known_provinces:
                            current_province = province_candidate
                            print(f"Found province: {current_province}")
                            continue
                    
                    # Check if this is the header row (Cantón, Distrito, Código Postal)
                    if (row_index == 1 and 
                        any(keyword in ' '.join(cell_texts).lower() for keyword in ['cantón', 'distrito', 'código'])):
                        print("Skipping header row")
                        continue
                    
                    # This should be a data row
                    if current_province and len(cell_texts) >= 3:
                        try:
                            canton = cell_texts[0]
                            district = cell_texts[1]
                            postal_code = cell_texts[2]
                            
                            # Validate postal code format (should be 5 digits)
                            if (re.match(r'^\d{5}$', postal_code) and 
                                canton and district and current_province and
                                len(canton) > 1 and len(district) > 1):
                                
                                entry = {
                                    "province": current_province,
                                    "canton": canton,
                                    "district": district,
                                    "postal_code": postal_code
                                }
                                
                                # Check for duplicates
                                if entry not in postal_codes_data:
                                    postal_codes_data.append(entry)
                                    
                                    if len(postal_codes_data) <= 10:  # Show first few entries
                                        print(f"Added: {current_province} > {canton} > {district} = {postal_code}")
                            
                        except Exception as e:
                            print(f"Error processing data row {row_index + 1} in table {table_index + 1}: {e}")
                            continue
        
        print(f"\nTotal postal codes extracted: {len(postal_codes_data)}")
        
        if postal_codes_data:
            # Sort data by province, canton, district for consistency
            postal_codes_data.sort(key=lambda x: (x['province'], x['canton'], x['district']))
            
            # Ensure the output directory exists
            os.makedirs('src/data', exist_ok=True)
            
            # Save to JSON file (overwrite existing)
            output_file = 'src/data/postal-codes.json'
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(postal_codes_data, f, ensure_ascii=False, indent=2)
            
            print(f"Data successfully saved to: {output_file}")
            print(f"Sample entries:")
            for i, entry in enumerate(postal_codes_data[:3]):
                print(f"  {i+1}. {entry}")
                
            # Also update the public copy
            public_file = 'public/postal-codes.json'
            if os.path.exists('public'):
                with open(public_file, 'w', encoding='utf-8') as f:
                    json.dump(postal_codes_data, f, ensure_ascii=False, indent=2)
                print(f"Also updated: {public_file}")
        else:
            print("No postal code data was extracted.")
            print("This might indicate that the website structure has changed.")
            print("Consider inspecting the page manually to update the scraping logic.")
            
    except requests.RequestException as e:
        print(f"Error fetching the webpage: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """Main function to run the scraping script."""
    print("=== Costa Rica Postal Codes Scraper ===")
    print("This script will extract postal codes from soyfreelancer.com")
    print("and save them to src/data/postal-codes.json\n")
    
    scrape_postal_codes()
    
    print("\n=== Scraping Complete ===")

if __name__ == "__main__":
    main() 