-- SELECT HISTORY_ID, FEE
-- ORDER BY FEE desc, HISTORY_ID desc;

WITH HISTORY_WITH_CAR_INFO AS
(
    SELECT
        history_id,
        c.car_id,
        c.car_type,
        c.daily_fee,
        datediff(end_date, start_date) + 1 'period',
        CASE
            WHEN datediff(end_date, start_date) + 1 < 7
            THEN NULL
            WHEN datediff(end_date, start_date) + 1 < 30
            THEN '7일 이상'
            WHEN datediff(end_date, start_date) + 1 < 90
            THEN '30일 이상'
            ELSE '90일 이상'
        END 'duration_type'
    FROM
        CAR_RENTAL_COMPANY_CAR c,
        CAR_RENTAL_COMPANY_RENTAL_HISTORY h
    WHERE
        c.car_id = h.car_id
        and car_type = '트럭'
)

SELECT
    history_id,
    (daily_fee * ( 100 - ifnull(discount_rate, 0)) div 100 ) * period 'FEE'
FROM
    HISTORY_WITH_CAR_INFO T1 LEFT OUTER JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN T2 
    ON T1.car_type = T2.car_type and T1.duration_type = T2.duration_type
ORDER BY fee desc, history_id desc;
