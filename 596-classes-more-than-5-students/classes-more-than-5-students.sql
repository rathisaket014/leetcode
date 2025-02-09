/* Write your PL/SQL query statement below */
select class
from Courses
having count (student) >= 5
group by class;