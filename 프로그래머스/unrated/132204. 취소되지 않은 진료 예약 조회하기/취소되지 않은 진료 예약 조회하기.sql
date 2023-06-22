-- 2022년 4월 13일 취소되지 않은 CS 진료 내역 조회
-- SELECT APNT_NO, PT_NAME, PT_NO, MCDP_CD, DR_NAME, APNT_YMD
-- ORDER BY APNT_YMD;

WITH `T1` AS (
    SELECT apnt_ymd, apnt_no, pt_no, mddr_id, mcdp_cd
    FROM appointment
    WHERE 
        apnt_ymd like '2022-04-13%' 
        and apnt_cncl_yn = 'N' 
        and mcdp_cd = 'cs'
)

SELECT t1.apnt_no, p.pt_name, t1.pt_no, t1.mcdp_cd, d.dr_name, t1.apnt_ymd
FROM 
    t1, patient p, doctor d
WHERE 
    t1.pt_no = p.pt_no and d.dr_id = t1.mddr_id
ORDER BY t1.apnt_ymd;
