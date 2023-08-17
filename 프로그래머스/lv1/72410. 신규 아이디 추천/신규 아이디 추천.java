class Solution {
    public String step1(String id){
        // 1. new_id의 모든 대문자를 소문자로 치환
        StringBuilder res = new StringBuilder();
        for(char c: id.toCharArray()){
            if(Character.isUpperCase(c)) c = Character.toLowerCase(c);
            res.append(c);
        }
        return res.toString();
    }
    
    public String step2(String id){
        // 2. 소문자, 숫자, -, _, . 이외의 문자 제거
        StringBuilder res = new StringBuilder();
        
        for(char c: id.toCharArray()){
            try {
                res.append(Integer.parseInt(Character.toString(c)));
            } catch(NumberFormatException e){
                if(Character.isLowerCase(c) || c == '-' || c == '_' || c == '.') {
                    res.append(c);
                    continue;
                }
                res.append("");
            }
        }
        
        return res.toString();
    }
    
    public String step3(String id){
        // 3. 마침표가 2번 이상 연속된 부분을 하나의 마침표로 치환
        return id.replaceAll("\\.+", ".");
    }
    
    public String step4(String id){
        StringBuilder res = new StringBuilder();
        // 4. 마침표가 처음이나 끝에 있다면 제거
        for(int i = 0; i < id.length(); i++){
            if((i == 0 || i == id.length() - 1) && id.charAt(i) == '.') {
                res.append("");
                continue;
            }
            res.append(id.charAt(i));
        }
        
        return res.toString();
    }
    
    public String step5(String id){
        // 5. id가 빈 문자열이라면, a를 대입
        return id.isEmpty() ? "a" : id;
    }
    
    public String step6(String id){
        // 6. id의 길이가 16자 이상이면 -> 첫 15개를 제외한 나머지 문자 제거
        //                            제거 후, 마침표가 끝에 위치한다면 끝에 위치한 마침표도 제거
        if(id.length() >= 16) {
            id = id.substring(0, 15);
            
            if(id.charAt(14) == '.') id = id.substring(0, 14);
        }
        
        return id;
    }
    
    public String step7(String id){
        // 7. id의 길이가 2자 이하라면, id의 마지막 문자를 길이가 3이 될 때 까지 문자열 끝에 삽입.
        int len = id.length();
        StringBuilder res = new StringBuilder(id);
        if(len <= 2){
            for(int i = 0; i < 3 - len; i++){
                res.append(id.charAt(len - 1));
            }
        }
        return res.toString();
    }
    public String solution(String new_id) {
        new_id = step1(new_id);
        new_id = step2(new_id);
        new_id = step3(new_id);
        new_id = step4(new_id);
        new_id = step5(new_id);
        new_id = step6(new_id);
        new_id = step7(new_id);
        return new_id;
    }
}