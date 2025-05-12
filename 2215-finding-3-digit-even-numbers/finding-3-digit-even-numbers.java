class Solution {
    List<Integer> res = new ArrayList<>();
    int[] frq = new int[10];

    public void DFS(int n) {
        if (n > 99) {
            if (n % 2 == 0) {
                res.add(n);
            }
            return;
        }
        
        for (int i = (n == 0 ? 1 : 0); i < 10; i++) {
            if (frq[i] > 0) {
                frq[i]--;
                DFS(n * 10 + i);
                frq[i]++;
            }
        }
    } 
    public int[] findEvenNumbers(int[] digits) {
        Arrays.fill(frq, 0);
        for (int n : digits) {
            frq[n]++;
        }
        DFS(0);
        return res.stream().mapToInt(Integer::intValue).toArray();
    }

}