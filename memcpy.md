```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    int *ptr1 = NULL;
    int *ptr2 = NULL;

    // First memory allocation
    ptr1 = (int *)malloc(10 * sizeof(int));
    if (ptr1 == NULL) {
        fprintf(stderr, "Memory allocation failed for ptr1\n");
        return 1;
    }

    // Initialize ptr1 with some values
    for (int i = 0; i < 10; i++) {
        ptr1[i] = i + 1;
    }

    // Second memory allocation
    ptr2 = (int *)malloc(20 * sizeof(int));
    if (ptr2 == NULL) {
        fprintf(stderr, "Memory allocation failed for ptr2\n");
        free(ptr1); // Free ptr1 to avoid memory leak
        return 1;
    }

    // Copy data from ptr1 to ptr2
    memcpy(ptr2, ptr1, 10 * sizeof(int));

    // Free the old memory block
    free(ptr1);

    // Initialize the remaining space in ptr2
    for (int i = 10; i < 20; i++) {
        ptr2[i] = (i + 1) * 2; // Example values
    }

    // Print the contents of ptr2
    printf("Contents of ptr2:\n");
    for (int i = 0; i < 20; i++) {
        printf("%d ", ptr2[i]);
    }
    printf("\n");

    // Free the new memory block
    free(ptr2);

    return 0;
}

```

### realloc
```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int i, num;
    int count = 0;
    int *ptr = NULL; // Initialize to NULL for safety

    do {
        printf("请输入一个整数(输入-1表示结束): ");
        scanf("%d", &num);

        if (num != -1) { // Only allocate if the input is not -1
            count++;
            ptr = (int *)realloc(ptr, count * sizeof(int));
            if (ptr == NULL) {
                fprintf(stderr, "内存分配失败\n");
                exit(1);
            }
            ptr[count - 1] = num; // Store the input in the newly allocated space
        }
    } while (num != -1);

    // Print the numbers entered
    printf("你输入的数字是: ");
    for (i = 0; i < count; i++) {
        printf("%d ", ptr[i]);
    }
    printf("\n");

    // Free the allocated memory
    free(ptr);

    return 0;
}
```