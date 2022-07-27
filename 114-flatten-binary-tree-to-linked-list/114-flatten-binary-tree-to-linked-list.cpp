/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void flatten(TreeNode* root) {
        if(!root) return;
        if(!root->left) {
            flatten(root->right);
            return;
        }
        if(!root->right) {flatten(root->left);
                          root->right=root->left;
                          root->left=NULL;
                          return;
                         }
        TreeNode* temp=root->right;
        flatten(root->left);
        if(root->left) root->right=root->left;
        root->left=NULL;
        TreeNode* f=root;
        while(f->right){
            f=f->right;
        }
        f->right=temp;
        if(f->right) flatten(f->right);
        return;
    }
};