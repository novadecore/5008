```c
#include <stdio.h>

// Function to swap two integers
void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Function to sort an array using Bubble Sort
void sortInteger(int* array, unsigned int size) {
    int i, j;
    for (i = 0; i < size - 1; ++i) {           // Outer loop
        for (j = 0; j < size - i - 1; ++j) {   // Inner loop, optimized
            if (array[j] > array[j + 1]) {
                swap(&array[j], &array[j + 1]); // Swap if out of order
            }
        }
    }
}

// Main function to test the sorting function
int main() {
    int array[] = {5, 3, 8, 6, 2};
    unsigned int size = sizeof(array) / sizeof(array[0]);

    printf("Original array: ");
    for (int i = 0; i < size; ++i) {
        printf("%d ", array[i]);
    }
    printf("\n");

    sortInteger(array, size);

    printf("Sorted array: ");
    for (int i = 0; i < size; ++i) {
        printf("%d ", array[i]);
    }
    printf("\n");

    return 0;
}

```
#### LC
```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 * 1.bubblesort
 */
int* sortArray(int* nums, int numsSize, int* returnSize) {
    * returnSize = numsSize;
    int count = 0;
    for(int i=0; i<(*returnSize); i++){
        for(int j=1; j<(*returnSize)-count; j++){
            if(nums[j-1]>nums[j]){
                int temp = nums[j-1];
                nums[j-1] = nums[j];
                nums[j] = temp;
            }
        }
        count++;
    }
    return nums;
}
```