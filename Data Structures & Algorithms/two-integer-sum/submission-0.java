class Solution {
    public int[] twoSum(int[] nums, int target) {
        LinkedHashMap<Integer, Integer> lhm = new LinkedHashMap<>();
        int[] retArr = new int[2];
        int remaining;
        for (int i=0; i<nums.length; i++){
            int value = nums[i];
            remaining = target - value;
            if(!lhm.containsValue(remaining)){
                lhm.put(i, value);
            }else{
                retArr[1] = i;
                for (Map.Entry<Integer,Integer> entry : lhm.entrySet()) {
                    if (entry.getValue()==remaining){
                        retArr[0] = entry.getKey();
                        break;
                    }
                }
            }
        }
        return retArr;
    }
}