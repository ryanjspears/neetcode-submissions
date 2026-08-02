class Solution {
private:
    void bubbleSort(vector<int>& nums) {
    int n = nums.size();

    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;

        for (int j = 0; j < n - 1 - i; j++) {
            if (nums[j] > nums[j + 1]) {
                swap(nums[j], nums[j + 1]);
                swapped = true;
            }
        }

        // Already sorted
        if (!swapped) {
            break;
        }
    }
}

public:
    int missingNumber(vector<int>& nums) {
        int result = nums.size();

    for (int i = 0; i < nums.size(); i++) {
        result ^= i;
        result ^= nums[i];
    }

    return result;
    }
};
