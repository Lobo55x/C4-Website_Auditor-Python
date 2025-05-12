# C4 Site Auditor

A web-based tool to audit websites for performance, SEO, security, code quality, and more using multiple AI agents.

## Features
- Performance, SEO, Security, Code, UI/UX, Marketing, and Business audits
- Generates detailed PDF reports
- Modern, responsive UI

## Requirements
- Python 3.8+
- pip

## Installation
1. Clone this repository:
   ```
   git clone https://github.com/yourusername/c4-site-auditor.git
   cd c4-site-auditor
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
   > **Note:** Make sure you have `beautifulsoup4` installed, as it is required for HTML parsing.

## Usage
1. Start the server:
   ```
   python backend/app.py
   ```
2. Open your browser and go to [http://localhost:5000](http://localhost:5000)
3. Enter a website URL and click "Audit Website"

## Output
- View audit results in the browser
- Download a PDF report

## Project Structure
- `backend/` - Flask backend and agents
- `backend/static/` - CSS and static files
- `backend/templates/` - HTML templates
- `reports/` - Generated PDF reports

## License
MIT