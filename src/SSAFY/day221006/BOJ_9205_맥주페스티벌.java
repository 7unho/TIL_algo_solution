import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_9205_맥주페스티벌 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N;
        Point start;
        Point target;
        Point[] conv;
        Queue<Point> queue;
        boolean[] visited;

        int TC = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= TC; tc++) {
            queue = new LinkedList<>();
            N = Integer.parseInt(br.readLine());
            conv = new Point[N];
            visited = new boolean[N];
            String answer = "sad";

            st = new StringTokenizer(br.readLine());
            start = new Point(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                conv[i] = new Point(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
            }

            st = new StringTokenizer(br.readLine());
            target = new Point(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));

            queue.offer(start);

            while(!queue.isEmpty()){
                Point current = queue.poll();

                if(Math.abs(current.x - target.x) + Math.abs(current.y - target.y) <= 1000){
                    answer = "happy";
                    break;
                }

                for (int i = 0; i < N; i++) {
                    Point nPoint = conv[i];
                    int dist = Math.abs(nPoint.x - current.x) + Math.abs(nPoint.y - current.y);
                    if(!visited[i] && dist <= 1000){
                        visited[i] = true;
                        queue.offer(nPoint);
                    }
                }
            }

            System.out.println(answer);
        }
    }

    static class Point{
        int x;
        int y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
