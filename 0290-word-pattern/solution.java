class Solution {
    public boolean wordPattern(String pattern, String s) {
        String[] arr = s.split(" ");
        HashMap<Character,String> m = new HashMap<>();
        int c = 0;
        if(pattern.length()!=arr.length){
            return false;
        }
        for (char i : pattern.toCharArray()){
            if(m.containsKey(i)){
                if(!(m.get(i).equals(arr[c]))){
                    
                    return false;
                }
            }else{
                if(m.containsValue(arr[c])){
                    return false;
                }
                m.put(i,arr[c]);
                
            }
            c++;
        }
        return true;
    }
}
