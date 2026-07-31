import os
from weasyprint import HTML

def build_pdf(data, output_filename="jo_pmd_kpi_report.pdf"):
    s = data["scores"]
    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>東淦工程 PMD 地盤 KPI 考核協議書</title>
    <style>
        @page {{ size: A4; margin: 10mm; }}
        body {{ font-family: 'PingFang HK', 'Microsoft JhengHei', sans-serif; font-size: 8pt; color: #1E293B; }}
        .title {{ text-align: center; font-size: 14pt; font-weight: bold; color: #1E3A8A; }}
        .subtitle {{ text-align: center; font-size: 10pt; font-weight: bold; color: #0284C7; margin-bottom: 8px; border-bottom: 2px solid #1E3A8A; padding-bottom: 4px; }}
        table {{ width: 100%; border-collapse: collapse; margin-bottom: 8px; }}
        td, th {{ border: 1px solid #CBD5E1; padding: 4px; font-size: 7.5pt; }}
        th {{ background-color: #F1F5F9; font-weight: bold; text-align: center; }}
        .label {{ font-weight: bold; background-color: #E2E8F0; width: 15%; }}
        .section-title {{ background-color: #1E3A8A; color: white; padding: 3px 6px; font-weight: bold; margin-top: 6px; margin-bottom: 4px; font-size: 8.5pt; }}
        .box {{ background-color: #F0F9FF; border: 1px solid #0284C7; padding: 6px; margin-top: 6px; }}
        .sign-table td {{ height: 35px; vertical-align: top; width: 25%; }}
    </style>
</head>
<body>
    <div class="title">東淦工程有限公司 Jumbo Orient Contracting Limited</div>
    <div class="subtitle">PMD 項目管理部 - 地盤同事 KPI 績效考核協議書 (jo-pmd-site-kpi)</div>

    <table>
        <tr>
            <td class="label">員工姓名：</td><td>{data['emp_name']}</td>
            <td class="label">所屬地盤：</td><td>{data['project_site']}</td>
        </tr>
        <tr>
            <td class="label">直屬上司：</td><td>{data['supervisor']}</td>
            <td class="label">PMD 代表：</td><td>{data['pmd_rep']}</td>
        </tr>
        <tr>
            <td class="label">考核週期：</td><td>{data['eval_month']}</td>
            <td class="label">評核日期：</td><td>{data['sign_date']}</td>
        </tr>
    </table>

    <div class="section-title">一、 KPI 量化評核結果（滿分 100 分）</div>
    <table>
        <thead>
            <tr><th>考核維度</th><th>編號</th><th>指标名稱</th><th>目標與評分標準</th><th>實際數據</th><th>得分</th></tr>
        </thead>
        <tbody>
            <tr><td rowspan="3" style="text-align:center; font-weight:bold;">溝通及匯報<br>(20%)</td><td>1.1</td><td>緊急通訊回覆率</td><td>≥95%=8分; 90-94.9%=6分; <80%=0分</td><td>有效:{s['c1_1_valid']} | 準時:{s['c1_1_ontime']} ({s['c1_1_rate']:.1f}%)</td><td style="text-align:center; font-weight:bold;">{s['s1_1']}/8</td></tr>
            <tr><td>1.2</td><td>開工/收工/異常匯報</td><td>100%=8分; 95-99.9%=6分; <80%=0分</td><td>應報:{s['c1_2_tot']} | 合規:{s['c1_2_ok']} ({s['c1_2_rate']:.1f}%)</td><td style="text-align:center; font-weight:bold;">{s['s1_2']}/8</td></tr>
            <tr><td>1.3</td><td>場地交接登記</td><td>0次漏登=4分; 1次=3分; ≥4次=0分</td><td>應登:{s['c1_3_tot']} | 漏登:{s['c1_3_miss']}</td><td style="text-align:center; font-weight:bold;">{s['s1_3']}/4</td></tr>
            
            <tr><td rowspan="3" style="text-align:center; font-weight:bold;">工程進度及技術<br>(35%)</td><td>2.1</td><td>調整後里程碑完成率</td><td>≥90%=15分; 85-89.9%=12分; <70%=0分</td><td>節點:{s['c2_1_tot']} | 按時:{s['c2_1_ok']} ({s['c2_1_rate']:.1f}%)</td><td style="text-align:center; font-weight:bold;">{s['s2_1']}/15</td></tr>
            <tr><td>2.2</td><td>首次驗收通過率</td><td>≥85%=12分; 80-84.9%=9分; <70%=0分</td><td>檢驗批:{s['c2_2_tot']} | 通過:{s['c2_2_ok']} ({s['c2_2_rate']:.1f}%)</td><td style="text-align:center; font-weight:bold;">{s['s2_2']}/12</td></tr>
            <tr><td>2.3</td><td>圖紙/RFI/技術交底</td><td>0宗=8分; 1輕微=6分; 1重大=0分</td><td>輕微:{s['c2_3_min']} | 中度:{s['c2_3_med']} | 重大:{s['c2_3_maj']}</td><td style="text-align:center; font-weight:bold;">{s['s2_3']}/8</td></tr>

            <tr><td rowspan="2" style="text-align:center; font-weight:bold;">物料及成本<br>(15%)</td><td>3.1</td><td>物料申請核對準確率</td><td>≥98%=8分; 95-97.9%=6分; <90%=0分</td><td>處理:{s['c3_1_tot']} | 準確:{s['c3_1_ok']} ({s['c3_1_rate']:.1f}%)</td><td style="text-align:center; font-weight:bold;">{s['s3_1']}/8</td></tr>
            <tr><td>3.2</td><td>可避免物料損耗率</td><td>≤2%=7分; >2-3%=5分; >5%=0分</td><td>領料:${s['c3_2_cost']:,.0f} | 損耗:${s['c3_2_loss']:,.0f} ({s['c3_2_rate']:.2f}%)</td><td style="text-align:center; font-weight:bold;">{s['s3_2']}/7</td></tr>

            <tr><td rowspan="3" style="text-align:center; font-weight:bold;">安全及團隊<br>(30%)</td><td>4.1</td><td>安全巡查整改完成率</td><td>≥95%=12分; 90-94.9%=9分; <80%=0分</td><td>應完成:{s['c4_1_tot']} | 完成:{s['c4_1_done']} ({s['c4_1_rate']:.1f}%)</td><td style="text-align:center; font-weight:bold;">{s['s4_1']}/12</td></tr>
            <tr><td>4.2</td><td>風險評估及事故呈報</td><td>100%=10分; 95-99.9%=8分; <80%=0分</td><td>應完成:{s['c4_2_tot']} | 合規:{s['c4_2_ok']} ({s['c4_2_rate']:.1f}%)</td><td style="text-align:center; font-weight:bold;">{s['s4_2']}/10</td></tr>
            <tr><td>4.3</td><td>出勤核實及人手調配</td><td>0差異=8分; 1次=6分; ≥4次=0分</td><td>核實日:{s['c4_3_days']} | 差異:{s['c4_3_diff']}次</td><td style="text-align:center; font-weight:bold;">{s['s4_3']}/8</td></tr>
        </tbody>
    </table>

    <div class="box">
        <strong>PMD 綜合總結：</strong><br>
        • 最終總得分：<strong style="color:#1D4ED8;">{data['total_score']:.1f} / 100 分</strong> | 評定等級：<strong style="color:#D97706;">{data['final_grade']}</strong> {"(⚠️ 觸發一票否決)" if data['veto_triggered'] else ""}<br>
        • 獎金與安排建議：{data['grade_desc']}<br>
        • PMD 監察評語：{data['pmd_comments'] if data['pmd_comments'] else "地盤表現良好，符合 PMD 監察標準。"}<br>
        • 工頭與組內反饋：{data['foreman_feedback'] if data['foreman_feedback'] else "工頭無異議。"}
    </div>

    <div class="section-title">二、 多方審核與簽署欄</div>
    <table class="sign-table">
        <tr>
            <td><strong>被考核員工簽署：</strong><br><br>日期：</td>
            <td><strong>直屬上司簽署：</strong><br><br>日期：</td>
            <td><strong>PMD 項目組代表簽署：</strong><br><br>日期：</td>
            <td><strong>HR / 覆核經理簽署：</strong><br><br>日期：</td>
        </tr>
    </table>
</body>
</html>"""
    HTML(string=html).write_pdf(output_filename)
    return output_filename
