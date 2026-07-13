class Solution {
    public void moveZeroes(int[] nums) 
    {
        //Optimal Appproach 
        //TC - O(N) - single traversal
        //SC - O(1) - single bariable used for swapping
        int interpos = 0;
        for(int i = 0; i < nums.length ; i++)
        {
            if(nums[i] != 0)
            {
                int temp =  nums[i];
                nums[i] = nums[interpos];
                nums[interpos] = temp;
                interpos++;
            }
        }
    }
}