```c
#include <stdio.h>

// Function to perform Insertion Sort
void insertionSort(int array[], int size) {
    for (int i = 1; i < size; i++) {
        int key = array[i]; // The element to be placed in the sorted part
        int j = i - 1;

        // Move elements of the sorted part that are greater than key
        // one position to the right
        while (j >= 0 && array[j] > key) {
            array[j + 1] = array[j];
            j--;
        }
        // Insert the key at its correct position
        array[j + 1] = key;
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
    int array[] = {12, 11, 13, 5, 6};
    int size = sizeof(array) / sizeof(array[0]);

    printf("Original array: ");
    printArray(array, size);

    insertionSort(array, size);

    printf("Sorted array: ");
    printArray(array, size);

    return 0;
}
```
#### LC
```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 * Simplified Insertion Sort
 */
int* sortArray(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize; // Set the return size

    for (int i = 1; i < numsSize; i++) {
        int key = nums[i]; // Store the current element
        int j = i - 1;

        // Shift elements to the right until the correct position is found
        while (j >= 0 && nums[j] > key) {
            nums[j + 1] = nums[j];
            j--;
        }

        // Insert the key at its correct position
        nums[j + 1] = key;
    }

    return nums; // Return the sorted array
}
```
