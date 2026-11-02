class Solution {
    public boolean isHappy(int n) 
    {
        HashSet<Integer> seen = new HashSet<>();
        
        while( n != 1)
        {    
            if (seen.contains(n))
            {
                return false;
            }
            else
            {
                seen.add(n);
                n = HappyNum(n);
            }
        }
        return true;
    }
    public static int HappyNum(int number)
    {   int sum  = 0;
        while(number > 0)
        {
          int digit = number % 10;
          sum += digit * digit;
          number = number/10;

        }
        return sum;
    }
}