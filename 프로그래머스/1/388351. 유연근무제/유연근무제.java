/**
n := 직원 수
schedules := 출근 희망 시각
timelogs := 일주일 실 출근 시각, hour * 100 + minute
startday := 시작 요일 1(월) ~ 7(일)


*/
import java.time.*;

class Solution {
    public int solution(int[] schedules, int[][] timelogs, int startday) {
        int answer = 0;
        int N = schedules.length;
        
        for (int crew = 0; crew < N; crew++) {
            if (isSuccess(schedules[crew], timelogs[crew], startday, crew)) {
                answer += 1;
            }
        }
        return answer;
    }
    
    public boolean isSuccess(int schedule, int[] timelogs, int startday, int crew) {
        for (int day = 0; day < 7; day++) {
            if (isIgnored(startday, day + 1)) continue;
            if (isFailed(schedule, timelogs[day])) return false;
        }
        return true;
    }
    
    public boolean isIgnored(int startday, int day) {
        if (startday == 7) {
            return day == 1 || day == 7;
        }
        return 8 - startday == day || 7 -  startday == day;
    }
    
    public boolean isFailed(int schedule, int timelog) {
        LocalTime parsedSchedule = LocalTime.of(schedule / 100, schedule % 100).plusMinutes(10);
        LocalTime parsedTimelog = LocalTime.of(timelog / 100, timelog % 100);
        
        return parsedTimelog.isAfter(parsedSchedule);
    }
}