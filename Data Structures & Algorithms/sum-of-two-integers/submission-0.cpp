class Solution {
public:
    int getSum(int a, int b) {
        unsigned int x = a;
        unsigned int y = b;

        while (y != 0) {
            unsigned int carry = (x & y) << 1;
            x ^= y;
            y = carry;
        }

        return static_cast<int>(x);
        
    }
};
