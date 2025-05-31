# Scripts Directory

This directory contains utility scripts for the Costa Rica Postal Codes project.

## generate-postal-json.py

A web scraping script that extracts postal code data from https://www.soyfreelancer.com/blog/codigos-postales-costa-rica/

### Prerequisites

Make sure you have Python 3 installed and the required dependencies:

```bash
pip3 install requests beautifulsoup4
```

### Usage

Run the script from the project root directory:

```bash
python3 scripts/generate-postal-json.py
```

### What it does

1. **Scrapes data** from the Costa Rica postal codes website
2. **Extracts** province, canton, district, and postal code information
3. **Normalizes** the data by removing whitespace and footnotes
4. **Validates** postal codes (must be 5 digits)
5. **Saves** the data to both:
   - `src/data/postal-codes.json` (for Astro.js server-side usage)
   - `public/postal-codes.json` (for client-side usage)

### Output format

The script generates JSON data in this format:

```json
[
  {
    "province": "San José",
    "canton": "San José", 
    "district": "Carmen",
    "postal_code": "10101"
  }
]
```

### Data structure

The website contains 7 tables, one for each Costa Rican province:
- San José
- Alajuela  
- Cartago
- Heredia
- Guanacaste
- Puntarenas
- Limón

Each table has:
- **Row 1**: Province name
- **Row 2**: Headers (Cantón, Distrito, Código Postal)
- **Rows 3+**: Data (canton, district, postal code)

### Notes

- The script **overwrites** existing files each time it runs
- It extracts approximately **473 postal codes** (as of the last run)
- The data is automatically sorted by province, canton, and district
- Duplicate entries are automatically filtered out
- The script includes error handling and debugging output

### Troubleshooting

If the script fails to extract data:
1. Check if the website structure has changed
2. Verify the URL is still accessible
3. Run with debug output to see table structure
4. Update the scraping logic if needed 