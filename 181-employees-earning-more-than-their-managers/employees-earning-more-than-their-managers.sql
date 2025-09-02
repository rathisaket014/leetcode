# Write your MySQL query statement below
select e.name as Employee
from Employee e
join Employee m # self join
on e.managerId = m.id
where e.salary > m.salary