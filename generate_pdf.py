import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def build_pdf(data, output_filename="jo_pmd_kpi_report.pdf"):
    s = data["scores"]
    
    # 註冊中文字體（採用系統預設或動態下載字型，避免亂碼）
    # ReportLab 預設 Helvetica 不支援中文，此處建立極簡 PDF 結構
    doc = SimpleDocTemplate(
        output_filename,
        pagesize=A4,
        rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=30
    )
    
    styles = getSampleStyleSheet()
    normal = styles['Normal']
    
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=normal,
        fontSize=16,
        leading=20,
        alignment=1, # Center
        textColor=colors.HexColor('#1E3A8A')
    )
    
    subtitle_style = ParagraphStyle(
        'SubTitleStyle',
        parent=normal,
        fontSize=11,
        leading=15,
        alignment=1, # Center
        textColor=colors.HexColor('#0284C7')
    )
    
    story = []
    
    # 標題
    story.append(Paragraph("<b>Jumbo Orient Contracting Limited (東淦工程)</b>", title_style))
    story.append(Paragraph("<b>PMD Site Staff KPI Assessment Agreement (jo-pmd-site-kpi)</b>", subtitle_style))
    story.append(Spacer(1, 10))
    
    # 基本資料表
    info_data = [
        [Paragraph(f"<b>Employee Name:</b> {data['emp_name']}"), Paragraph(f"<b>Site:</b> {data['project_site']}")],
        [Paragraph(f"<b>Supervisor:</b> {data['supervisor']}"), Paragraph(f"<b>PMD Rep:</b> {data['pmd_rep']}")],
        [Paragraph(f"<b>Period:</b> {data['eval_month']}"), Paragraph(f"<b>Date:</b> {data['sign_date']}")]
    ]
    t_info = Table(info_data, colWidths=[260, 260])
    t_info.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_info)
    story.append(Spacer(1, 15))
    
    # KPI 得分彙總表
    summary_data = [
        [Paragraph("<b>Dimension / Item</b>"), Paragraph("<b>Score</b>"), Paragraph("<b>Max</b>")],
        [Paragraph("1.1 Emergency Call Response"), Paragraph(str(s['s1_1'])), Paragraph("8")],
        [Paragraph("1.2 Daily Report Integrity"), Paragraph(str(s['s1_2'])), Paragraph("8")],
        [Paragraph("1.3 Site Transfer Log"), Paragraph(str(s['s1_3'])), Paragraph("4")],
        [Paragraph("2.1 Milestone Completion Rate"), Paragraph(str(s['s2_1'])), Paragraph("15")],
        [Paragraph("2.2 First Inspection Pass Rate"), Paragraph(str(s['s2_2'])), Paragraph("12")],
        [Paragraph("2.3 Drawing / RFI / Briefing"), Paragraph(str(s['s2_3'])), Paragraph("8")],
        [Paragraph("3.1 Material Requisition Accuracy"), Paragraph(str(s['s3_1'])), Paragraph("8")],
        [Paragraph("3.2 Material Wastage Rate"), Paragraph(str(s['s3_2'])), Paragraph("7")],
        [Paragraph("4.1 Safety Inspection Rectification"), Paragraph(str(s['s4_1'])), Paragraph("12")],
        [Paragraph("4.2 Risk Assessment & Reporting"), Paragraph(str(s['s4_2'])), Paragraph("10")],
        [Paragraph("4.3 Attendance Verification"), Paragraph(str(s['s4_3'])), Paragraph("8")],
        [Paragraph("<b>FINAL TOTAL SCORE</b>"), Paragraph(f"<b>{data['total_score']:.1f}</b>"), Paragraph("<b>100</b>")],
        [Paragraph("<b>FINAL GRADE</b>"), Paragraph(f"<b>{data['final_grade']}</b>"), Paragraph("-")]
    ]
    t_summary = Table(summary_data, colWidths=[320, 100, 100])
    t_summary.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E3A8A')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('ALIGN', (1,0), (-1,-1), 'CENTER'),
        ('BACKGROUND', (0,-2), (-1,-1), colors.HexColor('#EFF6FF')),
    ]))
    story.append(t_summary)
    story.append(Spacer(1, 15))
    
    # 簽署欄
    sign_data = [
        [Paragraph("<b>Employee Signature:</b><br/><br/>Date:"), Paragraph("<b>Supervisor Signature:</b><br/><br/>Date:")],
        [Paragraph("<b>PMD Rep Signature:</b><br/><br/>Date:"), Paragraph("<b>HR / Reviewer Signature:</b><br/><br/>Date:")]
    ]
    t_sign = Table(sign_data, colWidths=[260, 260])
    t_sign.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 20),
    ]))
    story.append(t_sign)
    
    doc.build(story)
    return output_filename
