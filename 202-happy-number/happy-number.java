class Solution {
    public boolean isHappy(int n) 
    {  
        //Mehnaz Java Solution
        //HashSet and dunction method
        //Time complexity = O(log n)
        //Space Complexity = O(log n) - usage of HashSet

        HashSet<Integer> seen = new HashSet<>();
        while( n != 1)
        {
            if(seen.contains(n))
            {
                return false; // we have detected infinite loop
            }
            else
            {
                seen.add(n);
                n = getSum(n);
            }
        }
      return true;
    }
    public static int getSum(int num)
    {
        int sum = 0;
        while(num > 0)
        {
            int digit = num % 10;
            sum += digit * digit;
            num /= 10;
        }
        return sum;
    }
}