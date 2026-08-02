class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t tmp = 0;

        for (int i = 0; i < 32; i++) {
            tmp <<= 1;
            tmp |= (n & 1);
            n >>= 1;
        }

        return tmp;
    }
};
