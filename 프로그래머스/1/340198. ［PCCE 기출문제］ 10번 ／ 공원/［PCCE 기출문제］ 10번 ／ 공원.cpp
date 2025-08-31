#include <bits/stdc++.h>
using namespace std;

int solution(vector<int> mats, vector<vector<string>> park) {
    int answer = -1;
    
    int R = park.size(), C = park[0].size();
    
    vector<vector<int>> dp(R, vector<int>(C, 0));
    
    int maxSq = 0;
    
    for (int i=0; i<R; i++) {
        for (int j=0; j<C; j++) {
            if (park[i][j] == "-1") {
                if (i==0 || j==0) {
                    dp[i][j] = 1;
                } else {
                    dp[i][j] = 1 + min({dp[i-1][j], dp[i][j-1], dp[i-1][j-1]});
                }
                maxSq = max(maxSq, dp[i][j]);
            }
        }
    }

    for (int m: mats) {
        if (m <= maxSq) {
            answer = max(answer, m);
        }
    }
    
    return answer;
}