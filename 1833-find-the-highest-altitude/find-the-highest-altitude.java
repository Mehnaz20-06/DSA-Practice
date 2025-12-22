class Solution {
    public int largestAltitude(int[] gain) 
    {   //Mehnaz
        int current_gain = 0;
        int max_gain = 0;
        for(int x : gain)
        {
            current_gain += x;
            max_gain= Math.max(max_gain,current_gain);
        }
        return max_gain;
    }
}