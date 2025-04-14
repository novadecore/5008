|Traversal|	Visit Order|	Use Case
|---|---|---|
Inorder|	Left → Root → Right|	BST: sorted output
Preorder|	Root → Left → Right|	Copying a tree, prefix expr.
Postorder|	Left → Right → Root|	Deleting tree, postfix expr.
Level Order|	Top-down left-right|	BFS, layer-wise access


### BST
Enables efficient search, insert, delete: O(log n) if balanced
O(n) worst

```c
#include <stdio.h>
#include <stdlib.h>

// Tree node definition
struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

// BFS traversal using array as queue
void bfs(struct TreeNode* root) {
    if (!root) return;

    // Allocate space for up to 1000 nodes (adjust if needed)
    struct TreeNode* queue[1000];
    int front = 0;
    int rear = 0;

    // Enqueue root
    queue[rear++] = root;

    while (front < rear) {
        struct TreeNode* current = queue[front++];  // Dequeue
        printf("%d ", current->val);

        // Enqueue children
        if (current->left) queue[rear++] = current->left;
        if (current->right) queue[rear++] = current->right;
    }
    printf("\n");
}
```