# score = 리뷰 평균 점수, 셋째 자리 반올림
# 평균점수 내림, 즐겨찾기 내림
SELECT ri.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, round(avg(REVIEW_SCORE), 2) as 'SCORE'
FROM REST_INFO ri, REST_REVIEW rr
WHERE ri.REST_ID in (
    SELECT REST_ID
    FROM REST_INFO
    WHERE ADDRESS like '서울%'
) AND ri.REST_ID = rr.REST_ID
GROUP BY ri.REST_ID
ORDER BY round(avg(REVIEW_SCORE), 2) desc, FAVORITES desc;