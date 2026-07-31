import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

def build_pdf(data, output_filename="jo_kpi_iso_report.pdf"):
    s = data["scores"]
    
    doc = SimpleDocTemplate(
        output_filename,
        pagesize=A4,
        rightMargin=25, leftMargin=25, topMargin=25, bottomMargin=25
    )
    
    styles = getSampleStyleSheet()
    normal = styles['Normal']
    
    title_style = ParagraphStyle(
        'TitleStyle', parent=normal, fontSize=14, leading=17, alignment=1, textColor=colors.HexColor('#1E3A8A')
    )
    subtitle_style = ParagraphStyle(
        'SubTitleStyle', parent=normal, fontSize=10, leading=13, alignment=1, textColor=colors.HexColor('#0284C7')
    )
    iso_style = ParagraphStyle(
        'IsoStyle', parent=normal, fontSize=7, leading=9, alignment=1, textColor=colors.HexColor('#64748B')
    )
    
    story = []
    
    # 標題與 ISO 管制宣告
    story.append(Paragraph("<b>Jumbo Orient Contracting Limited (東淦工程)</b>", title_style))
    story.append(Paragraph("<b>Senior Foreman KPI Assessment Agreement</b>", subtitle_style))
    story.append(Paragraph("Doc Control Ref: JO-QMS-KPI-SF01 v2.0 | ISO 9001:2015 & ISO 42001 Compliant", iso_style))
    story.append(Spacer(1, 8))
    
    # 基本資料表 (包含 Employee ID)
    info_data = [
        [Paragraph(f"<b>Employee Name:</b> {data['emp_name']}"), Paragraph(f"<b>Employee ID:</b> {data['emp_id']}")],
        [Paragraph(f"<b>Project Site:</b> {data['project_site']}"), Paragraph(f"<b>Direct Supervisor:</b> {data['supervisor']}")],
        [Paragraph(f"<b>Assessment Period:</b> {data['eval_month']}"), Paragraph(f"<b>Sign Date:</b> {data['sign_date']}")],
        [Paragraph(f"<b>ISO Evidence Ref:</b> {data['evidence_ref']}"), Paragraph(f"<b>Bonus Base:</b> {data['bonus_base']}")]
    ]
    t_info = Table(info_data, colWidths=[270, 270])
    t_info.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('TOPPADDING', (0,0), (-1,-1), 4), ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_info)
    story.append(Spacer(1, 10))
    
    # KPI 明細表
    summary_data = [
        [Paragraph("<b>KPI Item</b>"), Paragraph("<b>Actual Data / Rate</b>"), Paragraph("<b>Score / Max</b>")],
        [Paragraph("1.1 Emergency Call Response"), Paragraph(f"Valid:{s['c1_1_valid']} | On-time:{s['c1_1_ontime']} ({s['c1_1_rate']:.1f}%)"), Paragraph(f"{s['s1_1']} / 8")],
        [Paragraph("1.2 Work Report Completion Rate"), Paragraph(f"Total:{s['c1_2_tot']} | OK:{s['c1_2_ok']} ({s['c1_2_rate']:.1f}%)"), Paragraph(f"{s['s1_2']} / 8")],
        [Paragraph("1.3 Site Transfer Log"), Paragraph(f"Total:{s['c1_3_tot']} | Missed:{s['c1_3_miss']}"), Paragraph(f"{s['s1_3']} / 4")],
        [Paragraph("2.1 Milestone Completion Rate"), Paragraph(f"Due:{s['c2_1_tot']} | Done:{s['c2_1_ok']} ({s['c2_1_rate']:.1f}%)"), Paragraph(f"{s['s2_1']} / 15")],
        [Paragraph("2.2 First Inspection Pass Rate"), Paragraph(f"Batches:{s['c2_2_tot']} | Passed:{s['c2_2_ok']} ({s['c2_2_rate']:.1f}%)"), Paragraph(f"{s['s2_2']} / 12")],
        [Paragraph("2.3 Drawing / RFI / Briefing"), Paragraph(f"Minor:{s['c2_3_min']} | Med:{s['c2_3_med']} | Major:{s['c2_3_maj']}"), Paragraph(f"{s['s2_3']} / 8")],
        [Paragraph("3.1 Material Requisition Accuracy"), Paragraph(f"Items:{s['c3_1_tot']} | Accurate:{s['c3_1_ok']} ({s['c3_1_rate']:.1f}%)"), Paragraph(f"{s['s3_1']} / 8")],
        [Paragraph("3.2 Material Wastage Rate"), Paragraph(f"Cost:${s['c3_2_cost']:,.0f} | Loss:${s['c3_2_loss']:,.0f} ({s['c3_2_rate']:.2f}%)"), Paragraph(f"{s['s3_2']} / 7")],
        [Paragraph("4.1 Safety Inspection Rectification"), Paragraph(f"Due:{s['c4_1_tot']} | Done:{s['c4_1_done']} ({s['c4_1_rate']:.1f}%)"), Paragraph(f"{s['s4_1']} / 12")],
        [Paragraph("4.2 Risk Assessment & Reporting"), Paragraph(f"Due:{s['c4_2_tot']} | OK:{s['c4_2_ok']} ({s['c4_2_rate']:.1f}%)"), Paragraph(f"{s['s4_2']} / 10")],
        [Paragraph("4.3 Attendance Verification"), Paragraph(f"Verified:{s['c4_3_days']} days | Diff:{s['c4_3_diff']}"), Paragraph(f"{s['s4_3']} / 8")],
        [Paragraph("<b>FINAL TOTAL SCORE</b>"), Paragraph(f"<b>{data['total_score']:.1f} / 100</b>"), Paragraph(f"<b>{data['total_score']:.1f}</b>")],
        [Paragraph("<b>FINAL GRADE</b>"), Paragraph(f"<b>{data['final_grade']}</b> ({data['grade_desc']})"), Paragraph("-")]
    ]
    t_summary = Table(summary_data, colWidths=[200, 240, 100])
    t_summary.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E3A8A')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('ALIGN', (2,0), (2,-1), 'CENTER'),
        ('BACKGROUND', (0,-2), (-1,-1), colors.HexColor('#EFF6FF')),
        ('TOPPADDING', (0,0), (-1,-1), 3), ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_summary)
    story.append(Spacer(1, 8))
    
    # 備註與 ISO 糾正預告
    comments_text = data['emp_comments'] if data['emp_comments'] else "None"
    comments_data = [
        [Paragraph(f"<b>Employee Agreement:</b> {data['emp_agree']}")],
        [Paragraph(f"<b>Employee Comments:</b> {comments_text}")]
    ]
    t_comm = Table(comments_data, colWidths=[540])
    t_comm.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('TOPPADDING', (0,0), (-1,-1), 4), ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_comm)
    story.append(Spacer(1, 10))

    # 簽署欄
    sign_data = [
        [Paragraph("<b>Employee Signature:</b><br/><br/>Date:"), Paragraph("<b>Direct Supervisor Signature:</b><br/><br/>Date:")],
        [Paragraph("<b>QMS / HR Auditor Signature:</b><br/><br/>Date:"), Paragraph("<b>Company Representative Signature:</b><br/><br/>Date:")]
    ]
    t_sign = Table(sign_data, colWidths=[270, 270])
    t_sign.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('TOPPADDING', (0,0), (-1,-1), 6), ('BOTTOMPADDING', (0,0), (-1,-1), 12),
    ]))
    story.append(t_sign)
    
    doc.build(story)
    return output_filename
