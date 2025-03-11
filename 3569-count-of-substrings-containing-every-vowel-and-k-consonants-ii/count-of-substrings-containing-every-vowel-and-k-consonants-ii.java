class Solution {
    public long countOfSubstrings(String word, int k) {
        int n = word.length();
        String vowels = "aeiou";
        Set<Character> vs = new HashSet<>();

        for (char ch : vowels.toCharArray()) {
            vs.add(ch);
        }

        // map to count occurences of vowels in curr window
        Map<Character, Integer> vcount = new HashMap<>();
        long count = 0;
        int left = 0;
        long substr = 0;
        long cons = 0;

        for(int i = 0; i < n; i++) {
            char ch = word.charAt(i);
            if (vs.contains(ch)) {
                vcount.put(ch, vcount.getOrDefault(ch, 0) + 1);
            } else {
                cons++;
                count = 0; // we have to reset count when cons is added
            }

            while(cons > k) {
                char leftch = word.charAt(left);
                if(vs.contains(leftch)) {
                    int curr = vcount.get(leftch);
                    if(curr == 1) {
                        vcount.remove(leftch);
                    } else {
                        vcount.put(leftch, curr - 1);
                    }
                } else {
                    cons--;
                }
                left++;
            }

            while (cons == k && vcount.size() == 5) {
                count++;
                char leftch = word.charAt(left);
                if (vs.contains(leftch)) {
                    int curr = vcount.get(leftch);
                    if (curr == 1) {
                        vcount.remove(leftch);
                    } else {
                        vcount.put(leftch, curr - 1);
                    }
                } else {
                    cons--;
                }
                left++;
            }
            
            // Add the count for this window to the overall substring count.
            substr += count;
        }
        return substr;
    }
}