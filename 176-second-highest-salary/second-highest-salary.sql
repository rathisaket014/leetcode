-- select coalesce(
--     (
--         select distinct salary
--         from Employee
--         order by salary desc
--         limit 1 offset 1
--     ),
--     null
-- ) as SecondHighestSalary;

select max(salary) as SecondHighestSalary
from Employee
where salary < (
    select max(salary) from employee
);