from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")  ##pdf instance
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style='B', size=16)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], border=0, ln=1, align="L")
    pdf.line(10, 21, 200, 22)

    pdf.ln(266)
    pdf.set_font(family="Times", style='I', size=8)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=0, txt="Keep Going!", border=0, ln=1, align="R")


    # for i in range(30, 298, 10):
    #     pdf.line(10, i, 200, i)
    n = 30

    for i in range(26):
        pdf.line(10, n, 200, n)
        n += 10

    for i in range(row['Pages']-1):
        pdf.add_page()
        for i in range(20, 290, 10):
            pdf.line(10, i, 200, i)

        pdf.ln(277)
        pdf.set_font(family="Times", style='I', size=8)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=0, txt="Keep Going!", border=0, ln=1, align="R")


pdf.output("output.pdf")




# def pdf_doc(n):
#     for i in range(2):
#         pdf.add_page()
#
#         pdf.set_font(family="Times", style='B', size=16)
#         pdf.cell(w=0, h=16, txt="This is a PDF", border=0, ln=1, align="L")
#
#         pdf.set_font(family="Times", style='B', size=12)
#         pdf.cell(w=0, h=16, txt=f"This is page number {n}", border=1, ln=1, align="L")
#
#         n += 1
#
#         #pdf_doc(1)

