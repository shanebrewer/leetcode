public class Solution { 
    public int[] TwoSum(int[] nums, int target) {
        if(nums.Length < 2)
            return null;
        
        Dictionary<int, int> traversedNumbers = new Dictionary<int, int>();
        
        for(int i=0; i < nums.Length; i++) {
            if(traversedNumbers.ContainsKey(target-nums[i])) {
                int[] matchedIndices = {traversedNumbers[target-nums[i]], i};
                return matchedIndices;
            }        
            
            // Add this number to the dictionary
            traversedNumbers.TryAdd(nums[i], i);
        }
        return null;
    }
}