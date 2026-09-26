#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int longestSubarray(vector<int>& nums, int k) {
        int n = nums.size();
        int ans = 0;

        // earliest_pref[r] stores the earliest prefix index where prefix % k == r
        vector<int> earliest_pref(k, -1);
        earliest_pref[0] = 0;

        // min_l[r] stores the minimum l such that (P[l] + 2*nums[m]) % k == r for some m >= l
        vector<int> min_l(k, 1e9);

        int curr = 0;
        for (int i = 0; i < n; ++i) {
            int x = nums[i];
            int rem_x = ((2LL * x) % k + k) % k;

            // Update min_l with nums[i] acting as the negated element m
            for (int p = 0; p < k; ++p) {
                if (earliest_pref[p] != -1) {
                    int target = (p + rem_x) % k;
                    if (earliest_pref[p] < min_l[target]) {
                        min_l[target] = earliest_pref[p];
                    }
                }
            }

            curr = ((curr + x) % k + k) % k;

            // Check no-negation
            if (earliest_pref[curr] != -1) {
                ans = max(ans, (i + 1) - earliest_pref[curr]);
            } else {
                earliest_pref[curr] = i + 1;
            }

            // Check with negation
            if (min_l[curr] <= i) {
                ans = max(ans, (i + 1) - min_l[curr]);
            }
        }

        return ans;
    }
};
