create database codingchallenge1;
use codingchallenge1;

create table Products(
productID int primary key,
productName varchar(30),
categoryID int 
);

insert into Products values
(1,'Table',1),
(2,'Chair',1),
(3,'Lamp',1),
(4,'Mirror',2),
(5,'Wardobe',2);

create table Sales (
saleID int primary key,
productID int,
salesdate date,
quantity int,
amount decimal(10,2),
foreign key (productID) references Products(productID)
);

insert into Sales values
(1,1,'2024-01-20',1,100.00),
(2,2,'2024-01-21',2,200.00),
(3,3,'2024-01-22',4,400.00),
(4,4,'2024-01-23',6,600.00),
(5,5,'2024-01-24',1,100.00);

select * from Products;
select * from Sales;

select
    p.categoryID,
    p.productName,
    s.salesdate,
    s.quantity,
    s.amount,
    SUM(s.amount) OVER (PARTITION BY p.categoryID ORDER BY s.salesdate) AS CategoryTotal,
    SUM(s.amount) OVER () AS GrandTotal
from
    Sales s
join
    Products p on s.productID = p.productID
order by
    p.categoryID, s.salesdate;


