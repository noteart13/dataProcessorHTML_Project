# Real Estate Data Processor

A Python-based project to scrape and process real estate data from HTML files, transform it into structured JSON, and store it in MongoDB.

## Project Structure
realestate-parser/
├── data/ # Contains sample HTML files and processed JSON data
├── scripts/ # Main processing scripts
│ ├── extract_step2.py # Extracts data from HTML to raw JSON
│ ├── map_step3.py # Maps raw data to structured format
│ ├── transform_step4.py # Applies final transformations
│ └── push_to_mongodb.py # Stores data in MongoDB
├── .env # Environment variables
├── requirements.txt # Python dependencies
└── README.md # This file


## Processing Pipeline

1. `step1.html` - Raw HTML input
2. `step2_meta.json` - Extracted metadata (from extract_step2.py)
3. `step3_mapped.json` - Mapped structured data (from map_step3.py)
4. `step4_final.json` - Final transformed data (from transform_step4.py)

## Prerequisites
- Python 3.8+
- MongoDB (local or Atlas)
- Git (optional for version control)

## Installation
1. Clone the repository (if using Git):
   ```bash
   git clone <https://github.com/noteart13/dataProcessorHTML_Project>
   cd realestate-parser
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Set up your MongoDB connection in .env

4. Run the processing pipeline:
    python scripts/extract_step2.py
    python scripts/map_step3.py
    python scripts/transform_step4.py
    python scripts/push_to_mongodb.py
## Requirements
Python 3.8+

MongoDB (local or remote)