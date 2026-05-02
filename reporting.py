#from matplotlib import colors
from reportlab.lib import colors
from matplotlib.table import Table, table
import pandas as pd
# create a function that takes filename, summary data, compliance percentage and chart path and generates a report in markdown format
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import subprocess
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

import os

def generate_report(filename: str, summary_data: str, compliance_data:pd.DataFrame, compliance_percentage: float, chart_path: str, chart_width: float = 180):
   with open(filename, "w", encoding="utf-8") as f:
        f.write("# Compliance Report\n\n")

        f.write(f"{summary_data}\n\n")

        f.write(f"## Compliance Percentage\n\n")
        f.write(f"**{compliance_percentage:.2f}%**\n\n")

        if not compliance_data.empty:
            f.write("## Compliance Data\n\n")
            f.write("| App Name | Department | Compliance Score | Audit Date |\n")
            f.write("|----------|------------|------------------|------------|\n")

            for _, row in compliance_data.iterrows():
                f.write(
                    f"| {row['App_Name']} | {row['Department']} | "
                    f"{row['Compliance_Score']} | {row['Audit_Date']} |\n"
                )
            f.write("\n")
        else:
            f.write("No compliance data available.\n\n")

        if os.path.exists(chart_path):
            f.write("## Compliance Chart\n\n")
            f.write(f"![Compliance Score by Department]({chart_path})\n\n")
        else:
            f.write("Compliance score chart not available.\n\n")
        
        print(f"Report generated and saved to {filename}")
    # Generate report in markdown format
   ''' 
    with open(filename, 'w') as f:
        f.write("# Compliance Report\n\n")
        f.write(f"{summary_data}\n\n")
        f.write(f"## Compliance Percentage: {compliance_percentage:.2f}%\n\n")
        if not compliance_data.empty:
            
            f.write("## Compliance Data:\n\n")
            f.write("| App Name | Department | Compliance Score | Audit Date |\n")
            f.write("|----------|------------|------------------|------------|\n")
            for index, row in compliance_data.iterrows():
                f.write(f" | {row['App_Name']} | {row['Department']} | {row['Compliance_Score']} | {row['Audit_Date']} |\n")
        
        else:
            f.write("No compliance data available.\n\n")

        if os.path.exists(chart_path):
            f.write(f"![Compliance Score by Department]({chart_path})\n\n")
            #f.write(f"![Compliance Score by Department]({chart_path})\n")
        else:
            f.write("Compliance score chart not available.\n")
    '''
    


# Define a function to convert markdown report to PDF using reportlab
'''
def markdown_to_pdf(markdown_file: str, pdf_file: str):
    c = canvas.Canvas(pdf_file, pagesize=letter)
    width, height = letter
    y_position = height - 50  # Start from the top of the page

    with open(markdown_file, 'r') as f:
        for line in f:
            if line.startswith("# "):  # Title
                c.setFont("Helvetica-Bold", 20)
                c.drawString(50, y_position, line[2:].strip())
                y_position -= 30
            elif line.startswith("## "):  # Subheading
                c.setFont("Helvetica-Bold", 16)
                c.drawString(50, y_position, line[3:].strip())
                y_position -= 25
            elif line.startswith("|"):  # Table row
                c.setFont("Helvetica", 12)
                c.drawString(50, y_position, line.strip())
                y_position -= 15
            else:  # Regular text
                c.setFont("Helvetica", 12)
                c.drawString(50, y_position, line.strip())
                y_position -= 15

            if y_position < 50:  # Check for page overflow
                c.showPage()
                y_position = height - 50

    c.save()
    print(f"PDF generated and saved to {pdf_file}")
'''

# This uses pandoc to convert markdown to pdf

def convert_md_to_pdf(input_md_path: str, output_pdf_path: str):
    #metadata_path = os.path.abspath("C:\Users\WU425NK\OneDrive - EY\Desktop\Python_training\Capstone_Project\compliance_report.pdf")

    command = [
        "pandoc",
        input_md_path,
        "-o", output_pdf_path,
        "--pdf-engine=lualatex",
        "--template=eisvogel",
        #f"--metadata-file={metadata_path}",
        "--variable=mainfont:Times New Roman",
        "--variable=fontsize:12pt"
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise RuntimeError(
            f"Pandoc failed:\n{result.stderr}"
        )

    print(f"PDF generated at {output_pdf_path}")
'''
def convert_md_to_pdf(input_md_path:str, output_pdf_path:str):

    command = [
        "pandoc", input_md_path, "-o", output_pdf_path,
        "--pdf-engine=lualatex", "--template=eisvogel", "--metadata-file=../output/metadata.yaml", "--variable=mainfont:DejaVuSerif", "--variable=fontsize:12pt"
    ]
    subprocess.run(command, capture_output=True, text=True)
'''