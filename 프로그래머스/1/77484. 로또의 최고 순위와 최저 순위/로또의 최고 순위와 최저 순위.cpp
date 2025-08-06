#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> lottos, vector<int> win_nums) {
    int same = 0;
    int zero = 0;

    for (int lotto : lottos) {
        if (find(win_nums.begin(), win_nums.end(), lotto) != win_nums.end()) {
            same++;
        }
        if (lotto == 0) {
            zero++;
        }
    }

    int best = (same + zero == 0) ? 6 : 7 - (same + zero);
    int worst = (same == 0) ? 6 : 7 - same;

    return {best, worst};
}