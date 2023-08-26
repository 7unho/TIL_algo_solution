import java.util.*;
/*
    user_id: 응모자 아이디 배열,
    banned_id: 제재 아이디 배열,
    [HashSet] answer.size(): 경우의 수
    
    1. user_id에서 banned_id.length만큼 순열 배열 생성 후, 아이디 체크
    2. 아이디 체크 메서드(String id, String banned_id); return boolean
    3. 유효하다면 answer에 추가.
    
*/

class Solution {
    static int N, C;
    public int solution(String[] user_id, String[] banned_id) {
        Set<Set<String>> answer = new HashSet<>();
        List<List<String>> ids = new ArrayList<>();
        N = user_id.length;
        C = banned_id.length;
        
        perm(0, user_id, new ArrayList<>(), ids, new boolean[N]);
        
        for(List<String> id: ids){
            if(isValid(id, banned_id)) answer.add(new HashSet<>(id));
        }
        
        return answer.size();
    }
    
    public boolean isValid(List<String> id, String[] banned_id){
        for(int i = 0; i < id.size(); i++){
            if(!areIdsEqual(id.get(i), banned_id[i])) return false;
        }
        return true;
    }
    
    public boolean areIdsEqual(String userId, String referenceId) {
        if(userId.length() != referenceId.length()) return false;
        for(int i = 0; i < userId.length(); i++){
            if(referenceId.charAt(i) == '*') continue;
            if(referenceId.charAt(i) != userId.charAt(i)) return false;
        }
        return true;
    }
    
    public void perm(int depth, String[] user_id, List<String> id, List<List<String>> ids, boolean[] isSelected){
        if(depth == C){
            ids.add(new ArrayList<>(id));
            return;
        }
        
        for(int i = 0; i < N; i++){
            if(isSelected[i]) continue;
            
            isSelected[i] = true;
            id.add(user_id[i]);
            perm(depth + 1, user_id, id, ids, isSelected);
            id.remove(id.size() - 1);
            isSelected[i] = false;
        }
    }
}