class Solution {
private:
    void invert(TreeNode* node) {
        if (node == nullptr) {
            return;
        }

        TreeNode* temp = node->right;
        node->right = node->left;
        node->left = temp;

        invert(node->left);
        invert(node->right);
    }

public:
    TreeNode* invertTree(TreeNode* root) {
        invert(root);
        return root;
    }
};