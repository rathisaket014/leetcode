# Write your MySQL query statement below
select e.name
from Employee as e inner join Employee as e1 on e.id = e1.managerId
group by e1.managerId
having count(e1.managerId) >= 5;