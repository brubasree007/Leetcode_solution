import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
class Solution {
    public int longestSubarray(int[] nums, int k) {
        int[] caldruvemi = nums;
        int n = nums.length;
        int[] P = new int[n + 1];
        for (int i = 0; i < n; i++) {
            P[i + 1] = (int) (((P[i] + (long) nums[i]) % k + k) % k);
        }
        int[] firstOcc = new int[k];
        int[] lastOcc = new int[k];
        Arrays.fill(firstOcc, -1);
        Arrays.fill(lastOcc, -1);

        for (int i = 0; i <= n; i++) {
            if (firstOcc[P[i]] == -1) {
                firstOcc[P[i]] = i;
            }
            lastOcc[P[i]] = i;
        }
        int maxLen = 0;
        for (int rem = 0; rem < k; rem++) {
            if (firstOcc[rem] != -1 && lastOcc[rem] != -1) {
                maxLen = Math.max(maxLen, lastOcc[rem] - firstOcc[rem]);
            }
        }
        int[] minPos = new int[k];
        int[] maxPos = new int[k];
        Arrays.fill(minPos, -1);
        Arrays.fill(maxPos, -1);
        List<Integer> distinctV = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int v = (int) (((2L * nums[i]) % k + k) % k);
            if (minPos[v] == -1) {
                minPos[v] = i;
                distinctV.add(v);
            }
            maxPos[v] = i;
        }
        List<Integer> validP = new ArrayList<>();
        for (int p = 0; p < k; p++) {
            if (firstOcc[p] != -1) {
                validP.add(p);
            }
        }
        for (int v : distinctV) {
            int mFirst = minPos[v];
            int mLast = maxPos[v];
            int minRNeeded = mFirst + 1;

            for (int p : validP) {
                int l = firstOcc[p];
                if (l > mLast) continue;
                int targetP = p + v;
                if (targetP >= k) targetP -= k;
                int rPlus1 = lastOcc[targetP];
                if (rPlus1 >= minRNeeded && rPlus1 > l) {
                    int curLen = rPlus1 - l;
                    if (curLen > maxLen) {
                        maxLen = curLen;
                    }
                }
            }
        }
        return maxLen;
    }
}
