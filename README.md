Sales Analytics Dashboard (End-to-End Data Analysis Project)
Project Highlights
End-to-end data analytics pipeline using Python, SQL, and Tableau
9,994 real-world retail transactions analyzed
Built KPI dashboards for executive-level decision making
Identified top-performing products, customers, and regions
Applied SQL-based business intelligence queries
Created data visualizations for actionable insights
Project Overview

This project is an end-to-end sales analytics solution built using Python, MySQL, SQL, and Tableau to analyze retail transaction data from the Sample Superstore dataset.

The objective is to transform raw sales data into meaningful business insights that support decision-making in areas such as sales performance, customer segmentation, product profitability, and regional trends.

The project follows a complete data analytics workflow: data cleaning, database storage, SQL analysis, visualization, and insight generation.

Business Problem

Retail companies generate large volumes of transactional data but often struggle to extract actionable insights.

This project answers the following questions:

What drives overall sales performance?
Which regions are underperforming or overperforming?
Who are the most valuable customers?
Which products are most and least profitable?
How do different product categories contribute to revenue?
Tech Stack
Python (Pandas, Matplotlib, Seaborn) for data cleaning and visualization
MySQL for data storage and querying
SQL for business analysis
Tableau for dashboard visualization
Git and GitHub for version control
Dataset
Sample Superstore Dataset
9,994 rows
21 columns
Contains order details, customer information, product categories, sales, profit, and discount data
Project Workflow
Data Cleaning (Python)
Removed duplicates
Verified missing values (none found)
Standardized dataset structure
Ensured correct data types
Data Storage (MySQL)
Imported cleaned dataset into MySQL database
Structured table for efficient querying
Enabled SQL-based analysis
SQL Analysis

Key insights extracted:

Total sales and profit
Region-wise performance comparison
Category-wise revenue contribution
Top customers by revenue
Top-performing products
Data Visualization (Python)

Created visual insights including:

Sales by category
Sales by region
Profit by region
Top customers analysis
Top products analysis
Key Insights
Technology category generates the highest revenue
West region is the strongest performing region
A small group of customers contributes a large portion of revenue
Furniture category shows lower profit margins compared to others
High-value office equipment dominates top product sales
Visualizations

All visualizations are included in the screenshots folder:

Sales by Category
Sales by Region
Profit by Region
Top Customers
Top Products
Skills Demonstrated
Data cleaning and preprocessing
Exploratory data analysis
SQL querying and aggregation
Data visualization
Business intelligence thinking
Dashboard design
End-to-end analytics pipeline development
Project Structure

Sales-Analytics-Dashboard/
│
├── data/
│ └── Sample-Superstore.csv
│
├── python/
│ ├── ExploreData.py
│ ├── visualizations.py
│
├── sql/
│ └── analysis_queries.sql
│
├── tableau/
│ └── Sales_Dashboard.twb
│
├── screenshots/
│ ├── dashboard_overview.png
│ ├── sales_by_category.png
│ ├── sales_by_region.png
│ ├── profit_by_region.png
│ └── top_customers.png
│
└── README.md

How to Run This Project
Clone the repository
Install dependencies using pip install -r requirements.txt
Run Python scripts in the python folder
Import dataset into MySQL and execute SQL queries
Open Tableau dashboard from the tableau folder
Business Impact

This project helps businesses:

Improve sales strategy
Identify high-value customers
Optimize regional performance
Reduce low-profit product lines
Make data-driven decisions
Future Improvements
Integration with advanced Tableau dashboards or Power BI
Predictive sales forecasting using machine learning
Automated reporting system
Real-time analytics dashboard
Author

Dev Kumar
Aspiring Data Analyst
Skills: Python, SQL, Tableau, Data Visualization, MySQL

If you like this project

Feel free to star the repository and connect.
