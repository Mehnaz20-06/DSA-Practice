class Solution {
    public int removeDuplicates(int[] nums) 
    {
        int n = nums.length;
        int[] result = new int[n];
        int j =  0;
        result[0] = nums[0];
        for(int i = 1 ; i < n; i++)
        {
            if(result[j] != nums[i])
            {
               j++;
               result[j] = nums[i];

            }
    
        }
        j+= 1;
        for(int i = 0; i < j;i++)
        {
            nums[i] = result[i];
        }
        return j;
    }
}