class Solution {
    public int[] intersection(int[] nums1, int[] nums2) 
    {
        HashSet<Integer> set = new HashSet<>();
        for(int n1: nums1)
        {
            set.add(n1);
        }
        ArrayList<Integer> result = new ArrayList<>();
        for(int n2: nums2)
        {
            if(set.contains(n2))
            {
                result.add(n2);
                set.remove(n2);
            }
        }
        int[] ans = new int[result.size()];
        for(int i = 0 ; i < result.size() ;i++)
        {
            ans[i]=result.get(i);
        }
        return ans;
    }
}