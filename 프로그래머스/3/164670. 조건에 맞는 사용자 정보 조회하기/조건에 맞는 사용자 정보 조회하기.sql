SELECT 
        USER_ID, 
        NICKNAME, 
        concat(CITY, ' ', STREET_ADDRESS1, ' ', STREET_ADDRESS2) as '전체주소', 
        concat(substr(TLNO, 1, 3), '-', substr(TLNO, 4, 4), '-', substr(TLNO, 8, 4)) as '전화번호'
FROM USED_GOODS_USER
WHERE USER_ID in (
    SELECT WRITER_ID
    FROM USED_GOODS_BOARD
    GROUP BY WRITER_ID
    HAVING count(*) >= 3
)
ORDER BY USER_ID desc;