```c
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

// Helper function: Sort a string using insertion sort
void sortString(char* str) {
    int len = strlen(str);
    for (int i = 1; i < len; i++) {
        char key = str[i];
        int j = i - 1;
        while (j >= 0 && str[j] > key) {
            str[j + 1] = str[j];
            j--;
        }
        str[j + 1] = key;
    }
}

bool isAnagram(char* s, char* t) {
    // Check for null pointers
    if (s == NULL || t == NULL) {
        return false;
    }

    // Check if the lengths are the same
    if (strlen(s) != strlen(t)) {
        return false;
    }

    // Create copies of the strings
    char* sCopy = strdup(s);
    char* tCopy = strdup(t);

    if (sCopy == NULL || tCopy == NULL) {
        // Memory allocation failed
        free(sCopy);
        free(tCopy);
        return false;
    }

    // Sort the copies
    sortString(sCopy);
    sortString(tCopy);

    // Compare the sorted strings
    bool result = strcmp(sCopy, tCopy) == 0;

    // Free the allocated memory
    free(sCopy);
    free(tCopy);

    return result;
}
```