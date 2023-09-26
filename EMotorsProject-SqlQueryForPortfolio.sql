
--- Which year recorded the highest sales?
SELECT Year, SUM(Amount) AS AnnualSale
FROM DimDates dd
JOIN FactSales fs
ON dd.Date_SK = fs.Date_SK
GROUP BY Year
ORDER BY AnnualSale desc

--- Which is the most popular product category?
SELECT COUNT(Product_Category)AS PopularProduct, Product_Category
FROM DimProducts
GROUP BY Product_Category
ORDER BY PopularProduct desc

--- What proportion of the customers are new?

SELECT COUNT(Customer_Category) AS NewCustomers, Year
FROM DimCustomers dc
JOIN FactSales fs
ON dc.Customer_SK = fs.Customer_SK
JOIN DimDates dd
ON dd.Date_SK = fs.Date_SK
WHERE Customer_Category = 'New_Customer'
GROUP BY Year
ORDER BY NewCustomers desc

---- What proportion of the customers are returning?

SELECT COUNT(Customer_Category) AS ReturningCustomers, Year
FROM DimCustomers dc
JOIN FactSales fs
ON dc.Customer_SK = fs.Customer_SK
JOIN DimDates dd
ON dd.Date_SK = fs.Date_SK
WHERE Customer_Category = 'Returning'
GROUP BY Year
ORDER BY ReturningCustomers desc


--- What is the total number of customers between November 2018 to June 2023 in their different categories?

SELECT COUNT(Customer_ID) AS TotalCustomerCount, Customer_Category
FROM DimCustomers
GROUP BY Customer_Category