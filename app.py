import streamlit as st
from datetime import datetime
from generate_pdf import build_pdf

st.set_page_config(
    page_title="東淦工程 - 地盤 KPI 考核",
    page_icon="🏗️",
    layout="centered" # 改為 centered 更適合手機直屏閱讀
)

# 手機專用 CSS 優化
st.markdown("""
<style>
    /* 針對手機螢幕調整字體與間距 */
    .pmd-title { font-size: 20px; font-weight: bold; color: #1E3A8A; text-align: center; }
    .pmd-subtitle { font-size: 13px; font-weight: 600; color: #0284C7; text-align: center; margin-bottom: 12px; }
    .section-header { font-size: 15px; font-weight: bold; color: #FFFFFF; background-color: #1E3A8A; padding: 6px 10px; border-radius: 4px; margin-top: 15px; margin-bottom: 10px; }
    .kpi-card { background-color: #F8FAFC; border: 1px solid #E2E8F0; border-left: 4px solid #0284C7; padding: 10px; border-radius: 4px; font-size: 13px; margin-bottom: 8px; }
    
    /* 大按鈕方便手機觸控 */
    .stButton>button { background-color: #1E3A8A; color: white; font-weight: bold; border-radius: 8px; width: 100%; height: 3.2em; font-size: 16px; }
    
    /* 調整輸入框高度 */
    div[data-baseweb="input"] { font-size: 16px !important; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="pmd-title">東淦工程有限公司</div>', unsafe_allow_html=True)
st.markdown('<div class="pmd-subtitle">📱 高級管工 KPI 考核系統 (Mobile Ready)</div>', unsafe_allow_html=True)

# 基本資料
st.markdown('<div class="section-header">一、 基本資料</div>', unsafe_allow_html=True)

emp_name = st.text_input("員工姓名", placeholder="例如：陳大文")
project_site = st.text_input("所屬項目／地盤", placeholder="例如：啟德地盤 A區")
supervisor = st.text_input("直屬上司", placeholder="例如：張偉明 工程經理")

col_m1, col_m2 = st.columns(2)
with col_m1:
    eval_month = st.text_input("考核週期", value=datetime.now().strftime("%Y年%m月份"))
with col_m2:
    sign_date = st.date_input("簽署日期", value=datetime.now())

# ==================== DIMENSION 1 ====================
st.markdown('<div class="section-header">二、 溝通及匯報（20%）</div>', unsafe_allow_html=True)

# 1.1
st.markdown("#### 1.1 緊急通訊準時回覆率 (上限 8 分)")
st.markdown("""
<div class="kpi-card">
<b>公式：</b>限時內回覆 ÷ 有效緊急聯絡總數 × 100%<br>
<b>標準：</b>≥95% (8分) | 90-94% (6分) | 85-89% (4分) | 80-84% (2分) | <80% (0分)
</div>
""", unsafe_allow_html=True)

v_calls = st.number_input("有效緊急聯絡總數 (次)", min_value=0, value=0, step=1, key="v_calls")
o_calls = st.number_input("準時回覆次數 (次)", min_value=0, value=0, step=1, key="o_calls")

rate_1_1 = (o_calls / v_calls * 100) if v_calls > 0 else 0.0
score_1_1 = 8.0 if rate_1_1 >= 95 else (6.0 if rate_1_1 >= 90 else (4.0 if rate_1_1 >= 85 else (2.0 if rate_1_1 >= 80 else 0.0)))
if v_calls == 0: score_1_1 = 0.0
st.info(f"📊 準時率：**{rate_1_1:.1f}%** | 💡 即時得分：**{score_1_1} / 8** 分")

st.markdown("---")
# 1.2
st.markdown("#### 1.2 開工、異常及收工匯報完整率 (上限 8 分)")
st.markdown("""
<div class="kpi-card">
<b>公式：</b>合規匯報數 ÷ 應提交匯報總數 × 100%<br>
<b>標準：</b>100% (8分) | 95-99% (6分) | 90-94% (4分) | 80-89% (2分) | <80% (0分)
</div>
""", unsafe_allow_html=True)

r_tot = st.number_input("應提交匯報總數", min_value=0, value=0, step=1, key="r_tot")
r_ok = st.number_input("合規匯報數", min_value=0, value=0, step=1, key="r_ok")

rate_1_2 = (r_ok / r_tot * 100) if r_tot > 0 else 0.0
score_1_2 = 8.0 if rate_1_2 >= 100 else (6.0 if rate_1_2 >= 95 else (4.0 if rate_1_2 >= 90 else (2.0 if rate_1_2 >= 80 else 0.0)))
if r_tot == 0: score_1_2 = 0.0
st.info(f"📊 合規率：**{rate_1_2:.1f}%** | 💡 即時得分：**{score_1_2} / 8** 分")

st.markdown("---")
# 1.3
st.markdown("#### 1.3 工作行程及場地交接紀錄 (上限 4 分)")
st.markdown("""
<div class="kpi-card">
<b>標準：</b>0 次漏登 (4分) | 1 次 (3分) | 2 次 (2分) | 3 次 (1分) | ≥4 次 (0分)
</div>
""", unsafe_allow_html=True)

t_tot = st.number_input("應登記移動次數", min_value=0, value=0, step=1, key="t_tot")
t_miss = st.number_input("漏登次數", min_value=0, value=0, step=1, key="t_miss")
score_1_3 = 4.0 if t_miss == 0 else (3.0 if t_miss == 1 else (2.0 if t_miss == 2 else (1.0 if t_miss == 3 else 0.0)))
if t_tot == 0 and t_miss == 0: score_1_3 = 0.0
st.info(f"💡 即時得分：**{score_1_3} / 4** 分")

# ==================== DIMENSION 2 ====================
st.markdown('<div class="section-header">三、 工程進度及技術執行（35%）</div>', unsafe_allow_html=True)

# 2.1
st.markdown("#### 2.1 里程碑按時完成率 (上限 15 分)")
st.markdown("""
<div class="kpi-card">
<b>標準：</b>≥90% (15分) | 85-89% (12分) | 80-84% (9分) | 70-79% (5分) | <70% (0分)
</div>
""", unsafe_allow_html=True)

m_tot = st.number_input("當月到期節點總數", min_value=0, value=0, step=1, key="m_tot")
m_ok = st.number_input("按時完成節點數", min_value=0, value=0, step=1, key="m_ok")
rate_2_1 = (m_ok / m_tot * 100) if m_tot > 0 else 0.0
score_2_1 = 15.0 if rate_2_1 >= 90 else (12.0 if rate_2_1 >= 85 else (9.0 if rate_2_1 >= 80 else (5.0 if rate_2_1 >= 70 else 0.0)))
if m_tot == 0: score_2_1 = 0.0
st.info(f"📊 完成率：**{rate_2_1:.1f}%** | 💡 即時得分：**{score_2_1} / 15** 分")

st.markdown("---")
# 2.2
st.markdown("#### 2.2 首次驗收通過率 (上限 12 分)")
st.markdown("""
<div class="kpi-card">
<b>標準：</b>≥85% (12分) | 80-84% (9分) | 75-79% (6分) | 70-74% (3分) | <70% (0分)
</div>
""", unsafe_allow_html=True)

i_tot = st.number_input("提交檢驗批次總數", min_value=0, value=0, step=1, key="i_tot")
i_ok = st.number_input("首次通過批次數", min_value=0, value=0, step=1, key="i_ok")
rate_2_2 = (i_ok / i_tot * 100) if i_tot > 0 else 0.0
score_2_2 = 12.0 if rate_2_2 >= 85 else (9.0 if rate_2_2 >= 80 else (6.0 if rate_2_2 >= 75 else (3.0 if rate_2_2 >= 70 else 0.0)))
if i_tot == 0: score_2_2 = 0.0
st.info(f"📊 通過率：**{rate_2_2:.1f}%** | 💡 即時得分：**{score_2_2} / 12** 分")

st.markdown("---")
# 2.3
st.markdown("#### 2.3 圖紙版本/RFI/技術交底 (上限 8 分)")
st.markdown("""
<div class="kpi-card">
<b>標準：</b>0 宗 (8分) | 1 輕微 (6分) | 1 中度或 ≥2 輕微 (4分) | 1 重大 (0分)
</div>
""", unsafe_allow_html=True)

e_min = st.number_input("輕微事件 (宗)", min_value=0, value=0, step=1, key="e_min")
e_med = st.number_input("中度事件 (宗)", min_value=0, value=0, step=1, key="e_med")
e_maj = st.number_input("重大事件 (宗)", min_value=0, value=0, step=1, key="e_maj")
score_2_3 = 0.0 if e_maj >= 1 else (4.0 if (e_med == 1 or e_min >= 2) else (6.0 if e_min == 1 else 8.0))
st.info(f"💡 即時得分：**{score_2_3} / 8** 分")

# ==================== DIMENSION 3 ====================
st.markdown('<div class="section-header">四、 物料及成本控制（15%）</div>', unsafe_allow_html=True)

# 3.1
st.markdown("#### 3.1 物料核對準確率 (上限 8 分)")
st.markdown("""
<div class="kpi-card">
<b>標準：</b>≥98% (8分) | 95-97% (6分) | 92-94% (4分) | 90-91% (2分) | <90% (0分)
</div>
""", unsafe_allow_html=True)

mat_tot = st.number_input("應處理物料項目", min_value=0, value=0, step=1, key="mat_tot")
mat_ok = st.number_input("準確項目", min_value=0, value=0, step=1, key="mat_ok")
rate_3_1 = (mat_ok / mat_tot * 100) if mat_tot > 0 else 0.0
score_3_1 = 8.0 if rate_3_1 >= 98 else (6.0 if rate_3_1 >= 95 else (4.0 if rate_3_1 >= 92 else (2.0 if rate_3_1 >= 90 else 0.0)))
if mat_tot == 0: score_3_1 = 0.0
st.info(f"📊 準確率：**{rate_3_1:.1f}%** | 💡 即時得分：**{score_3_1} / 8** 分")

st.markdown("---")
# 3.2
st.markdown("#### 3.2 可避免物料損耗率 (上限 7 分)")
st.markdown("""
<div class="kpi-card">
<b>標準：</b>≤2% (7分) | >2-3% (5分) | >3-4% (3分) | >4-5% (1分) | >5% (0分)
</div>
""", unsafe_allow_html=True)

mc = st.number_input("領用材料成本 (HK$)", min_value=0.0, value=0.0, step=1000.0, key="mc")
lc = st.number_input("可避免損耗金額 (HK$)", min_value=0.0, value=0.0, step=500.0, key="lc")
rate_3_2 = (lc / mc * 100) if mc > 0 else 0.0
score_3_2 = 7.0 if rate_3_2 <= 2.0 else (5.0 if rate_3_2 <= 3.0 else (3.0 if rate_3_2 <= 4.0 else (1.0 if rate_3_2 <= 5.0 else 0.0)))
if mc == 0: score_3_2 = 0.0
st.info(f"📊 損耗率：**{rate_3_2:.2f}%** | 💡 即時得分：**{score_3_2} / 7** 分")

# ==================== DIMENSION 4 ====================
st.markdown('<div class="section-header">五、 安全及團隊管理（30%）</div>', unsafe_allow_html=True)

# 4.1
st.markdown("#### 4.1 安全巡查整改完成率 (上限 12 分)")
st.markdown("""
<div class="kpi-card">
<b>標準：</b>≥95% (12分) | 90-94% (9分) | 85-89% (6分) | 80-84% (3分) | <80% (0分)
</div>
""", unsafe_allow_html=True)

s_tot = st.number_input("應完成項目數", min_value=0, value=0, step=1, key="s_tot")
s_done = st.number_input("按時完成數", min_value=0, value=0, step=1, key="s_done")
rate_4_1 = (s_done / s_tot * 100) if s_tot > 0 else 0.0
score_4_1 = 12.0 if rate_4_1 >= 95 else (9.0 if rate_4_1 >= 90 else (6.0 if rate_4_1 >= 85 else (3.0 if rate_4_1 >= 80 else 0.0)))
if s_tot == 0: score_4_1 = 0.0
st.info(f"📊 完成率：**{rate_4_1:.1f}%** | 💡 即時得分：**{score_4_1} / 12** 分")

st.markdown("---")
# 4.2
st.markdown("#### 4.2 風險評估及事件呈報 (上限 10 分)")
st.markdown("""
<div class="kpi-card">
<b>標準：</b>100% (10分) | 95-99% (8分) | 90-94% (6分) | 80-89% (3分) | <80% (0分)
</div>
""", unsafe_allow_html=True)

ra_tot = st.number_input("應完成項目數 ", min_value=0, value=0, step=1, key="ra_tot")
ra_ok = st.number_input("合規完成數 ", min_value=0, value=0, step=1, key="ra_ok")
rate_4_2 = (ra_ok / ra_tot * 100) if ra_tot > 0 else 0.0
score_4_2 = 10.0 if rate_4_2 >= 100 else (8.0 if rate_4_2 >= 95 else (6.0 if rate_4_2 >= 90 else (3.0 if rate_4_2 >= 80 else 0.0)))
if ra_tot == 0: score_4_2 = 0.0
st.info(f"📊 合規率：**{rate_4_2:.1f}%** | 💡 即時得分：**{score_4_2} / 10** 分")

st.markdown("---")
# 4.3
st.markdown("#### 4.3 出勤核實及調配 (上限 8 分)")
st.markdown("""
<div class="kpi-card">
<b>標準：</b>0 次差異 (8分) | 1 次 (6分) | 2 次 (4分) | 3 次 (2分) | ≥4 次 (0分)
</div>
""", unsafe_allow_html=True)

att_d = st.number_input("核實日數", min_value=0, value=0, step=1, key="att_d")
att_diff = st.number_input("申報與實際差異次數", min_value=0, value=0, step=1, key="att_diff")
score_4_3 = 8.0 if att_diff == 0 else (6.0 if att_diff == 1 else (4.0 if att_diff == 2 else (2.0 if att_diff == 3 else 0.0)))
if att_d == 0 and att_diff == 0: score_4_3 = 0.0
st.info(f"💡 即時得分：**{score_4_3} / 8** 分")

# ==================== SUMMARY ====================
st.markdown('<div class="section-header">六、 綜合評分結果</div>', unsafe_allow_html=True)

total_score = score_1_1 + score_1_2 + score_1_3 + score_2_1 + score_2_2 + score_2_3 + score_3_1 + score_3_2 + score_4_1 + score_4_2 + score_4_3

veto_triggered = st.checkbox("⚠️ 觸發「重大違規與一票否決」")

if veto_triggered:
    final_grade = "F級（不合格）"
    grade_desc = "因觸發重大違規事項，評定為 F 級"
else:
    if total_score >= 90: final_grade, grade_desc = "A級（卓越）", "按績效獎金基數 120% 發放"
    elif total_score >= 80: final_grade, grade_desc = "B級（良好）", "按績效獎金基數 100% 發放"
    elif total_score >= 70: final_grade, grade_desc = "C級（合格）", "按績效獎金基數 80% 發放"
    elif total_score >= 60: final_grade, grade_desc = "D級（待改善）", "按 50% 發放並進入改善計劃"
    else: final_grade, grade_desc = "F級（不合格）", "當月不發放獎金"

st.metric("最終總得分", f"{total_score:.1f} / 100 分")
st.metric("評定績效等級", final_grade)
st.success(f"💡 **建議：** {grade_desc}")

emp_agree = st.radio("員工意向：", ["同意", "不同意"])
emp_comments = st.text_area("員工意見／備註", placeholder="請在此填寫備註...")
bonus_base = st.text_input("績效獎金基數", placeholder="例如：HK$ 5,000")

st.markdown("<br>", unsafe_allow_html=True)
if st.button("📱 匯出 PDF 考核報告", type="primary"):
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
        st.success("✅ PDF 報告已生成！")
        with open(pdf_file, "rb") as f:
            st.download_button("📥 下載 PDF 報告", f.read(), file_name=f"JO_KPI_{emp_name}_{eval_month}.pdf", mime="application/pdf")
