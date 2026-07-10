class Solution {
    public boolean containsDuplicate(int[] nums) 
    {
        // Optimal Approach
        HashSet <Integer> set = new HashSet<>();
        for (int n : nums)
        {
            if(set.contains(n))
            {
                return true;
            }
            set.add(n);
        }
        return false;
        
    }
}