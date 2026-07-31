import streamlit as st
from datetime import datetime
from generate_pdf import build_pdf

st.set_page_config(
    page_title="東淦工程 - PMD 地盤 KPI 考核系統",
    page_icon="🏗️",
    layout="wide"
)

# 東淦工程 PMD 視覺主題
st.markdown("""
<style>
    .pmd-title { font-size: 26px; font-weight: bold; color: #1E3A8A; margin-bottom: 2px; }
    .pmd-subtitle { font-size: 15px; font-weight: 600; color: #0284C7; margin-bottom: 15px; }
    .section-header { font-size: 18px; font-weight: bold; color: #FFFFFF; background-color: #1E3A8A; padding: 6px 12px; border-radius: 4px; margin-top: 20px; margin-bottom: 15px; }
    .kpi-card { background-color: #F8FAFC; border: 1px solid #E2E8F0; border-left: 4px solid #0284C7; padding: 12px; border-radius: 4px; margin-bottom: 15px; }
    .stButton>button { background-color: #1E3A8A; color: white; font-weight: bold; border-radius: 6px; width: 100%; height: 3em; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="pmd-title">東淦工程有限公司 Jumbo Orient Contracting Limited</div>', unsafe_allow_html=True)
st.markdown('<div class="pmd-subtitle">📋 高級管工 (Senior Foreman) 關鍵績效指標 (KPI) 考核協議書 (jo-pmd-site-kpi)</div>', unsafe_allow_html=True)

# 基本資料
st.markdown('<div class="section-header">一、 基本資料</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    emp_name = st.text_input("員工姓名", placeholder="例如：陳大文")
    project_site = st.text_input("所屬項目／地盤", placeholder="例如：啟德地盤 A區")
with col2:
    supervisor = st.text_input("直屬上司", placeholder="例如：張偉明 工程經理")
    eval_month = st.text_input("考核週期", value=datetime.now().strftime("%Y年%m月份"))
with col3:
    sign_date = st.date_input("被考核人簽署日期", value=datetime.now())

# ==================== DIMENSION 1 ====================
st.markdown('<div class="section-header">二、 溝通及匯報（權重 20%）</div>', unsafe_allow_html=True)

# 1.1
st.markdown("#### 1.1 緊急通訊準時回覆率 (上限 8 分)")
c_left, c_right = st.columns([1, 1])
with c_left:
    st.markdown("""
    <div class="kpi-card">
    <b>量度方式與公式：</b>限時內完成回覆的有效緊急聯絡 ÷ 有效緊急聯絡總數 × 100%<br>
    • 漏接電話於 30 分鐘內回電；WhatsApp/微信緊急訊息於 60 分鐘內回覆。<br>
    <b>目標值與評分標準：</b><br>
    ≥95% → <b>8分</b> | 90–94.9% → <b>6分</b> | 85–89.9% → <b>4分</b> | 80–84.9% → <b>2分</b> | <80% → <b>0分</b>
    </div>
    """, unsafe_allow_html=True)
with c_right:
    v_calls = st.number_input("有效緊急聯絡總數 (次)", min_value=0, value=0, step=1, key="v_calls")
    o_calls = st.number_input("準時回覆次數 (次)", min_value=0, value=0, step=1, key="o_calls")
    
    rate_1_1 = (o_calls / v_calls * 100) if v_calls > 0 else 0.0
    score_1_1 = 8.0 if rate_1_1 >= 95 else (6.0 if rate_1_1 >= 90 else (4.0 if rate_1_1 >= 85 else (2.0 if rate_1_1 >= 80 else 0.0)))
    if v_calls == 0: score_1_1 = 0.0
    st.info(f"📊 準時率：**{rate_1_1:.1f}%** | 💡 即時得分：**{score_1_1} / 8** 分")

st.markdown("---")
# 1.2
st.markdown("#### 1.2 開工、異常及收工匯報完整率 (上限 8 分)")
c_left, c_right = st.columns([1, 1])
with c_left:
    st.markdown("""
    <div class="kpi-card">
    <b>量度方式與公式：</b>準時且資料完整的匯報數 ÷ 應提交匯報總數 × 100%<br>
    • 開工匯報於 30 分鐘內；收工匯報於 60 分鐘內；重大異常即時呈報。<br>
    <b>目標值與評分標準：</b><br>
    100% → <b>8分</b> | 95–99.9% → <b>6分</b> | 90–94.9% → <b>4分</b> | 80–89.9% → <b>2分</b> | <80% → <b>0分</b>
    </div>
    """, unsafe_allow_html=True)
with c_right:
    r_tot = st.number_input("應提交匯報總數", min_value=0, value=0, step=1, key="r_tot")
    r_ok = st.number_input("合規匯報數", min_value=0, value=0, step=1, key="r_ok")
    
    rate_1_2 = (r_ok / r_tot * 100) if r_tot > 0 else 0.0
    score_1_2 = 8.0 if rate_1_2 >= 100 else (6.0 if rate_1_2 >= 95 else (4.0 if rate_1_2 >= 90 else (2.0 if rate_1_2 >= 80 else 0.0)))
    if r_tot == 0: score_1_2 = 0.0
    st.info(f"📊 合規率：**{rate_1_2:.1f}%** | 💡 即時得分：**{score_1_2} / 8** 分")

st.markdown("---")
# 1.3
st.markdown("#### 1.3 工作行程及場地交接紀錄 (上限 4 分)")
c_left, c_right = st.columns([1, 1])
with c_left:
    st.markdown("""
    <div class="kpi-card">
    <b>量度方式與公式：</b>由辦公室/廠房/地盤跨地點移動前登記離開時間、目的地及交接人。<br>
    <b>目標值與評分標準：</b><br>
    0 次漏登 → <b>4分</b> | 1 次 → <b>3分</b> | 2 次 → <b>2分</b> | 3 次 → <b>1分</b> | ≥4 次 → <b>0分</b>
    </div>
    """, unsafe_allow_html=True)
with c_right:
    t_tot = st.number_input("應登記移動次數", min_value=0, value=0, step=1, key="t_tot")
    t_miss = st.number_input("漏登次數", min_value=0, value=0, step=1, key="t_miss")
    score_1_3 = 4.0 if t_miss == 0 else (3.0 if t_miss == 1 else (2.0 if t_miss == 2 else (1.0 if t_miss == 3 else 0.0)))
    if t_tot == 0 and t_miss == 0: score_1_3 = 0.0
    st.info(f"💡 即時得分：**{score_1_3} / 4** 分")

# ==================== DIMENSION 2 ====================
st.markdown('<div class="section-header">三、 工程進度及技術執行（權重 35%）</div>', unsafe_allow_html=True)

# 2.1
st.markdown("#### 2.1 調整後里程碑按時完成率 (上限 15 分)")
c_left, c_right = st.columns([1, 1])
with c_left:
    st.markdown("""
    <div class="kpi-card">
    <b>量度方式與公式：</b>按時完成到期里程碑 ÷ 當月到期且可歸責節點 × 100%<br>
    • 排除天氣、圖紙未批、總承建商次序改動等不可控因素。<br>
    <b>目標值與評分標準：</b><br>
    ≥90% → <b>15分</b> | 85–89.9% → <b>12分</b> | 80–84.9% → <b>9分</b> | 70–79.9% → <b>5分</b> | <70% → <b>0分</b>
    </div>
    """, unsafe_allow_html=True)
with c_right:
    m_tot = st.number_input("當月到期節點總數", min_value=0, value=0, step=1, key="m_tot")
    m_ok = st.number_input("按時完成節點數", min_value=0, value=0, step=1, key="m_ok")
    rate_2_1 = (m_ok / m_tot * 100) if m_tot > 0 else 0.0
    score_2_1 = 15.0 if rate_2_1 >= 90 else (12.0 if rate_2_1 >= 85 else (9.0 if rate_2_1 >= 80 else (5.0 if rate_2_1 >= 70 else 0.0)))
    if m_tot == 0: score_2_1 = 0.0
    st.info(f"📊 完成率：**{rate_2_1:.1f}%** | 💡 即時得分：**{score_2_1} / 15** 分")

st.markdown("---")
# 2.2
st.markdown("#### 2.2 首次驗收通過率 (上限 12 分)")
c_left, c_right = st.columns([1, 1])
with c_left:
    st.markdown("""
    <div class="kpi-card">
    <b>量度方式與公式：</b>首次正式檢驗即獲接受批次 ÷ 正式提交檢驗批次總數 × 100%<br>
    • 適用於焊接外觀、尺寸、平直度、防銹油漆膜厚等。<br>
    <b>目標值與評分標準：</b><br>
    ≥85% → <b>12分</b> | 80–84.9% → <b>9分</b> | 75–79.9% → <b>6分</b> | 70–74.9% → <b>3分</b> | <70% → <b>0分</b>
    </div>
    """, unsafe_allow_html=True)
with c_right:
    i_tot = st.number_input("正式提交檢驗批次總數", min_value=0, value=0, step=1, key="i_tot")
    i_ok = st.number_input("首次通過批次數", min_value=0, value=0, step=1, key="i_ok")
    rate_2_2 = (i_ok / i_tot * 100) if i_tot > 0 else 0.0
    score_2_2 = 12.0 if rate_2_2 >= 85 else (9.0 if rate_2_2 >= 80 else (6.0 if rate_2_2 >= 75 else (3.0 if rate_2_2 >= 70 else 0.0)))
    if i_tot == 0: score_2_2 = 0.0
    st.info(f"📊 通過率：**{rate_2_2:.1f}%** | 💡 即時得分：**{score_2_2} / 12** 分")

st.markdown("---")
# 2.3
st.markdown("#### 2.3 圖紙版本、RFI 及技術交底 (上限 8 分)")
c_left, c_right = st.columns([1, 1])
with c_left:
    st.markdown("""
    <div class="kpi-card">
    <b>量度方式與公式：</b>只計經調查確認因未核對版本、錯誤解讀或未交底而造成的可避免事件。<br>
    <b>目標值與評分標準：</b><br>
    0 宗 → <b>8分</b> | 1 宗輕微 → <b>6分</b> | 1 宗中度或 ≥2 宗輕微 → <b>4分</b> | 1 宗重大 → <b>0分</b>
    </div>
    """, unsafe_allow_html=True)
with c_right:
    e_min = st.number_input("輕微事件 (宗)", min_value=0, value=0, step=1, key="e_min")
    e_med = st.number_input("中度事件 (宗)", min_value=0, value=0, step=1, key="e_med")
    e_maj = st.number_input("重大事件 (宗)", min_value=0, value=0, step=1, key="e_maj")
    score_2_3 = 0.0 if e_maj >= 1 else (4.0 if (e_med == 1 or e_min >= 2) else (6.0 if e_min == 1 else 8.0))
    st.info(f"💡 即時得分：**{score_2_3} / 8** 分")

# ==================== DIMENSION 3 ====================
st.markdown('<div class="section-header">四、 物料及成本控制（權重 15%）</div>', unsafe_allow_html=True)

# 3.1
st.markdown("#### 3.1 物料申請及收貨核對準確率 (上限 8 分)")
c_left, c_right = st.columns([1, 1])
with c_left:
    st.markdown("""
    <div class="kpi-card">
    <b>量度方式與公式：</b>型號、尺寸、數量及日期均正確項目 ÷ 應處理物料項目 × 100%<br>
    <b>目標值與評分標準：</b><br>
    ≥98% → <b>8分</b> | 95–97.9% → <b>6分</b> | 92–94.9% → <b>4分</b> | 90–91.9% → <b>2分</b> | <90% → <b>0分</b>
    </div>
    """, unsafe_allow_html=True)
with c_right:
    mat_tot = st.number_input("應處理物料項目", min_value=0, value=0, step=1, key="mat_tot")
    mat_ok = st.number_input("準確項目", min_value=0, value=0, step=1, key="mat_ok")
    rate_3_1 = (mat_ok / mat_tot * 100) if mat_tot > 0 else 0.0
    score_3_1 = 8.0 if rate_3_1 >= 98 else (6.0 if rate_3_1 >= 95 else (4.0 if rate_3_1 >= 92 else (2.0 if rate_3_1 >= 90 else 0.0)))
    if mat_tot == 0: score_3_1 = 0.0
    st.info(f"📊 準確率：**{rate_3_1:.1f}%** | 💡 即時得分：**{score_3_1} / 8** 分")

st.markdown("---")
# 3.2
st.markdown("#### 3.2 可避免物料損耗率 (上限 7 分)")
c_left, c_right = st.columns([1, 1])
with c_left:
    st.markdown("""
    <div class="kpi-card">
    <b>量度方式與公式：</b>錯誤切割/保管/搬運報廢成本 ÷ 當月已領用材料成本 × 100%<br>
    <b>目標值與評分標準：</b><br>
    ≤2% → <b>7分</b> | >2–3% → <b>5分</b> | >3–4% → <b>3分</b> | >4–5% → <b>1分</b> | >5% → <b>0分</b>
    </div>
    """, unsafe_allow_html=True)
with c_right:
    mc = st.number_input("當月已領用材料成本 (HK$)", min_value=0.0, value=0.0, step=1000.0, key="mc")
    lc = st.number_input("可避免損耗金額 (HK$)", min_value=0.0, value=0.0, step=500.0, key="lc")
    rate_3_2 = (lc / mc * 100) if mc > 0 else 0.0
    score_3_2 = 7.0 if rate_3_2 <= 2.0 else (5.0 if rate_3_2 <= 3.0 else (3.0 if rate_3_2 <= 4.0 else (1.0 if rate_3_2 <= 5.0 else 0.0)))
    if mc == 0: score_3_2 = 0.0
    st.info(f"📊 損耗率：**{rate_3_2:.2f}%** | 💡 即時得分：**{score_3_2} / 7** 分")

# ==================== DIMENSION 4 ====================
st.markdown('<div class="section-header">五、 安全及團隊管理（權重 30%）</div>', unsafe_allow_html=True)

# 4.1
st.markdown("#### 4.1 安全巡查及整改完成率 (上限 12 分)")
c_left, c_right = st.columns([1, 1])
with c_left:
    st.markdown("""
    <div class="kpi-card">
    <b>量度方式與公式：</b>按計劃完成巡查及限期整改數 ÷ 應完成項目 × 100%<br>
    <b>目標值與評分標準：</b><br>
    ≥95% → <b>12分</b> | 90–94.9% → <b>9分</b> | 85–89.9% → <b>6分</b> | 80–84.9% → <b>3分</b> | <80% → <b>0分</b>
    </div>
    """, unsafe_allow_html=True)
with c_right:
    s_tot = st.number_input("應完成項目數", min_value=0, value=0, step=1, key="s_tot")
    s_done = st.number_input("按時完成數", min_value=0, value=0, step=1, key="s_done")
    rate_4_1 = (s_done / s_tot * 100) if s_tot > 0 else 0.0
    score_4_1 = 12.0 if rate_4_1 >= 95 else (9.0 if rate_4_1 >= 90 else (6.0 if rate_4_1 >= 85 else (3.0 if rate_4_1 >= 80 else 0.0)))
    if s_tot == 0: score_4_1 = 0.0
    st.info(f"📊 完成率：**{rate_4_1:.1f}%** | 💡 即時得分：**{score_4_1} / 12** 分")

st.markdown("---")
# 4.2
st.markdown("#### 4.2 風險評估、工具箱會議及事件呈報 (上限 10 分)")
c_left, c_right = st.columns([1, 1])
with c_left:
    st.markdown("""
    <div class="kpi-card">
    <b>量度方式與公式：</b>已按要求完成項目 ÷ 應完成項目 × 100%<br>
    <b>目標值與評分標準：</b><br>
    100% → <b>10分</b> | 95–99.9% → <b>8分</b> | 90–94.9% → <b>6分</b> | 80–89.9% → <b>3分</b> | <80% → <b>0分</b>
    </div>
    """, unsafe_allow_html=True)
with c_right:
    ra_tot = st.number_input("應完成項目數 ", min_value=0, value=0, step=1, key="ra_tot")
    ra_ok = st.number_input("合規完成數 ", min_value=0, value=0, step=1, key="ra_ok")
    rate_4_2 = (ra_ok / ra_tot * 100) if ra_tot > 0 else 0.0
    score_4_2 = 10.0 if rate_4_2 >= 100 else (8.0 if rate_4_2 >= 95 else (6.0 if rate_4_2 >= 90 else (3.0 if rate_4_2 >= 80 else 0.0)))
    if ra_tot == 0: score_4_2 = 0.0
    st.info(f"📊 合規率：**{rate_4_2:.1f}%** | 💡 即時得分：**{score_4_2} / 10** 分")

st.markdown("---")
# 4.3
st.markdown("#### 4.3 出勤核實及人手調配 (上限 8 分)")
c_left, c_right = st.columns([1, 1])
with c_left:
    st.markdown("""
    <div class="kpi-card">
    <b>量度方式與公式：</b>每日核實鐵工人數/工種/位置，突發缺勤及時調配。<br>
    <b>目標值與評分標準：</b><br>
    0 次差異 → <b>8分</b> | 1 次 → <b>6分</b> | 2 次 → <b>4分</b> | 3 次 → <b>2分</b> | ≥4 次 → <b>0分</b>
    </div>
    """, unsafe_allow_html=True)
with c_right:
    att_d = st.number_input("核實日數", min_value=0, value=0, step=1, key="att_d")
    att_diff = st.number_input("申報與實際差異次數", min_value=0, value=0, step=1, key="att_diff")
    score_4_3 = 8.0 if att_diff == 0 else (6.0 if att_diff == 1 else (4.0 if att_diff == 2 else (2.0 if att_diff == 3 else 0.0)))
    if att_d == 0 and att_diff == 0: score_4_3 = 0.0
    st.info(f"💡 即時得分：**{score_4_3} / 8** 分")

# ==================== SUMMARY ====================
st.markdown('<div class="section-header">六、 綜合評分與績效等級評定</div>', unsafe_allow_html=True)

total_score = score_1_1 + score_1_2 + score_1_3 + score_2_1 + score_2_2 + score_2_3 + score_3_1 + score_3_2 + score_4_1 + score_4_2 + score_4_3

veto_triggered = st.checkbox("⚠️ 觸發第五部分「重大違規與一票否決事項」（如嚴重失聯≥5次 / 明知故犯人為重大事故 / 誠信虛報考勤，當月強制判定為 F 級）")

if veto_triggered:
    final_grade = "F級（不合格）"
    grade_desc = "因觸發重大違規事項，評定為 F 級"
else:
    if total_score >= 90: final_grade, grade_desc = "A級（卓越）", "按績效獎金基數 120% 發放"
    elif total_score >= 80: final_grade, grade_desc = "B級（良好）", "按績效獎金基數 100% 發放"
    elif total_score >= 70: final_grade, grade_desc = "C級（合格）", "按績效獎金基數 80% 發放"
    elif total_score >= 60: final_grade, grade_desc = "D級（待改善）", "按績效獎金基數 50% 發放，進入 30-60 日改善計劃"
    else: final_grade, grade_desc = "F級（不合格）", "當月不發放績效獎金，進行正式績效覆核"

m1, m2 = st.columns(2)
m1.metric("最終總得分", f"{total_score:.1f} / 100 分")
m2.metric("評定績效等級", final_grade)

st.success(f"💡 **建議發放及跟進安排：** {grade_desc}")

emp_agree = st.radio("員工是否同意評分：", ["同意", "不同意（請於下方填寫意見）"])
emp_comments = st.text_area("員工意見／不同意理由（如適用）", placeholder="如對評分有異議或需要說明事項，請在此填寫...")
bonus_base = st.text_input("當月績效獎金基數", placeholder="例如：HK$ 5,000")

st.markdown("<br>", unsafe_allow_html=True)
if st.button("💾 生成考核報告並導出 PDF", type="primary"):
    if not emp_name:
        st.error("請填寫員工姓名！")
    else:
        data = {
            "emp_name": emp_name, "project_site": project_site, "supervisor": supervisor,
            "eval_month": eval_month, "sign_date": str(sign_date),
            "scores": {
                "s1_1": score_1_1, "c1_1_valid": v_calls, "c1_1_ontime": o_calls, "c1_1_rate": rate_1_1,
                "s1_2": score_1_2, "c1_2_tot": r_tot, "c1_2_ok": r_ok, "c1_2_rate": rate_1_2,
                "s1_3": score_1_3, "c1_3_tot": t_tot, "c1_3_miss": t_miss,
                "s2_1": score_2_1, "c2_1_tot": m_tot, "c2_1_ok": m_ok, "c2_1_rate": rate_2_1,
                "s2_2": score_2_2, "c2_2_tot": i_tot, "c2_2_ok": i_ok, "c2_2_rate": rate_2_2,
                "s2_3": score_2_3, "c2_3_min": e_min, "c2_3_med": e_med, "c2_3_maj": e_maj,
                "s3_1": score_3_1, "c3_1_tot": mat_tot, "c3_1_ok": mat_ok, "c3_1_rate": rate_3_1,
                "s3_2": score_3_2, "c3_2_cost": mc, "c3_2_loss": lc, "c3_2_rate": rate_3_2,
                "s4_1": score_4_1, "c4_1_tot": s_tot, "c4_1_done": s_done, "c4_1_rate": rate_4_1,
                "s4_2": score_4_2, "c4_2_tot": ra_tot, "c4_2_ok": ra_ok, "c4_2_rate": rate_4_2,
                "s4_3": score_4_3, "c4_3_days": att_d, "c4_3_diff": att_diff
            },
            "total_score": total_score, "final_grade": final_grade, "grade_desc": grade_desc,
            "veto_triggered": veto_triggered, "emp_agree": emp_agree, "emp_comments": emp_comments,
            "bonus_base": bonus_base
        }
        pdf_file = build_pdf(data)
        st.success("✅ KPI 評核報告已成功生成！")
        with open(pdf_file, "rb") as f:
            st.download_button("📥 下載 PDF 報告", f.read(), file_name=f"JO_KPI_{emp_name}_{eval_month}.pdf", mime="application/pdf")
