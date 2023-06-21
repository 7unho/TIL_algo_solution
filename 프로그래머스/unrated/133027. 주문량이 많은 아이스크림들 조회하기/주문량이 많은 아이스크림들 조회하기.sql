-- 7월 총 주문량 + 상반기 아이스크림 상위 3개의 맛
-- SELECT FLAVOR
-- ORDER BY 총 주문량 desc
SELECT flavor
FROM
(    SELECT j.shipment_id, j.flavor, sum((j.total_order + ifnull(f.total_order, 0))) 'total_count'
    FROM
        july j left outer join
        first_half f on f.shipment_id = j.shipment_id
    group by j.flavor
    order by total_count desc limit 3) `solution`; # 초코, 딸기, 화이트초코
    

