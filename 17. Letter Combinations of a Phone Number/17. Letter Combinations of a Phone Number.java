import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {

  public List<String> letterCombinations(String digits) {
    if (digits.equals("")) {
      return new ArrayList<>();
    }

    Map<Character, String> digitsMap = new HashMap<>();
    digitsMap.put('2', "abc");
    digitsMap.put('3', "def");
    digitsMap.put('4', "ghi");
    digitsMap.put('5', "jkl");
    digitsMap.put('6', "mno");
    digitsMap.put('7', "pqrs");
    digitsMap.put('8', "tuv");
    digitsMap.put('9', "wxyz");

    List<String> ans = new ArrayList<>();
    StringBuilder curr = new StringBuilder();

    backtrack(0, digits, digitsMap, ans, curr);
    return ans;
  }

  private void backtrack(
    int i,
    String digits,
    Map<Character, String> digitsMap,
    List<String> ans,
    StringBuilder curr
  ) {
    if (curr.length() == digits.length()) {
      ans.add(curr.toString());
      return;
    }

    String letters = digitsMap.get(digits.charAt(i));
    for (char c : letters.toCharArray()) {
      curr.append(c);
      backtrack(i + 1, digits, digitsMap, ans, curr);
      curr.deleteCharAt(curr.length() - 1);
    }
  }
}
