from fpdf import FPDF
import os
from datetime import datetime

def generate_pdf_report(url, results):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=16)
    pdf.cell(200, 10, txt="C4 Site Auditor Report", ln=True, align="C")
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Website: {url}", ln=True, align="L")
    pdf.cell(200, 10, txt=f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True, align="L")
    pdf.ln(5)
    for agent, data in results.items():
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(200, 10, txt=agent, ln=True, align="L")
        pdf.set_font("Arial", '', 12)
        if isinstance(data, dict):
            summary = data.get("summary", "No summary available.")
            pdf.multi_cell(0, 10, txt=f"Summary: {summary}")
            suggestions = data.get("suggestions", [])
            if suggestions:
                pdf.cell(0, 10, txt="Suggestions:", ln=True)
                for s in suggestions:
                    pdf.multi_cell(0, 8, txt=f"- {s}")
            if "error" in data:
                pdf.set_text_color(255, 0, 0)
                pdf.cell(0, 10, txt=f"Error: {data['error']}", ln=True)
                pdf.set_text_color(0, 0, 0)
        else:
            pdf.multi_cell(0, 10, txt=str(data))
        pdf.ln(5)
    reports_dir = os.path.join(os.path.dirname(__file__), '..', 'reports')
    os.makedirs(reports_dir, exist_ok=True)
    filename = f"audit_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    pdf_path = os.path.join(reports_dir, filename)
    pdf.output(pdf_path)
    return pdf_path