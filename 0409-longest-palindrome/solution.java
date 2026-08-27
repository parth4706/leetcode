class Solution {
    public int longestPalindrome(String s) {
        HashMap<Character,Integer> freq = new HashMap<>();
        boolean flag = false;
        int res = 0;
        for(char i:s.toCharArray()){
            freq.put(i,freq.getOrDefault(i,0)+1);
        }
        
        for(char i:freq.keySet()){
            if(freq.getOrDefault(i,0)%2==0){
                res += freq.getOrDefault(i,0);
            }
            else{
                res += freq.get(i) -1;
                flag = true;
            }
        }
        if(flag){
            return ++res;
        }else{
            return res;
        }
    }
}
