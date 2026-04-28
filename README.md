# 📊 Retail Sales Analytics Pipeline

## 🚀 Overview

This project presents an end-to-end data analytics pipeline built using Python to process, analyze, and extract business insights from retail sales data. It includes modular data cleaning, KPI computation, and visualization to support data-driven decision-making.

---

## 🧠 Key Features

* 🔹 Modular **Data Cleaning Pipeline** using OOP (`DataCleaner`)
* 🔹 Config-driven workflow using `.env`
* 🔹 Efficient data storage using **Parquet (PyArrow)**
* 🔹 Reusable **KPI computation framework** (`KPIAnalyzer`)
* 🔹 Exploratory Data Analysis & visual storytelling
* 🔹 Clean, production-style project structure

---

## 🛠️ Tech Stack

* Python (Pandas, NumPy)
* Matplotlib / Seaborn
* Jupyter Notebook
* Parquet (PyArrow)
* Git & GitHub

---

## 📂 Project Structure

```
retail_sales_dashboard/
│
├── data/                  # Raw & cleaned datasets
├── notebooks/             # Analysis notebooks
├── src/
│   ├── __init__.py
│   ├── data_cleaner.py    # Data preprocessing pipeline
│   ├── kpi_analyzer.py    # KPI computation module
│
├── .env                   # Environment variables (ignored)
├── .gitignore
├── README.md
```

---

## ⚙️ Data Pipeline

```
Raw Data → DataCleaner → Clean Data (Parquet) → KPIAnalyzer → Insights
```

---

## 📊 Key Performance Indicators (KPIs)

* **Total Sales:** ~$2.30M
* **Total Profit:** ~$286K
* **Profit Margin:** ~12.47%
* **Total Orders:** 5009
* **Average Order Value:** ~$458
* **Sales Growth:**

  * 2015: -2.83%
  * 2016: +29.47%
  * 2017: +20.36%

---

## 📈 Key Insights

* **Technology** is the top-performing category in both sales and profit.
* **Furniture** generates moderate revenue but significantly lower profit, indicating inefficiencies.
* Sales experienced a dip in 2015 followed by strong and consistent growth through 2017.
* **Office Supplies** shows steady growth and strong profitability potential.
* Growth trends indicate shifting demand toward higher-margin categories.

---

## 📊 Analysis Highlights

* Sales trends over time
* Category-wise revenue and profit comparison
* Profit vs Sales relationship
* Growth trends across categories
* KPI breakdown and segmentation

---

## 🔐 Configuration

Project uses `.env` for flexible path management.

Example:

```
DATA_PATH=data/Superstore.csv
CLEAN_DATA_PATH=data/cleaned_superstore.parquet
```

---

## 🧹 Data Processing Highlights

* Removed duplicates and handled missing values
* Standardized column formats and data types
* Converted date fields and extracted time features
* Built reusable preprocessing methods

---

## 🚀 How to Run

1. Clone the repository:

```
git clone https://github.com/your-username/retail_sales_dashboard.git
```

2. Navigate into the project:

```
cd retail_sales_dashboard
```

3. Create and activate virtual environment:

```
python -m venv venv
venv\Scripts\activate
```

4. Install dependencies:

```
pip install -r requirements.txt
```

5. Run the notebook:

```
jupyter notebook
```

---

## 💡 Future Improvements

* Interactive dashboard using Power BI or Streamlit
* Automated data pipeline execution
* Advanced forecasting models
* Deployment as a web application

---

## 🏆 Project Highlights

* End-to-end analytics pipeline
* Strong focus on modular design and reusability
* Business-oriented insights and KPI reporting
* Clean and professional project structure

---

## 👤 Author

**Pranith Devu**
Master’s in Computer Science
Aspiring Data Scientist / Data Analyst

---

## ⭐ Final Note

This project demonstrates the ability to:

* Build scalable data pipelines
* Perform structured data analysis
* Translate data into actionable business insights

---
