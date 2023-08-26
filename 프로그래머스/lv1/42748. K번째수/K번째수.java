import java.util.*;
import java.util.stream.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        int idx = 0;
        for(int[] cmd: commands) answer[idx++] = find(array, cmd);
        return answer;
    }
    
    public int find(int[] array, int[] cmd){
        return IntStream.rangeClosed(cmd[0] - 1, cmd[1] - 1).map(i -> array[i]).sorted().toArray()[cmd[2] - 1];
    }
}