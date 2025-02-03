```c
#include <stdio.h>

// Function to swap two elements
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Function to perform Selection Sort
void selectionSort(int array[], int size) {
    for (int i = 0; i < size - 1; i++) {
        int minIndex = i; // Assume the first unsorted element is the smallest
        for (int j = i + 1; j < size; j++) {
            if (array[j] < array[minIndex]) {
                minIndex = j; // Update minIndex if a smaller element is found
            }
        }
        // Swap the found minimum element with the first unsorted element
        swap(&array[i], &array[minIndex]);
    }
}

// Function to print the array
void printArray(int array[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");
}

// Main function to test the sorting algorithm
int main() {
    int array[] = {64, 25, 12, 22, 11};
    int size = sizeof(array) / sizeof(array[0]);

    printf("Original array: ");
    printArray(array, size);

    selectionSort(array, size);

    printf("Sorted array: ");
    printArray(array, size);

    return 0;
}

```
#### LC
```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 * 2.selection sort
 */
int* sortArray(int* nums, int numsSize, int* returnSize) {
    * returnSize = numsSize;
    for(int i=0; i<(*returnSize); i++){
        int min = i;
        for(int j=i+1; j<(*returnSize); j++){
            if(nums[j]<nums[min]){
                min = j;
            }
        }
        int temp = nums[i];
        nums[i] = nums[min];
        nums[min] = temp;
    }
    return nums;
}
```