# # -- 2022년 1월, 저자 별, 카테고리 별 매출액을 구해라
# # -- order by 저자, category desc;
# # -- AUTHOR_ID, AUTHOR_NAME, CATEGORY, TOTAL_SALES


SELECT A.AUTHOR_ID, A.AUTHOR_NAME, SALES.CATEGORY, SUM(TOTAL_SALES) 'TOTAL_SALES'
FROM author a,
(SELECT B.AUTHOR_ID, B.CATEGORY, (B.PRICE * S.SALES) 'TOTAL_SALES'
FROM
    book b,
    book_sales s
WHERE b.book_id = s.book_id
and s.sales_date like '2022-01%') sales 
where a.author_id = sales.author_id
group by a.author_id, a.author_name, sales.category
order by a.author_id, sales.category desc