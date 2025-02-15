# Write your MySQL query statement below
select coalesce (
    (select num
    from MyNumbers
    group by num
    having count(num) = 1
    order by num DESC
    limit 1), null
) as num;