-- 7월 총 주문량 + 상반기 아이스크림 상위 3개의 맛
-- SELECT FLAVOR
-- ORDER BY 총 주문량 desc
SELECT FLAVOR
FROM
(    
    SELECT j.shipment_id, j.flavor, sum((j.total_order + ifnull(f.total_order, 0))) 'total_count'
    FROM
        july j LEFT OUTER JOIN first_half f ON f.shipment_id = j.shipment_id
    GROUP BY j.flavor
    ORDER BY total_count DESC LIMIT 3
) `solution`;
    
