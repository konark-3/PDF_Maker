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

`pip install fpdf pandas`

## ⚙️ Setup

1. Add a `topics.csv` file with columns:
Topic,Pages
Python,3
Machine Learning,5
Data Science,2

2. Install dependencies:
`pip install fpdf pandas`

1.  Ensure the script and CSV file are in the same directory.

* * * * *

## 🚀 How It Works
---------------

1.  Reads the topic list and page counts from `topics.csv`.

2.  For each topic:

    -   Creates a title page with the topic name and a header line.

    -   Adds multiple ruled pages (based on the "Pages" column).

    -   Adds a motivational footer "Keep Going!" on every page.

3.  Outputs the final compiled notebook as `output.pdf`.

* * * * *

## 💡 Example Usage
----------------

Run the script:
`python notebook_generator.py`

Output:
`output.pdf`


Each topic section includes:

-   Title page

-   Number of ruled pages as specified in the CSV

-   Footer with "Keep Going!" motivation

* * * * *

## 📝 Notes
--------

-   You can adjust the spacing or add background lines by editing the line drawing loop.

-   The script uses fixed margins and font settings optimized for A4 paper.

-   Customize the footer text or style easily in the final section of the code.


