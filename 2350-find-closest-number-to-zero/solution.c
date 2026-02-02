int findClosestNumber(int* nums, int numsSize) {
    int res = nums[0];
    for(int i=0;i<numsSize-1;++i){
        if(abs(res)>abs(nums[i+1])){
            res = nums[i+1];
        }
        if(abs(res)==abs(nums[i+1]) && res < nums[i+1]){
            res = nums[i+1];
        }
    }
    return res;
}
