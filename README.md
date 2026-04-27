# 🌍 Global Development & Socio-Economic Risk Segmentation Analysis

## 📌 Project Overview

This project analyzes global country-level socio-economic indicators to identify development patterns, classify countries into meaningful segments, and support data-driven international aid allocation.

Using Python, SQL, and Streamlit, the project explores relationships between income, GDP, child mortality, health expenditure, inflation, fertility, and life expectancy to uncover socio-economic risks and prioritize vulnerable nations.

---

## 🎯 Problem Statement

International development organizations need a strategic way to allocate financial aid based on socio-economic conditions. This project helps by:

* Identifying high-risk and underdeveloped countries
* Segmenting countries into development categories
* Understanding economic and health relationships
* Supporting international aid prioritization

---

## 🛠️ Tech Stack

**Programming & Analysis:** Python, Pandas, NumPy

**Database:** SQL (MySQL)

**Visualization:** Plotly, Streamlit

**Concepts:** Data Cleaning, EDA, Feature Engineering, KPI Dashboard, Country Segmentation

---

## 📂 Dataset Features

Key indicators used in this project are country wise:

* Child Mortality (`child_mort`)
* Exports (`exports`)
* Health Expenditure (`health`)
* Imports (`imports`)
* Income (`income`)
* Inflation (`inflation`)
* Life Expectancy (`life_expec`)
* Fertility Rate (`total_fer`)
* GDP Per Capita (`gdpp`)

---

## ⚙️ Project Workflow

### 1️⃣ Data Cleaning & Preprocessing

* Missing value handling
* Duplicate removal
* Outlier treatment
* Inflation anomaly correction
* Derived metrics creation:

  * Development Index
  * Trade Balance
  * Health Impact Ratio

### 2️⃣ Exploratory Data Analysis

* Income distribution
* Child mortality trends
* GDP vs Fertility
* Health vs Mortality
* Correlation heatmap

### 3️⃣ Rule-Based Segmentation

Countries are classified into:

* High Risk Country
* Developed Nation
* Emerging Economy
* High Inflation Risk
* Health Critical
* Low GDP Trap

### 4️⃣ SQL Analytics

* Average income by segment
* Top high-risk countries
* Inflation analysis
* GDP comparison
* Segment KPIs

### 5️⃣ Interactive Streamlit Dashboard

### Page 1: Global Overview

* KPI Cards
* World Map by Segment
* Income vs Life Expectancy

### Page 2: Health & Economic Risk

* Child Mortality by Country
* Health vs Mortality
* Inflation Risk
* Fertility vs GDP

### Page 3: Segmentation Insights

* Segment Distribution
* Income by Segment
* GDP by Segment

---

## 📈 Key Insights

* Higher income strongly correlates with better life expectancy
* Increased health spending often reduces child mortality
* High fertility rates are common in low-GDP countries
* Inflation instability can significantly affect economic development
* High-risk nations require prioritized aid intervention

---

## 🚀 Business Recommendations

* Prioritize aid for countries with low income + high mortality
* Increase healthcare investment in vulnerable nations
* Support inflation stabilization programs
* Promote women’s education in high fertility countries
* Encourage trade reforms for emerging economies

---

## ▶️ How to Run the Project

### Install Dependencies

```bash
pip install pandas numpy plotly streamlit mysql-connector-python
```

### Run Streamlit Dashboard

```bash
streamlit run app.py
```

---

## 👩‍💻 Developed By

**Madhavi Pathipaka**

## 📚 Skills Demonstrated

Python | SQL | Streamlit | Pandas | Plotly | Data Analysis | EDA | Dashboard Development
