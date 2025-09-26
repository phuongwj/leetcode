class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& a) {
        stack<pair<int,int>> stk; int n = a.size(); vector<int> ans(n,0);
        for(int i = 0; i<n; ++i){
            while(!stk.empty() && stk.top().first < a[i]){
                ans[stk.top().second] = i-stk.top().second;
                stk.pop();
            }
            stk.push({a[i],i});
        }
       
        return ans;
    }
};