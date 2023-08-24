import java.util.*;

class Solution {
    static char[] INDEX = {'A', 'E', 'I', 'O', 'U'};
    public int solution(String word) {
        List<String> words = new ArrayList<>();
        getWordIndex("", words);
        return words.indexOf(word);
    }
    
    public void getWordIndex(String word, List<String> words){
        words.add(word);
        
        if(word.length() == 5) return;
        
        for(char i: INDEX) getWordIndex(word + i, words);
    }
}