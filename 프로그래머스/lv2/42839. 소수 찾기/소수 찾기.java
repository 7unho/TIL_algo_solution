// (number, numbers) -> number로 시작해서 numbers로 만들 수 있는 숫자 중 소수의 집합
import java.util.*;
import java.util.stream.*;
class Solution {
    public int solution(String nums) {
        List<Integer> numbers = nums.chars().map(c -> c - '0').boxed().collect(Collectors.toList());
        return getPrimes(0, numbers).size();
    }
    
    public boolean isPrime(int number){
        if(number < 2) return false;
        if(number == 2 || number == 3) return true;
        for(int i = 2; i < Math.sqrt(number) + 1; i++){
            if(number % i == 0) return false;
        }
        return true;
    }
    
    public Set<Integer> getPrimes(int number, List<Integer> numbers){
        Set<Integer> primes = new HashSet<>();
        if(isPrime(number)) primes.add(number);
            
        
        for(int i = 0; i < numbers.size(); i++){
            int next = number * 10 + numbers.get(i);
            List<Integer> nextNumbers = new ArrayList<>(numbers);
            
            nextNumbers.remove(i);
            primes.addAll(getPrimes(next, nextNumbers));
        }
        return primes;
    }
}