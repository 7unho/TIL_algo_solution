-- 2022년 3월에 판매된 데이터 조회
-- 오프라인 데이터의 USER_ID -> NULL 처리
-- SELECT SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
-- ORDER BY SALES_DATE, PRODUCT_ID, USER_ID;

(
    SELECT 
        date_format(sales_date, '%Y-%m-%d') 'sales_date', 
        product_id, 
        user_id, 
        sales_amount 
    FROM 
        online_sale 
    WHERE sales_date like '2022-03%'
)
UNION
(
    SELECT 
        date_format(sales_date, '%Y-%m-%d') 'sales_date',   
        product_id, 
        NULL 'user_id', 
        sales_amount from offline_sale where sales_date like '2022-03%'
)
ORDER BY sales_date, product_id, user_id;