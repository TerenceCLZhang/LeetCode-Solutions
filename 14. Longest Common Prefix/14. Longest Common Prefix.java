class Solution {
    public String longestCommonPrefix(String[] strs) {
        int minLength = Integer.MAX_VALUE;
        for (String s : strs) {
            if (s.length() < minLength) {
                minLength = s.length();
            }
        }

        for (int i = 0; i < minLength; i++) {
            for (String s : strs) {
                if (strs[0].charAt(i) != s.charAt(i)) {
                    return s.substring(0, i);
                }
            }
        }

        return strs[0].substring(0, minLength);
    }
}