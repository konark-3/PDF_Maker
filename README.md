# CSV to Lined PDF Generator

This Python script generates a **lined notebook-style PDF** from a CSV file containing topics and page counts. Each topic gets its own section with the specified number of lined pages, making it ideal for creating study guides, planners, or custom notebooks.

---

## Features

- Reads topics and page counts from a CSV file.
- Creates a PDF where:
  - Each topic starts on a new page.
  - Pages contain evenly spaced horizontal lines.
  - Footer text ("Keep Going!") is added on each page.
- Automatically handles multiple pages per topic.

---

## Requirements

- Python 3.x
- Packages:
  - `fpdf`
  - `pandas`

Install dependencies using pip:

```bash
pip install fpdf pandas
