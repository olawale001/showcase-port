from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

def create_resume_pdf(file_path):
    # Create a PDF document
    pdf = SimpleDocTemplate(file_path, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    # Title
    title = Paragraph("Python Developer Resume", styles['Title'])
    elements.append(title)
    elements.append(Spacer(1, 12))

    # Contact Information
    contact_info = """
    Name: <b>Abdullateef Yusuf</b><br/>
    Hot_Email: abdullateefy265@gmail.com<br/>
    Email: olacodeire@gmail.com<br/>
    GitHub: <a href="[https://github.com/olawale001]">https://github.com/olawale001</a><br/>
    """
    elements.append(Paragraph(contact_info, styles['Normal']))
    elements.append(Spacer(1, 12))

    # Professional Summary
    summary_title = Paragraph("<b>Professional Summary</b>", styles['Heading2'])
    elements.append(summary_title)
    summary = """
    Results-driven Python developer with [2] years of experience in designing, developing, 
    and deploying efficient web and data science applications. Proficient in Django, 
    RESTful APIs, and data visualization techniques. Passionate about solving complex problems 
    and continuously learning new technologies.
    """
    elements.append(Paragraph(summary, styles['Normal']))
    elements.append(Spacer(1, 12))

    # Skills
    skills_title = Paragraph("<b>Skills</b>", styles['Heading2'])
    elements.append(skills_title)
    skills = [
        ["Python Developer", "Django", "Maintainance"],
        ["Data Science & Visualization", "Front-end Technologies", "Test-Driven Development"],
        ["Database Management", "RESTful API Development", "Version Control (Git, GitHub)"],
    ]
    table = Table(skills)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(table)
    elements.append(Spacer(1, 12))

    # Experience
    experience_title = Paragraph("<b>Experience</b>", styles['Heading2'])
    elements.append(experience_title)
    experience = """
    <b>Python Developer | [OIC HUB]</b><br/>
    - Developed and maintained scalable web applications using Django and Flask frameworks.<br/>
    - Implemented RESTful APIs for data exchange between front-end and back-end systems.<br/>
    - Collaborated with cross-functional teams to deliver high-quality software solutions.<br/>
    - Optimized database queries and improved application performance by 20%.<br/>
    """
    elements.append(Paragraph(experience, styles['Normal']))
    elements.append(Spacer(1, 12))


    education_title = Paragraph("<b>Education</b>", styles['Heading2'])
    elements.append(education_title)
    education = """
    <b>Degree</b><br/>
    [Technical College] | [Year of Graduation: 2022]
    """
    elements.append(Paragraph(education, styles['Normal']))
    elements.append(Spacer(1, 12))


    projects_title = Paragraph("<b>Projects</b>", styles['Heading2'])
    elements.append(projects_title)
    project = """
    <b>[Project Title]</b><br/>
    Description: Developed a full-stack e-commerce application using Django, HTML, CSS and Javascript, 
    featuring JWT authentication, product management, and AI and ML.<br/>
    Technologies: Python, Django, PostgreSQL, Tensorflow, SciKit
    """
    elements.append(Paragraph(project, styles['Normal']))
    elements.append(Spacer(1, 12))

    # Build the PDF
    pdf.build(elements)

if __name__ == "__main__":
    create_resume_pdf("python_developer_resume.pdf")
