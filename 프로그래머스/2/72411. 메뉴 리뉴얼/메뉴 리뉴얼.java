import java.util.*;
/*
    각 메뉴별로 조합 -> 비트마스킹
    
    answer: map의 키 값이 2이상인 것들 정렬 후 출력
    
    1. orders를 탐색하며 키 추출(단일 메뉴)
    2. 각 키값에 대응되는 비트마스킹용 배열(keys) 생성
    3. 키 조합 생성 후, 카운트 누산
    
    
*/
class Solution {
    static boolean[] isSelected;
    static Map<String, Integer> menus;
    public String[] solution(String[] orders, int[] course) {
        List<String> answer = new ArrayList<>();
        // 1. course 개수 만큼 메뉴 조합 생성
        for(int c: course){
            menus = new HashMap<>();
            for(String order: orders){
                if(c > order.length()) continue;
                
                char[] menu = order.toCharArray();
                Arrays.sort(menu);
                isSelected = new boolean[menu.length];
                combi(0, c, 0, menu);
            }
            
            for(String key: menus.keySet()){
                if(Collections.max(menus.values()) == menus.get(key) && menus.get(key) >= 2) answer.add(key);
            }
        }
        
        Collections.sort(answer);
        return answer.toArray(new String[answer.size()]);
    }
    
    static void combi(int depth, int c, int start, char[] menu){
        if(depth >= c){
            String key = "";
            for(int i = 0; i < menu.length; i++) {
                if(!isSelected[i]) continue;
                key += menu[i];
            }
            menus.compute(key, (k, v) -> ((v == null) ? 1: v + 1));
            return;
        }

        for(int i = start; i < menu.length; i++){
            if(isSelected[i]) continue;
            isSelected[i] = true;
            combi(depth + 1, c, i + 1, menu);
            isSelected[i] = false;
        }
    }
}