import java.util.*;
import java.util.stream.Collector;

public class Test {
    public static void main(String[] args) {
        Set<Set<String>> stringSetsSet = new HashSet<>();

        // 예시 문자열 요소들
        String[] array1 = {"apple", "banana", "orange"};
        String[] array2 = {"banana", "orange", "apple"};
        String[] array3 = {"grape", "pear", "kiwi"};
        String[] array4 = {"orange", "apple", "banana"};
        // 문자열 배열을 Set<String>으로 변환하여 중복 없이 추가
        stringSetsSet.add(new HashSet<>(Arrays.asList(array1)));
        stringSetsSet.add(new HashSet<>(Arrays.asList(array2)));
        stringSetsSet.add(new HashSet<>(Arrays.asList(array3)));
        stringSetsSet.add(new HashSet<>(Arrays.asList(array4)));
        List<String> test = new ArrayList<>();
        test.add("te");
        test.add("st");
        System.out.println(test.toString());

        System.out.println(stringSetsSet.size()); // 중복 요소 조합 제거 후의 개수 출력
    }
}
