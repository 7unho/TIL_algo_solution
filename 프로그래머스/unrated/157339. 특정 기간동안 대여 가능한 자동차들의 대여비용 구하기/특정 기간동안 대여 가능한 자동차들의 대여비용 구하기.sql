# CAR_TYPE이 'SUV', '세단' 중, 2022-11-01 ~ 2022-11-30간 대여가 가능하고, 대여 금액이 50 <= x < 200 인 자동차
-- SELECT CAR_ID, CAR_TYPE, FEE
-- ORDER BY FEE desc, CAR_TYPE, CAR_ID desc


SELECT 
        c.CAR_ID,
        c.CAR_TYPE,
        daily_fee * 30 * (100 - discount_rate) div 100 'FEE'
FROM 
    CAR_RENTAL_COMPANY_CAR c,
    CAR_RENTAL_COMPANY_DISCOUNT_PLAN p
WHERE 
    c.car_type = p.car_type
and c.CAR_TYPE in ('SUV', '세단')
and duration_type = '30일 이상'
and CAR_ID not in (
    SELECT car_id 
    FROM car_rental_company_rental_history 
    WHERE not (start_date > '2022-11-30' or end_date < '2022-11-01')
)
HAVING fee >= 500000 and fee < 2000000
ORDER BY fee desc, c.CAR_TYPE asc, c.CAR_ID desc