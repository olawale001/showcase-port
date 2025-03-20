from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image

def create_portfolio_pdf(file_path):
    # Create a PDF document
    pdf = SimpleDocTemplate(file_path, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    # Portfolio Title
    title = Paragraph("My Portfolio", styles['Title'])
    elements.append(title)
    elements.append(Spacer(1, 12))

    # Introduction
    introduction = Paragraph("""
    <b>Name: Abdullateef Yusuf</b><br/>
    Role: Python Developer, Data Scientist, Web Developer<br/>
    Welcome to my portfolio! I am a passionate developer with expertise in Python, Django, and data science. Below you'll find details about my skills, projects, and how to contact me.
    """, styles['Normal'])
    elements.append(introduction)
    elements.append(Spacer(1, 12))

    # Skills Section
    skills_title = Paragraph("<b>Skills</b>", styles['Heading2'])
    elements.append(skills_title)
    skills = [
        ["Programming Languages", "Python, JavaScript, HTML, CSS"],
        ["Frameworks & Libraries", "Django, React", "Tensorflow"],
        ["Databases", "PostgreSQL, MySQL, SQLite"],
        ["Tools & Platforms", "Git, Docker, AWS"]
    ]
    table = Table(skills, hAlign='LEFT')
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(table)
    elements.append(Spacer(1, 12))

    # Projects Section
    projects_title = Paragraph("<b>Projects</b>", styles['Heading2'])
    elements.append(projects_title)
    project_1 = """
    <b>Project 1: E-commerce Platform</b><br/>
    Developed e-commerce platform using Django and RestFul API. Implemented features like product management, user authentication, and payment processing.
    """
    elements.append(Paragraph(project_1, styles['Normal']))
    elements.append(Spacer(1, 12))

    project_2 = """
    <b>Project 2: Data Visualization Dashboard</b><br/>
    Built a data visualization dashboard using Django and Plotly, allowing users to explore and visualize complex datasets interactively.
    """
    elements.append(Paragraph(project_2, styles['Normal']))
    elements.append(Spacer(1, 12))

    # Add more projects as needed
    # ...

    # Contact Information
    contact_title = Paragraph("<b>Contact Information</b>", styles['Heading2'])
    elements.append(contact_title)
    contact_info = """
    <b>Email:</b> olacodeire@gmail.com<br/>
    <b>GitHub:</b> <a href="[https://github.com/olawale001]">https://github.com/olawale001</a><br/>
    """
    elements.append(Paragraph(contact_info, styles['Normal']))
    elements.append(Spacer(1, 12))

    # Optional: Add an image or logo
    # logo = Image("path/to/your/logo.png", 2*inch, 2*inch)
    # elements.append(logo)

    # Build the PDF
    pdf.build(elements)

if __name__ == "__main__":
    create_portfolio_pdf("my_portfolio.pdf")
