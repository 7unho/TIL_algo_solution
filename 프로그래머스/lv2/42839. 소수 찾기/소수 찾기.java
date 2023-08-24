// (number, numbers) -> number로 시작해서 numbers로 만들 수 있는 숫자 중 소수의 집합
import java.util.*;
import java.util.stream.*;
class Solution {
    static int N;
    public int solution(String nums) {
        Set<Integer> primes = new HashSet<>();
        int[] numbers = nums.chars().map(c -> c - '0').toArray();
        N = numbers.length;
        getPrimes(0, numbers, new boolean[N], primes);
        return primes.size();
    }
    
    public boolean isPrime(int number){
        if(number < 2) return false;
        if(number == 2 || number == 3) return true;
        for(int i = 2; i < Math.sqrt(number) + 1; i++){
            if(number % i == 0) return false;
        }
        return true;
    }
    
    public void getPrimes(int number, int[] numbers, boolean[] isSelected, Set<Integer> primes){
        if(isPrime(number)) primes.add(number);
        
        for(int i = 0; i < N; i++){
            if(isSelected[i]) continue;
            int next = number * 10 + numbers[i];
            
            isSelected[i] = true;
            getPrimes(next, numbers, isSelected, primes);
            isSelected[i] = false;
        }
    }
}