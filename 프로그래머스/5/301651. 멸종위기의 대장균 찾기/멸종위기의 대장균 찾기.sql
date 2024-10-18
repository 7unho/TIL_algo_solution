WITH RECURSIVE Generation_CTE AS (
    -- 기저 조건: PARENT_ID가 NULL인 경우 1세대
    SELECT 
        ID, 
        PARENT_ID, 
        1 AS GENERATION
    FROM 
        ECOLI_DATA
    WHERE 
        PARENT_ID IS NULL

    UNION ALL

    -- 재귀 조건: PARENT_ID가 NULL이 아닌 경우 부모의 세대 + 1
    SELECT 
        E.ID, 
        E.PARENT_ID, 
        G.GENERATION + 1
    FROM 
        ECOLI_DATA E
    INNER JOIN 
        Generation_CTE G
    ON 
        E.PARENT_ID = G.ID
)

-- 자식이 없는 개체를 찾고 세대별로 그룹화
SELECT 
    COUNT(G.ID) AS 'COUNT',
    G.GENERATION
FROM 
    Generation_CTE G
LEFT JOIN 
    ECOLI_DATA E 
ON 
    G.ID = E.PARENT_ID
WHERE 
    E.ID IS NULL  -- 자식이 없는 개체만 필터링
GROUP BY 
    G.GENERATION
ORDER BY 
    G.GENERATION;
