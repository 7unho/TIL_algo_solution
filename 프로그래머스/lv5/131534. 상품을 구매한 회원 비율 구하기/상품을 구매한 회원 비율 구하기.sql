# -- 2021년 가입한 회원 중, (2021년에 가입한 회원 중 상품을 구매한 회원 수) / 2021년에 가입한 전체 회원수 )를 구해라
# -- SELECT YEAR, MONTH, PUCHASED_USERS(상품 구매한 회원 수), PUCHASED_RATIO(비율) // 비율은 소수점 둘 쨰 자리에서 반올림
# -- ORDER BY YEAR, MONTH;

SET @2021_TOTAL_USER_COUNT := (
    SELECT count(*)
    FROM user_info
    WHERE year(joined) = '2021'
);

SELECT 
    year(sales_date) 'YEAR', 
    month(sales_date) 'MONTH', 
    count(distinct s.user_id) 'PURCHASED_USERS', 
    round(count(distinct s.user_id) / @2021_TOTAL_USER_COUNT, 1) 'PUCHASED_RATIO'
FROM 
    online_sale s, user_info u
WHERE
    s.user_id = u.user_id
    and year(joined) = '2021'
GROUP BY year(sales_date), month(sales_date)
ORDER BY YEAR, MONTH;