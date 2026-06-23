-- Total Sales
SELECT ROUND(SUM(sales),2) AS total_sales
FROM sales;

-- Total Profit
SELECT ROUND(SUM(profit),2) AS total_profit
FROM sales;

-- Total Customers
SELECT COUNT(DISTINCT customer_id) AS total_customers
FROM sales;

-- Total Orders
SELECT COUNT(DISTINCT order_id) AS total_orders
FROM sales;

-- Sales by Category
SELECT category,
       ROUND(SUM(sales),2) AS revenue
FROM sales
GROUP BY category
ORDER BY revenue DESC;

-- Sales by Region
SELECT region,
       ROUND(SUM(sales),2) AS revenue
FROM sales
GROUP BY region
ORDER BY revenue DESC;

-- Profit by Region
SELECT region,
       ROUND(SUM(profit),2) AS profit
FROM sales
GROUP BY region
ORDER BY profit DESC;

-- Top 10 Customers
SELECT customer_name,
       ROUND(SUM(sales),2) AS revenue
FROM sales
GROUP BY customer_name
ORDER BY revenue DESC
LIMIT 10;

-- Top 10 Products
SELECT product_name,
       ROUND(SUM(sales),2) AS revenue
FROM sales
GROUP BY product_name
ORDER BY revenue DESC
LIMIT 10;

-- Average Discount by Category
SELECT category,
       ROUND(AVG(discount),2) AS avg_discount
FROM sales
GROUP BY category;