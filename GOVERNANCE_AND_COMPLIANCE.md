# 🛡️ 治理、法規與標準合規架構聲明 (Governance & Regulatory Compliance Framework)

**文件控制編號 (Document Ref):** `JO-GOV-KPI-001`  
**版本 (Version):** `v2.0 (2026 Edition)`  
**適用系統 (Target System):** `jo-pmd-site-kpi` (東淦工程高級管工 KPI 績效評核系統)  

---

## 1. 核心設計原則與資料架構 (Core Architecture & Principles)

本系統專為工程地盤現場之關鍵績效指標（KPI）量化計算與文件生成設計，自架構底層落實以下原則：

* **零資料保留架構 (Zero-Data-Retention & Stateless Architecture):**  
  系統採用完全無狀態（Stateless）記憶體運算模式。使用者在 Web 介面輸入之姓名、員工編號、地盤數據及評語，僅在當前連線 Session 內暫存用於即時運算與 PDF 渲染，**伺服器端不設任何永久性資料庫（No Persistent Storage / No Database）**。Session 結束或網頁重新整理後，所有暫存數據立即自記憶體清除。
* **確定性演算法 (Deterministic Scoring Logic):**  
  系統內嵌之 11 項 KPI 得分計算規則與一票否決判定完全基於確定性數學邏輯與硬編碼邊界條件（Hardcoded Thresholds），**不包含黑箱自我學習模型或不可解釋之自動化決策系統**。

---

## 2. 全球與本地法規適用性評估 (Regulatory & Standards Applicability Analysis)

| 規範 / 標準名稱 | 適用情況 (Status) | 項目落實與合規控制說明 (Compliance Implementation) |
| :--- | :---: | :--- |
| **香港《個人資料（私隱）條例》(PDPO, Cap. 486)** | **全面適用** | 嚴格遵守保障資料原則（DPP）。本系統收集員工姓名、編號僅用於生成當月評核紀錄；採用零留存架構，符合 DPP 2（資料保留期限）及 DPP 4（資料保安）；不作目的外轉移（DPP 3）。 |
| **ISO 9001:2015 (品質管理體系 - QMS)** | **全面適用** | 落實**條款 7.1.5（監控與量測資源）**及**條款 7.5（文件化資訊）**。系統提供「ISO 7.5 可追溯證據單號」欄位，確保每項扣分與評估均具備可核實之工程記錄（Audit Trail）。 |
| **ISO/IEC 27001:2022 (資訊安全管理)** | **全面適用** | 符合 A.8.8（技術弱點管理）及 A.8.24（密碼編譯）。傳輸過程全程強制 HTTPS/TLS 1.3 加密，無後端儲存漏洞風險。 |
| **ISO/IEC 42001:2023 (AI 管理體系)** | **部分適用 / 治理對齊** | 本系統為確定性演算法輔助工具。對齊標準之「透明度（Transparency）」、「可解釋性（Explainability）」與「人類監督（Human-in-the-Loop, HITL）」，最終結果須經 4 方簽署確認。 |
| **歐盟《通用數據保障條例》(GDPR)** | **參考對齊** | 系統主要營運於香港且未主動向歐盟境內個人提供服務。架構設計參考 GDPR Article 5（資料最小化）及 Article 25（Data Protection by Design and by Default）。 |
| **歐盟人工智慧法 (EU AI Act)** | **原則排除 / 最低風險** | 本系統不具備自主推論能力，屬固定規則計算工具，不屬於 Annex III 所定義之高風險 AI 招募/晉升評估系統；若作廣義參照，其透明度與人工覆核機制已滿足低風險要求。 |

---

## 3. 人工介入與最終決策機制 (Human-in-the-Loop & Due Process)

為保障僱員法定權益與程序正義，本系統之評分與建議**不得單獨作為終止僱傭或紀律處分之唯一法律依據**：
1. **四方簽署機制：** 報告須經被考核員工、直屬主管、QMS/HR 審核員及公司代表書面/電子簽署方具效力。
2. **申訴與覆核權：** 員工保留對評分提出異議之權利，評定為 D 或 F 級時自動提示進入 ISO 糾正措施（CAPA）與 30–60 日績效改善計劃（PIP）。

---

## 4. 變更管理與版本控制 (Change Control)

任何關於 KPI 權重、分數門檻或法規宣告之修改，均須遵循東淦工程內部 QMS 變更流程，並於 GitHub Repository 留下對應之 Commit 簽署紀錄。
