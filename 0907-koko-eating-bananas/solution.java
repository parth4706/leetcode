
class Solution {
    public boolean test(int k,int[] piles,int h){
        int hours = 0;
        for (int i = 0;i< piles.length;i++){
            if(piles[i]%k==0){
                hours = hours + piles[i]/k;
            }
            else{
            hours = hours + piles[i]/k + 1;
            }
        }
        return hours <= h;
    }
    public int minEatingSpeed(int[] piles, int h) {
        int l = 1;
        int r = 0;
        for (int i = 0;i < piles.length;i++){
            if(r<piles[i]){
                r = piles[i];
            }
        }
        while(l<r){
            int m = l + (r-l)/2;
            if (test(m,piles,h)){
                r = m;
            }
            else{
                l = m+1;
            }
        }
        return l;
    }
}
