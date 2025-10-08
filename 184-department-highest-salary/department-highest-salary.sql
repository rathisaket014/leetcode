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


-- WITH RankedEmployees AS (...): We use a Common Table Expression (CTE) to create a temporary result set. This makes the query easier to read.

-- RANK() OVER (...): This is the window function that does the magic.

-- PARTITION BY d.name: This is the crucial part. It tells the function to split the employees into separate groups for each department ('Sales', 'Engineering', etc.).

-- ORDER BY e.salary DESC: Within each of those department groups, it ranks the employees by their salary from highest to lowest.

-- as rnk: We name the resulting rank column rnk.

-- SELECT ... WHERE rnk = 1: Finally, we query our temporary RankedEmployees table and select only the rows where the rank is 1, which corresponds to the highest-paid employee(s) in each department.