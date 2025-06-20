class Solution {
    public String generateTag(String caption) {
        if (caption == null || caption.isEmpty()) {
            return "#";
        }

        String[] words = caption.trim().split("\\s+");

        StringBuilder tag = new StringBuilder("#");

        for (int i = 0; i < words.length; i++) {
            String w = words[i];
            if (w.isEmpty()) continue;
            w = w.toLowerCase();
            if (i == 0) {
                tag.append(w);
            } else {
                tag.append(Character.toUpperCase(w.charAt(0)));
                tag.append(w.substring(1));
            }
        }

        StringBuilder cleaned = new StringBuilder("#");
        for (int i = 1; i < tag.length(); i++) {
            char ch = tag.charAt(i);
            if (Character.isLetter(ch)) {
                cleaned.append(ch);
            }
        }

        if (cleaned.length() > 100) {
            return cleaned.substring(0, 100);
        }

        return cleaned.toString();
    }
}