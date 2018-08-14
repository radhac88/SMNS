SELECT 
    *
FROM
    customers
WHERE
    firstname IN (SELECT 
            firstname
        FROM
            students);

SELECT 
    *
FROM
    students
WHERE
    marks BETWEEN 80 AND 100
ORDER BY marks;

SELECT 
    studentid, CONCAT(stdname, ', ', marks) AS stdmarks
FROM
    students;
    
SELECT 
    *
FROM
    students;

SELECT 
    customers.customerid, students.stdname, customers.country
FROM
    customers
        JOIN
    students ON customers.customerid = students.studentid;/*inner join left join right join,
full join is not working in mysql 
join is used to combine rows from two or more tables, based on a related cloumn btwn them
*/


SELECT 
    lastname AS l, customerid AS c
FROM
    customers,
    employees
WHERE
    customers.customerid = employees.employeeid;

SELECT 
    city
FROM
    customers 
UNION SELECT 
    marks
FROM
    students;/* union will combine the result of two select statements 
no duplicates allowed*/

SELECT 
    city
FROM
    customers 
UNION ALL SELECT 
    marks
FROM
    students;/*no duplicates allowed in union all */

SELECT 
    city, employeeid, firstname
FROM
    employees
WHERE
    city = 'hyd' 
UNION SELECT 
    city, customerid, firstname
FROM
    customers
WHERE
    city = 'hyd';
/*groupby statement is often used for aggregate functions like(count,max,min,sum,avg)*/
SELECT 
    COUNT(city), firstname
FROM
    customers
GROUP BY city
ORDER BY COUNT(city) DESC;

SELECT 
    COUNT(customers.city), employees.city
FROM
    customers
        JOIN
    employees ON customers.city = employees.city
GROUP BY city;/*group by with join */

SELECT 
    SUM(marks) AS totalmarks
FROM
    students;

/*having keyword is use in where to insert aggregate functions */
SELECT 
    customerid, firstname
FROM
    customers
WHERE
    EXISTS( SELECT 
            firstname
        FROM
            employees
        WHERE
            firstname = customers.firstname);
/* any and all operators*/
SELECT 
    *
FROM
    students
WHERE
    marks = ANY (SELECT 
            marks
        FROM
            students
        WHERE
            marks > 0);
/*select into statement*/
SELECT 
    *
INTO customersbackup FROM
    customers;
    /*alternative for into */
create table new_tbl select * from customers;     
/*if null is used to check condition ..if it is null it will replace that null with gaven parameters*/
SELECT 
    studentid, gpa * (IFNULL(marks, 0))
FROM
    students;
/*stored procedures doubt */
/*data base*/
create database testdb;
drop database testdb;
create table temp (tempid int, firstname varchar(30));
drop table temp;
alter table new_tbl 
add cid int;
alter table new_tbl
drop cid;



























