class Solution {
    public String longestCommonPrefix(String[] strs) 
    {  if ( strs == null || strs.length == 0)
        {
        return "";
        }
        String shortest = strs[0];
        for( String s : strs)
        {
            if ( s.length() < shortest.length())
            {
                shortest = s;
            }
           
        }
        StringBuilder sb = new StringBuilder();
        
        for(int i = 0; i< shortest.length(); i++)
        {
         for(String s :strs)
         {
            if(shortest.charAt(i) != s.charAt(i))
            {
               return sb.toString();
            }           
         }
         sb.append(shortest.charAt(i));  
        } 
        return sb.toString();
    }
}