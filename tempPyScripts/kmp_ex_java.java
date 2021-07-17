class Solution {
  private int[] computeLPS(String str) { // computes Longest Prefix Suffix (LPS) array
    int[] lps = new int[str.length()];
    lps[0] = 0;
    int i = 1; // always walks forward
    int j = 0; // tracks prefix that matches suffix

    while (i < str.length()) {
      if (str.charAt(i) == str.charAt(j)) {
        j++;
        lps[i] = j;
        i++;
      } else { // mismatch
        if (j == 0) { // go onto next character in string
          lps[i] = 0;
          i++;
        } else { // backtrack j to check previous matching prefix
          j = lps[j - 1];
        }
      }
    }
    return lps;
  }

  int strStr(String haystack, String needle) {
      if (haystack == null || needle == null || haystack.length() < needle.length()) {
          return -1;
      } else if (needle.isEmpty()) {
          return 0;
      }

      int[] lps = computeLPS(needle);
      int i = 0;
      int j = 0;
      System.out.println(lps);

      while (i < haystack.length()) {
          if (needle.charAt(j) == haystack.charAt(i)) {
              i++;
              j++;
              if (j == needle.length()) {
                  return i - j; // match found. Return location of match
              }
          } else {
              if (j == 0) {
                  i++;
              } else {
                  j = lps[j - 1]; // backtrack j to check previous matching prefix
              }
          }
      }

      return -1; // did not find needle
  }
}
public class kmp_ex_java {

public static void main(String[] args){

  Solution s=new Solution();
  String s1 = "hello";
  String s2 = "ll";
  Integer s3 = s.strStr(s1,s2);
  System.out.println(s3);


}


}
