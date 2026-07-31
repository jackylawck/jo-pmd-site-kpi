# jo-pmd-site-kpi | 東淦工程 PMD 地盤同事 KPI 績效評核系統

本專案專為 **東淦工程有限公司 (Jumbo Orient Contracting Limited)** 設計，旨在將《高級管工關鍵績效指標 (KPI) 考核協議書》數位化。系統支援 PMD (Project Management Department) 及地盤主管透過手機或電腦進行現場實測評核、動態即時算分，並自動產出符合 ISO 規範的標準 PDF 報告。

---

## 🎯 核心功能與設計亮點

1. **📱 手機端極致優化 (Mobile-First & Real-time Scoring)**
   - 採用單欄自適應介面與大尺寸觸控組件，適合地盤現場單手操作。
   - 移除阻塞式表單，輸入數據（如電話次數、巡查次數）後**即時（Real-time）自動計算百分比與 11 項 KPI 得分**。

2. **🛡️ ISO 9001 & ISO 42001 合規治理**
   - **條款 7.5 可追溯性**：特別加入「ISO 7.5 可追溯核實證據單號/文件編號」欄位（如地盤日誌、安全審核單號），避免無憑據扣分引發 HR 爭議。
   - **演算法透明度**：公開 11 項 KPI 計算公式與一票否決（F 級）條件，符合 ISO 42001 自動化評核標準。

3. **⚖️ 嚴謹的一票否決與 PIP 機制**
   - 支援「重大失聯（≥5次）」、「人為重大事故」或「誠信/考勤虛報」之勾選，自動觸發一票否決（強制 F 級），並自動連結至 ISO 糾正措施程序 (CAPA) 與 30-60 日績效改善計劃 (PIP)。

4. **📄 100% 穩定之 ReportLab PDF 引擎**
   - 採用純 Python `ReportLab` 引擎，徹底解決 Cloud 部署環境缺少 C 語言底層庫而引致的 `OSError` 報錯。
   - 生成含 4 方審核簽署欄（被考核員工、直屬上司、QMS/HR 審核員、公司代表）的官方 A4 評核報告。
   - 檔名採用 ISO 標準化命名：`[員工編號]_[員工姓名]_[考核日期].pdf`（例如：`E26001_陳大文_20260731.pdf`），極方便 HR 歸檔與稽核。

---

## 📦 專案檔案結構 (Project Architecture)

```text
jo-pmd-site-kpi/
├── app.py                # Streamlit 前端網頁應用主程式 (包含即時計分與 ISO 欄位)
├── generate_pdf.py       # ReportLab PDF 報告生成模組 (含 ISO 文件管制與 4 方簽署欄)
├── requirements.txt      # Python 套件依賴清單 (reportlab, streamlit, pandas)
└── README.md             # 專案說明與部署指南
```
---

## 🚀 部署至 Streamlit Cloud 指南
將最新代碼 Commit & Push 至 GitHub 儲存庫 jackylawck/jo-pmd-site-kpi。

前往 Streamlit Community Cloud 並登入。

選擇 Repository jo-pmd-site-kpi、main 分支與主程式 app.py。

點擊 Deploy! 即可完成發布。

🔗 線上測試網址：https://jo-pmd-site-kpi.streamlit.app
