```c
void addone(int n) {
    n++; // n is a local copy, not the original variable
}

int n = 10;
printf("Before: %d\n", n);
addone(n);
printf("After: %d\n", n);
```