import streamlit as st
import json
from datetime import datetime
from generate_pdf import build_pdf

st.set_page_config(
    page_title="東淦工程 - PMD 地盤 KPI 監察系統",
    page_icon="🏗️",
    layout="wide"
)

# 東淦工程 PMD 視覺主題
st.markdown("""
<style>
    .pmd-title { font-size: 26px; font-weight: bold; color: #1E3A8A; margin-bottom: 2px; }
    .pmd-subtitle { font-size: 15px; font-weight: 600; color: #0284C7; margin-bottom: 20px; }
    .pmd-card { background-color: #F0F9FF; border-left: 5px solid #0284C7; padding: 12px; margin-bottom: 15px; border-radius: 4px; }
    .section-header { font-size: 18px; font-weight: bold; color: #1E3A8A; border-bottom: 2px solid #0284C7; padding-bottom: 5px; margin-top: 20px; margin-bottom: 15px; }
    .stButton>button { background-color: #1E3A8A; color: white; font-weight: bold; border-radius: 6px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="pmd-title">東淦工程有限公司 Jumbo Orient Contracting Limited</div>', unsafe_allow_html=True)
st.markdown('<div class="pmd-subtitle">🔍 PMD (項目管理部) 地盤同事 KPI 績效監察與評核系統 (jo-pmd-site-kpi)</div>', unsafe_allow_html=True)

st.markdown("""
<div class="pmd-card">
    <b>📌 PMD 監察指引：</b>評核須基於地盤現場可核實數據（如每日報告、驗收紀錄、物料單及安全巡查）。因天氣、圖紙未批、總承建商改動等不可控因素，應在評分時排除。
</div>
""", unsafe_allow_html=True)

# 模式選擇
eval_role = st.sidebar.selectbox(
    "👤 當前評核角色 (Evaluator Role)",
    ["PMD 項目管理部代表", "直屬主管 (Direct Supervisor)", "組內/相關部門同事 (Project Team)", "工頭意見整合 (Foreman Feedback)"]
)

with st.form("pmd_kpi_form"):
    st.markdown('<div class="section-header">一、 被考核地盤同事與考核人員資料</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        emp_name = st.text_input("被考核員工姓名", placeholder="例如：陳大文 (高級管工)")
        project_site = st.text_input("監察地盤／項目名稱", placeholder="例如：啟德體育園 / 地盤 B區")
    with col2:
        supervisor = st.text_input("直屬上司", placeholder="例如：張偉明 工程經理")
        pmd_rep = st.text_input("PMD 監察代表姓名", placeholder="例如：李志強 (PMD Senior PM)")
    with col3:
        eval_month = st.text_input("考核週期", value=datetime.now().strftime("%Y年%m月份"))
        sign_date = st.date_input("評核／巡查日期", value=datetime.now())

    st.markdown('<div class="section-header">二、 地盤數據量化評分 (PMD 與主管聯合核實)</div>', unsafe_allow_html=True)

    # 1. 溝通及匯報
    st.markdown("#### 1. 溝通及匯報 (20%)")
    c1, c2, c3 = st.columns(3)
    valid_calls = c1.number_input("有效緊急聯絡總數 (次)", min_value=0, value=10, key="v_calls")
    ontime_calls = c2.number_input("準時回覆次數 (30/60分鐘內)", min_value=0, value=10, key="o_calls")
    call_rate = (ontime_calls / valid_calls * 100) if valid_calls > 0 else 100.0
    c3.text_input("1.1 準時回覆率 (%)", value=f"{call_rate:.1f}%", disabled=True)
    score_1_1 = 8.0 if call_rate>=95 else (6.0 if call_rate>=90 else (4.0 if call_rate>=85 else (2.0 if call_rate>=80 else 0.0)))

    c1, c2, c3 = st.columns(3)
    rep_tot = c1.number_input("應提交開工/收工/異常匯報數", min_value=0, value=30, key="r_tot")
    rep_ok = c2.number_input("合規匯報數", min_value=0, value=30, key="r_ok")
    rep_rate = (rep_ok / rep_tot * 100) if rep_tot > 0 else 100.0
    c3.text_input("1.2 匯報完整率 (%)", value=f"{rep_rate:.1f}%", disabled=True)
    score_1_2 = 8.0 if rep_rate>=100 else (6.0 if rep_rate>=95 else (4.0 if rep_rate>=90 else (2.0 if rep_rate>=80 else 0.0)))

    c1, c2 = st.columns(2)
    trip_tot = c1.number_input("跨場地移動應登記數", min_value=0, value=15, key="t_tot")
    trip_miss = c2.number_input("漏登次數", min_value=0, value=0, key="t_miss")
    score_1_3 = 4.0 if trip_miss==0 else (3.0 if trip_miss==1 else (2.0 if trip_miss==2 else (1.0 if trip_miss==3 else 0.0)))

    # 2. 工程進度及技術執行
    st.markdown("---")
    st.markdown("#### 2. 工程進度及技術執行 (35%)")
    c1, c2, c3 = st.columns(3)
    m_tot = c1.number_input("當月到期里程碑節點數", min_value=0, value=5, key="m_tot")
    m_ok = c2.number_input("按時完成節點數 (已排除不可控因素)", min_value=0, value=5, key="m_ok")
    m_rate = (m_ok / m_tot * 100) if m_tot > 0 else 100.0
    c3.text_input("2.1 里程碑完成率 (%)", value=f"{m_rate:.1f}%", disabled=True)
    score_2_1 = 15.0 if m_rate>=90 else (12.0 if m_rate>=85 else (9.0 if m_rate>=80 else (5.0 if m_rate>=70 else 0.0)))

    c1, c2, c3 = st.columns(3)
    insp_tot = c1.number_input("正式提交驗收批次總數", min_value=0, value=10, key="i_tot")
    insp_ok = c2.number_input("首次驗收通過批次數", min_value=0, value=9, key="i_ok")
    insp_rate = (insp_ok / insp_tot * 100) if insp_tot > 0 else 100.0
    c3.text_input("2.2 首次驗收通過率 (%)", value=f"{insp_rate:.1f}%", disabled=True)
    score_2_2 = 12.0 if insp_rate>=85 else (9.0 if insp_rate>=80 else (6.0 if insp_rate>=75 else (3.0 if insp_rate>=70 else 0.0)))

    c1, c2, c3 = st.columns(3)
    err_min = c1.number_input("圖紙/交底輕微可避免事件(宗)", min_value=0, value=0, key="e_min")
    err_med = c2.number_input("中度可避免事件(宗)", min_value=0, value=0, key="e_med")
    err_maj = c3.number_input("重大可避免事件(宗)", min_value=0, value=0, key="e_maj")
    score_2_3 = 0.0 if err_maj>=1 else (4.0 if (err_med==1 or err_min>=2) else (6.0 if err_min==1 else 8.0))

    # 3. 物料及成本控制
    st.markdown("---")
    st.markdown("#### 3. 物料及成本控制 (15%)")
    c1, c2, c3 = st.columns(3)
    mat_tot = c1.number_input("應處理物料項目", min_value=0, value=20, key="mat_tot")
    mat_ok = c2.number_input("準確處理項目", min_value=0, value=20, key="mat_ok")
    mat_rate = (mat_ok / mat_tot * 100) if mat_tot > 0 else 100.0
    c3.text_input("3.1 物料核對準確率 (%)", value=f"{mat_rate:.1f}%", disabled=True)
    score_3_1 = 8.0 if mat_rate>=98 else (6.0 if mat_rate>=95 else (4.0 if mat_rate>=92 else (2.0 if mat_rate>=90 else 0.0)))

    c1, c2, c3 = st.columns(3)
    mat_cost = c1.number_input("當月已領用材料成本 (HK$)", min_value=0.0, value=100000.0, key="mc")
    loss_cost = c2.number_input("可避免損耗金額 (HK$)", min_value=0.0, value=1000.0, key="lc")
    loss_rate = (loss_cost / mat_cost * 100) if mat_cost > 0 else 0.0
    c3.text_input("3.2 可避免物料損耗率 (%)", value=f"{loss_rate:.2f}%", disabled=True)
    score_3_2 = 7.0 if loss_rate<=2.0 else (5.0 if loss_rate<=3.0 else (3.0 if loss_rate<=4.0 else (1.0 if loss_rate<=5.0 else 0.0)))

    # 4. 安全及團隊管理
    st.markdown("---")
    st.markdown("#### 4. 安全及團隊管理 (30%)")
    c1, c2, c3 = st.columns(3)
    safe_tot = c1.number_input("安全巡查及整改應完成數", min_value=0, value=12, key="s_tot")
    safe_done = c2.number_input("按時完成數", min_value=0, value=12, key="s_done")
    safe_rate = (safe_done / safe_tot * 100) if safe_tot > 0 else 100.0
    c3.text_input("4.1 安全巡查整改完成率 (%)", value=f"{safe_rate:.1f}%", disabled=True)
    score_4_1 = 12.0 if safe_rate>=95 else (9.0 if safe_rate>=90 else (6.0 if safe_rate>=85 else (3.0 if safe_rate>=80 else 0.0)))

    c1, c2, c3 = st.columns(3)
    ra_tot = c1.number_input("風險評估/Toolbox/事故呈報應完成數", min_value=0, value=20, key="ra_tot")
    ra_ok = c2.number_input("合規完成數", min_value=0, value=20, key="ra_ok")
    ra_rate = (ra_ok / ra_tot * 100) if ra_tot > 0 else 100.0
    c3.text_input("4.2 風險評估合規率 (%)", value=f"{ra_rate:.1f}%", disabled=True)
    score_4_2 = 10.0 if ra_rate>=100 else (8.0 if ra_rate>=95 else (6.0 if ra_rate>=90 else (3.0 if ra_rate>=80 else 0.0)))

    c1, c2 = st.columns(2)
    att_days = c1.number_input("出勤核實日數", min_value=0, value=22, key="att_d")
    att_diff = c2.number_input("申報與實際差異次數", min_value=0, value=0, key="att_diff")
    score_4_3 = 8.0 if att_diff==0 else (6.0 if att_diff==1 else (4.0 if att_diff==2 else (2.0 if att_diff==3 else 0.0)))

    # 總分與一票否決
    st.markdown("---")
    total_score = score_1_1 + score_1_2 + score_1_3 + score_2_1 + score_2_2 + score_2_3 + score_3_1 + score_3_2 + score_4_1 + score_4_2 + score_4_3
    
    st.markdown('<div class="section-header">三、 PMD 審核評級與一票否決機制</div>', unsafe_allow_html=True)
    veto_triggered = st.checkbox("⚠️ 是否觸發「重大違規與一票否決」（嚴重失聯≥5次 / 人為重大事故 / 虛報考勤與資產問題）")
    
    if veto_triggered:
        final_grade = "F級（不合格）"
        grade_desc = "因觸發 PMD 重大違規條款，當月評級強制判定為 F 級"
    else:
        if total_score >= 90: final_grade, grade_desc = "A級（卓越）", "建議按績效獎金基數 120% 發放"
        elif total_score >= 80: final_grade, grade_desc = "B級（良好）", "建議按績效獎金基數 100% 發放"
        elif total_score >= 70: final_grade, grade_desc = "C級（合格）", "建議按績效獎金基數 80% 發放"
        elif total_score >= 60: final_grade, grade_desc = "D級（待改善）", "建議按 50% 發放並啟動 30-60日改善計劃"
        else: final_grade, grade_desc = "F級（不合格）", "當月不發放獎金，進入正式覆核程序"

    m1, m2 = st.columns(2)
    m1.metric("地盤 KPI 最終得分", f"{total_score:.1f} / 100 分")
    m2.metric("PMD 評定等級", final_grade)

    st.markdown('<div class="section-header">四、 PMD 監察評語、工頭反饋與意見</div>', unsafe_allow_html=True)
    pmd_comments = st.text_area("PMD 項目組監察評語 / 地盤現場特別紀錄", placeholder="請填寫地盤巡查發現、跨部門協調表現或需改進事項...")
    foreman_feedback = st.text_area("相關工頭及組內同事意見整合", placeholder="記錄直屬主管詢問相關工頭後之反饋...")
    emp_agree = st.radio("被考核員工意向：", ["同意評分", "不同意評分（請於下方註明理由）"])
    emp_reasons = st.text_area("員工不同意理由（如適用）")

    submitted = st.form_submit_button("💾 匯出 PMD 地盤 KPI 考核 PDF 報告", type="primary")

if submitted:
    if not emp_name:
        st.error("請輸入被考核員工姓名！")
    else:
        data = {
            "emp_name": emp_name, "project_site": project_site, "supervisor": supervisor,
            "pmd_rep": pmd_rep, "eval_month": eval_month, "sign_date": str(sign_date),
            "eval_role": eval_role,
            "scores": {
                "s1_1": score_1_1, "c1_1_valid": valid_calls, "c1_1_ontime": ontime_calls, "c1_1_rate": call_rate,
                "s1_2": score_1_2, "c1_2_tot": rep_tot, "c1_2_ok": rep_ok, "c1_2_rate": rep_rate,
                "s1_3": score_1_3, "c1_3_tot": trip_tot, "c1_3_miss": trip_miss,
                "s2_1": score_2_1, "c2_1_tot": m_tot, "c2_1_ok": m_ok, "c2_1_rate": m_rate,
                "s2_2": score_2_2, "c2_2_tot": insp_tot, "c2_2_ok": insp_ok, "c2_2_rate": insp_rate,
                "s2_3": score_2_3, "c2_3_min": err_min, "c2_3_med": err_med, "c2_3_maj": err_maj,
                "s3_1": score_3_1, "c3_1_tot": mat_tot, "c3_1_ok": mat_ok, "c3_1_rate": mat_rate,
                "s3_2": score_3_2, "c3_2_cost": mat_cost, "c3_2_loss": loss_cost, "c3_2_rate": loss_rate,
                "s4_1": score_4_1, "c4_1_tot": safe_tot, "c4_1_done": safe_done, "c4_1_rate": safe_rate,
                "s4_2": score_4_2, "c4_2_tot": ra_tot, "c4_2_ok": ra_ok, "c4_2_rate": ra_rate,
                "s4_3": score_4_3, "c4_3_days": att_days, "c4_3_diff": att_diff
            },
            "total_score": total_score, "final_grade": final_grade, "grade_desc": grade_desc,
            "veto_triggered": veto_triggered, "pmd_comments": pmd_comments,
            "foreman_feedback": foreman_feedback, "emp_agree": emp_agree, "emp_reasons": emp_reasons
        }
        pdf_file = build_pdf(data)
        st.success("✅ PMD 地盤 KPI 評核報告已成功生成！")
        with open(pdf_file, "rb") as f:
            st.download_button("📥 下載 PMD 地盤 KPI 報告 (PDF)", f.read(), file_name=f"JO_PMD_KPI_{emp_name}_{eval_month}.pdf", mime="application/pdf")
