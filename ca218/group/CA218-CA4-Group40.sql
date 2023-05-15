CREATE DATABASE ikea;
USE ikea;

CREATE TABLE Branch (
BranchNo INT(5) PRIMARY KEY,
Ownership ENUM('owned', 'rented') NOT NULL,
BuildingNo INT,
Street VARCHAR(50),
City VARCHAR(50),
Country VARCHAR(75),
Type VARCHAR(50)
);

CREATE TABLE Employee (
EmployeeNo INT(5) PRIMARY KEY,
Position VARCHAR(50),
Salary INT,
BranchNo INT,
firstName VARCHAR(50),
lastName VARCHAR(50),
Sex ENUM('male', 'female', 'other'),
FOREIGN KEY (BranchNo) references Branch(BranchNo)
);

CREATE TABLE Retailers (
RetailerID INT PRIMARY KEY, 
CompanyName VARCHAR(75) NOT NULL
);

INSERT INTO Branch values (1, 'rented', 81, 'Mains Street', 'Dublin', 'Ireland', 'Store'),
(2, 'owned', 71, 'Northgate', 'Bewerly', 'United Kingdom', 'Design'),
(3, 'owned', 2811, 'Parkview Drive', 'Miami', 'United States of America', 'Store');

INSERT INTO Employee values (1, 'Manager', 45000, 1, 'John', 'Apple', 'male'),
(2, 'Manager', 45000, 2, 'Kristian', 'Olson', 'female'),
(3, 'Manager', 45000, 3, 'Daisy', 'Lawrence', 'female'),
(4, 'Supervisor', 30000, 1, 'Greg', 'Johnson', 'male'),
(5, 'Shop Assistant', 25000, 3, 'Jason', 'Fry', 'male'),
(6, 'Designer', 40000, 2, 'Piers', 'Blevins', 'male');

INSERT INTO Retailers values (1, 'Shaily Engineering Plastics Limited'), 
(2, 'Sunny Exports'), 
(3, 'Travancore Mats & Matting Company');