# SELECT FISH_INFO.ID, FISH_NAME_INFO.FISH_NAME, FISH_INFO.LENGTH

select id, fish_name, b.length
from fish_info i, (

select i.fish_type, fish_name, length
from fish_name_info i,
(
select fish_type, max(length) as 'LENGTH'
from fish_info
group by fish_type) g
where i.fish_type = g.fish_type) b
where i.fish_type = b.fish_type
and i.length = b.length
order by id;