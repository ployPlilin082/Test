SELECT c.ID AS CustomerID, c.Name, o.ID AS OrderID, o.Amount 
FROM Customer c
INNER JOIN Order o ON c.ID = o.CustomerID;
