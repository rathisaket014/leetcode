# Write your MySQL query statement below
with RankedEmps as (
    select 
        d.name as Department,
        e.name as Employee,
        e.salary as Salary,
        RANK() OVER(partition by d.name order by e.salary DESC) as rnk
    from Employee e
    join Department d on e.departmentId = d.id
)

select 
    Department,
    Employee,
    Salary
from RankedEmps
where rnk = 1;