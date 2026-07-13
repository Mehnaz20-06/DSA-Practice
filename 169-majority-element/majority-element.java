class Solution {
    public int majorityElement(int[] nums) 
    {
        HashMap<Integer,Integer> map = new HashMap<>();
        int n = nums.length;
        int majority = n/2;
        for(int num : nums)
        {
            map.put(num,map.getOrDefault(num , 0)+1);
        }
        for(Map.Entry<Integer,Integer> entry :map.entrySet())
        {
            if(entry.getValue() > majority)
            {
                return entry.getKey();
            }
        }
        return -1;
    }
}