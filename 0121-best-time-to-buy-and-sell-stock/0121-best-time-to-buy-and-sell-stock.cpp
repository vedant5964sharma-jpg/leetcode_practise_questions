class Solution {
public:
    int maxProfit(vector<int>& prices) {
       int n=prices.size();
        int minprice=prices[0];
        int profit;
        int maxprofit=0;
        for(int i=0;i<n;i++){
            if(prices[i]<minprice){
                minprice=prices[i];
            }
            else{
                profit=prices[i]-minprice;
                maxprofit=max(profit,maxprofit);
            }
        }
        return maxprofit;  
    }
};