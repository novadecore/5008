use extern in declaring variable later
& between files

### static
**Inside a function: Retains value between calls.**
**Global scope: Restricts visibility to the file.**
**Functions: Makes the function private to the file.**
```c
#include <stdio.h>

void counter() {
    static int count = 0; // Retains its value between calls
    // Visible only in this file
    count++;
    printf("Count: %d\n", count);
}

int main() {
    counter(); // Output: Count: 1
    counter(); // Output: Count: 2
    counter(); // Output: Count: 3
    return 0;
}

```

### register
```c
#include <stdio.h>

void countTo100() {
    register int i; // Suggest storing `i` in a CPU register
    for (i = 0; i < 100; i++) {
        printf("%d ", i);
    }
}
```