## pointers
**A pointer is essentially a simple integer variable which holds a memory address that points to a value, instead of holding the actual value itself.**

```c
char * name = "John";
```
1. It allocates a local (stack) variable called name, which is a pointer to a single character.
2. It causes the string "John" to appear somewhere in the program memory (after it is compiled and executed, of course).
3. It initializes the name argument to point to where the J character resides at (which is followed by the rest of the string in the memory).

#### Dereferencing
**Dereferencing is the act of referring to where the pointer points, instead of the memory address.**
```c
/* define a local variable a */
int a = 1;

/* define a pointer variable, and point it to a using the & operator */
int * pointer_to_a = &a; // & operator to point at the variable a

printf("The value a is %d\n", a);
printf("The value of a is also %d\n", *pointer_to_a); //* is the dereferencing operator that can also be operated
```
#### address
```c
#include <stdio.h>

int main() {
    int value = 5;              // A regular integer variable
    int *p_value = &value;      // A pointer storing the address of 'value'

    printf("Address of value (&value): %p\n", (void *)&value); // Address of value
    printf("Value of p_value (pointer): %p\n", (void *)p_value); // Address stored in p_value (same as &value)
    printf("Address of p_value (&p_value): %p\n", (void *)&p_value); // Address of the pointer variable itself
    printf("Value of p_value (pointer): %d\n", *p_value); // value stored in p_value address (same as value)
    return 0;
}
//A void * can represent any pointer type (int *, char *, etc.) without needing to know the type of the data it points to.
```
