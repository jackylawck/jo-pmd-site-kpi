# 🏛️ AI Governance & Global Regulatory Compliance Framework
### 東淦工程有限公司 (Jumbo Orient) - 智能扣帳方查詢系統管治合規架構文件

本文件由專案管理與 AI 管治負責人維護，旨在明確界定本系統之法律定位、全球法規適用性判定、豁免邊界，以及對應之國際標準控制措施。

---

## 1. 全球法規適用性與管轄邊界判定 (Global Regulatory Applicability Matrix)

| 法律 / 監管框架 (Framework) | 適用性判定 (Status) | 法律依據與合規邊界分析 (Legal Justification & Risk Boundary) |
| :--- | :---: | :--- |
| **EU Artificial Intelligence Act (EU AI Act)** | **Minimal / No Risk (不適用高風險管控)** | 本系統為內部營運輔助之語意檢索工具（Deterministic Semantic Lookup），不屬於 Annex III 所列之高風險 AI 系統（如生物識別、關鍵基礎設施控管、招聘篩選或信用評級），亦非 GPAI Foundation Model。 |
| **EU GDPR (Regulation (EU) 2016/679)** | **Exempt / Compliant (默認不處理歐盟個人資料)** | 系統設計用途限定為地盤工程扣帳代號比對，不收集亦不處理歐盟境內居民之個人資料。系統架構完全實踐 Article 25 之「Data Protection by Design and by Default」。 |
| **香港《個人資料（私隱）條例》(Cap. 486 PDPO)** | **Fully Compliant (完全合規)** | 系統運作採「零持久化存儲（Zero Data at Rest）」，不設使用者註冊、追蹤 Cookies 或後端數據庫，完全符合六項保障資料原則（DPPs），特別是 DPP2（數據保留）與 DPP4（數據安全）。 |
| **ISO/IEC 42001:2023 (AIMS)** | **Aligned (完全對齊)** | 符合人工智能管理體系之系統透明度（A.8.2）、數據最小化（A.6.2）及人工監督（A.8.3）要求。 |
| **ISO/IEC 27001:2022 (ISMS)** | **Aligned (完全對齊)** | 符合資訊安全控制措施，特別是 A.8.12（數據洩漏防護）與 A.8.24（安全開發生命週期）。 |

---

## 2. 系統架構級合規控制措施 (Architectural Compliance Controls)

* **數據最小化與即時銷毀 (Data Minimization - ISO 42001 A.6.2 / GDPR Art. 5(1)(c))：**
  * 使用者上傳之 `.xlsx` 檔案僅暫存於使用者獨立之 Session 揮發性記憶體（RAM）。
  * 伺服器端不設任何形式之持久化數據庫（No SQL/NoSQL Database, No Persistent Log Storage）。
  * 網頁關閉或重新整理時，所有記憶體指標即刻釋放並全量銷毀。
* **數據隔離與防洩漏 (Air-Gapped Embedding & DLP - ISO 27001 A.8.12)：**
  * 語意向量計算使用開源多語言嵌入模型於本地端完成。
  * 徹底切斷任何外部第三方生成式 AI API（如 OpenAI, Anthropic, Google Gemini），確保內部資料絕不出境或傳輸予第三方。
* **確定性檢索與抗幻覺 (Deterministic Output & Anti-Hallucination - ISO 42001 A.8.2)：**
  * 系統僅提供基於 FAISS 向量相似度與精準關鍵字之文件行數檢索，不具備自主文本生成功能，從根本杜絕 AI 幻覺與虛假陳述風險。

---

## 3. 人工介入與最終決策責任 (Human-in-the-Loop & Accountability - ISO 42001 A.8.3)

* **輔助工具定位：** 本系統明確定位為「運營決策支援工具（Decision Support System）」，不具備自主法定或財務決定權限。
* **最終審核：** 所有扣帳代號之最終採用、Debit Note 之簽發及分判商責任確認，必須由相關權責主管人員（Authorized Human Personnel）審核並承擔最終管理責任。

---

## 4. 變更與審計歷史 (Audit & Change Control)

* **當前版本 (Version):** 1.0.0
* **維護負責人 (Governance Lead):** Jacky Law
* **最近檢視日期 (Last Reviewed):** 2026 年 8 月
