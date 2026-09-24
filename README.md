# 🌍 LLM-Augmented ESG Data Pipeline & Dashboard

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=googlebard&logoColor=white)
![SQL Server](https://img.shields.io/badge/SQL_Server-CC2927?style=for-the-badge&logo=microsoft-sql-server&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)

Automated ETL pipeline using Python, Google Gemini, SQL Server, and Power BI to extract and visualize corporate ESG metrics.

## 📑 Table of Contents
- [Business Problem](#-business-problem)
- [Architecture & Workflow](#-architecture--workflow)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Power BI Dashboard](#-power-bi-dashboard)
- [Author](#-author)

---

## 🎯 Business Problem
Investors and regulators increasingly demand transparency regarding Environmental, Social, and Governance (ESG) performance. However, ESG data is notoriously unstructured—buried in dense PDF reports and dynamic corporate websites. 

This project solves the manual, error-prone process of ESG data collection by engineering an automated pipeline that scrapes web text, leverages Large Language Models (LLMs) to extract precise metrics, enforces strict data schemas, and warehouses the clean data for BI reporting.

---

## ⚙️ Architecture & Workflow

1. **Data Ingestion (Selenium):** Automates browser navigation to extract raw text from dynamic, JavaScript-heavy corporate sustainability pages.
2. **AI Extraction & Schema Enforcement (Google Gemini & Pydantic):** Passes unstructured text to the Gemini API with strict instructions to map data (Scope 1-3 Emissions, Board Diversity) to a validated Pydantic JSON schema.
3. **Data Warehousing (pyodbc & SQL Server):** Parses the validated JSON and securely loads the records into a relational Microsoft SQL Server database (`Fact_Emissions`).
4. **Data Modeling & Visualization (Power BI):** Connects directly to the SQL Server via DirectQuery/Import, utilizing advanced DAX measures to track corporate carbon footprints against industry benchmarks.

---

## 💻 Tech Stack
* **Languages:** Python, T-SQL, DAX
* **Libraries:** `selenium`, `pydantic`, `google-genai`, `pyodbc`, `python-dotenv`
* **AI/ML:** Google Gemini 2.5 Flash API
* **Database:** Microsoft SQL Server (SSMS)
* **Visualization:** Microsoft Power BI

---

## 📂 Project Structure

```text
📦 LLM-ESG-Data-Pipeline
 ┣ 📜 scraper.py         # Selenium web scraping logic
 ┣ 📜 extractor.py       # Gemini API integration and Pydantic validation
 ┣ 📜 loader.py          # SQL Server database connection and insertion
 ┣ 📜 ESG_Pipelines.sql  # T-SQL script for database and table creation
 ┣ 📜 ESG_Dashboard.pbix # Power BI semantic model and executive dashboard
 ┗ 📜 README.md          # Project documentation
```

---
## 🚀 Future Scope
* **PDF Ingestion Engine:** Expand the Selenium scraper to download and parse multi-page PDF sustainability reports using `PyMuPDF` and chunked LLM processing.
* **Pipeline Orchestration:** Implement **Apache Airflow** to schedule and monitor the ETL jobs for automated quarterly runs.
* **Cloud Migration:** Transition the on-premise Microsoft SQL Server warehouse to **Azure SQL Database** for enhanced scalability.
* **Predictive Forecasting:** Integrate Scikit-Learn to model emissions trajectories and forecast estimated "Net Zero" achievement dates per company.
