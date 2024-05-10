
-- 1) Fetch all the paintings which are not displayed on any museums?
select * from work w where w.museum_id is null


-- 2) Are there museuems without any paintings?
select * from museum m where 
 exists(select 1 from work where work.museum_id=m.museum_id)

or 

select museum.name,count(work.name) from museum join work on museum.museum_id=work.museum_id
group by museum.name 
having count(work.name)>1

-- Output there is no museums without having any pantings

-- 3) How many paintings have an asking price of more than their regular price? 
select * from work w join product_size ps on w.work_id=ps.work_id
where sale_price > regular_price
-- Output there is no paintings with having more aking price than regular price.


-- 4) Identify the paintings whose asking price is less than 50% of its regular price

select w.name,sale_price,regular_price from work w join product_size ps on w.work_id=ps.work_id 
where sale_price < regular_price/2

5) Which canva size costs the most?
--This is will work only when there will be no exact sale_price multile times
select * from canvas_size cs join 
product_size ps on cs.size_id = ps.size_id::float
order by sale_price desc
limit 1
(or)
--  This will work because ranking it according to the sale price eventhough there is same sale_price it will give all records.
with t as (select *,rank() over(order by sale_price desc) as sal_rank 
from canvas_size cs join 
product_size ps on cs.size_id = ps.size_id::float
order by sale_price desc ) 
select * from t where t.sal_rank=1

