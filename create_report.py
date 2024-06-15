from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf(filename):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, height - 100, "My Report Title")

    # Subtitle
    c.setFont("Helvetica", 12)
    c.drawString(100, height - 150, "Subtitle or description here.")

    # Line
    c.setStrokeColorRGB(0, 0, 0)
    c.setLineWidth(1)
    c.line(100, height - 170, width - 100, height - 170)

    # Body text
    c.setFont("Helvetica", 10)
    text = (
        "This is a sample paragraph demonstrating the use of ReportLab to generate "
        "PDFs in Python. You can add more text, images, tables, and other elements "
        "as needed."
    )
    text_object = c.beginText(100, height - 200)
    text_object.textLines(text)
    c.drawText(text_object)

    c.showPage()
    c.save()

if __name__ == "__main__":
    create_pdf("example_report.pdf")
