import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path


filepaths = glob.glob("Invoices/*.xlsx")

for filepath in filepaths:

    pdf = FPDF(orientation='P', unit="mm", format="A4")
    pdf.add_page()

    filename = Path(filepath).stem
    Invoice_no = filename.split('-')[0]
    date = filename.split('-')[1]

    pdf.set_font(family="Times", style="B", size=16)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=10, txt=f"Invoice Number: {Invoice_no}", border=0, ln=1, align="L")

    pdf.set_font(family="Times", style="B", size=16)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=10, txt=f"Date: {date}", border=0, ln=1, align="L")

    df = pd.read_excel(filepath)

    print(list(df.columns))

    columns = df.columns
    lst = [i.replace("_", " ") for i in columns]
    lst = [i.title() for i in lst]

    pdf.set_font(family="Times", style="B", size=11)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=30, h=10, txt=lst[0], border=1, ln=0, align="C")

    pdf.set_font(family="Times", style="B", size=11)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=60, h=10, txt=lst[1], border=1, ln=0, align="C")

    pdf.set_font(family="Times", style="B", size=11)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=35, h=10, txt=lst[2], border=1, ln=0, align="C")

    pdf.set_font(family="Times", style="B", size=11)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=30, h=10, txt=lst[3], border=1, ln=0, align="C")

    pdf.set_font(family="Times", style="B", size=11)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=30, h=10, txt=lst[4], border=1, ln=1, align="C")

    for index, row in df.iterrows():

        pdf.set_font(family="Times", style="B", size=11)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=30, h=10, txt=str(row['product_id']), border=1, ln=0, align="C")

        pdf.set_font(family="Times", style="B", size=11)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=60, h=10, txt=str(row['product_name']), border=1, ln=0, align="C")

        pdf.set_font(family="Times", style="B", size=11)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=35, h=10, txt=str(row['amount_purchased']), border=1, ln=0, align="C")

        pdf.set_font(family="Times", style="B", size=11)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=30, h=10, txt=str(row['price_per_unit']), border=1, ln=0, align="C")

        pdf.set_font(family="Times", style="B", size=11)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=30, h=10, txt=str(row['total_price']), border=1, ln=1, align="C")

    pdf.cell(w=30, h=10, txt="", border=1, ln=0, align="C")

    pdf.cell(w=60, h=10, txt="", border=1, ln=0, align="C")

    pdf.cell(w=35, h=10, txt="", border=1, ln=0, align="C")

    pdf.cell(w=30, h=10, txt="", border=1, ln=0, align="C")

    pdf.set_font(family="Times", style="B", size=11)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=30, h=10, txt=str(df['total_price'].sum()), border=1, ln=1, align="C")

    pdf.set_font(family="Times", style="B", size=16)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=10, txt=f"Total Amount due: ${df['total_price'].sum()}", border=0, ln=1, align="L")

    pdf.set_font(family="Times", style="I", size=16)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=7, txt="PythonHow", align="L")

    pdf.image("pythonhow.png", w=8, x=40)

    pdf.output(f"Invoices_Docs/{filename}.pdf")
