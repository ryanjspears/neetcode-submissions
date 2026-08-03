class Solution {
public:
    int hammingWeight(uint32_t n) {
        int count = 0;
        for (int i = 0; i < 32; i++) {
            count += (1 & n);
            n >>= 1;
        }

        return count;
    }
    vector<int> countBits(int n) {
        vector<int> result;

        for (int i = 0; i <= n; i++) {
            result.push_back(hammingWeight(i));
        } 

        return result;
        
    }
};
