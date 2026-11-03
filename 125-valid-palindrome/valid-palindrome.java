class Solution {
    public boolean isPalindrome(String s) 
    {
       String ss = s.toLowerCase();
       String word = ss.replaceAll("[^a-z0-9]","");
       int right = word.length()-1;
       int left =0;
       while(left < right)
       {
        if(word.charAt(left) == word.charAt(right))
        {
            left++;
            right--;
        }
        else
        {
            return false;
        }
       }
       return true;
    }
}