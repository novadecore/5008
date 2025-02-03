## Allowed Characters:

**Variable names can contain:**
* Letters (a to z, A to Z)
* Digits (0 to 9)
* Underscore (_)


**Variable names must start with a letter or an underscore.**
```c
int _myVar; // Valid
int myVar2; // Valid
int 2myVar; // Invalid
```


**Variable names cannot include symbols like @, $, %, *, or spaces.**
```c
int my$var; // Invalid
int my var; // Invalid
```


**Variable names cannot be C keywords (e.g., int, return, if, for, etc.).**
```c
int if; // Invalid
```

**Variable names are case-sensitive.**
```c
int myVar;  // Different from
int MyVar;  // These are two distinct variables.
```


## datatype
**Integers - whole numbers which can be either positive or negative.**
```c
//Defined using:
char, int, short, long or long long.
//A char can range only from -128 to 127
//a long can range from -2,147,483,648 to 2,147,483,647
//a int can range from -2,147,483,648 to 2,147,483,647
```
**Unsigned integers - whole numbers which can only be positive.**
```c
//Defined using:
unsigned char, unsigned int, unsigned short, unsigned long or unsigned long long.
```
**Floating point numbers - real numbers (numbers with fractions).**
```c
//Defined using
float and double.
```
**C does not have a boolean type**
```c
#define BOOL char
#define FALSE 0
#define TRUE 1
```

## quotation

#### Single Quotes (')
**Used to represent a single character constant.**
```c
// Enclosed characters are of type char and have an integer value (ASCII value or Unicode).

char c = 'A';   // 'A' is a single character.
char newline = '\n'; // '\n' is the newline character.
```
#### Double Quotes(")
**Used to represent a string literal (a sequence of characters ending with a null terminator \0).**
```c
// Enclosed characters form a char array.
```

## Arrays
```c
/* defines an array of 10 integers */
int numbers[10];
/* populate the array */
numbers[0] = 10;
numbers[1] = 20;
numbers[2] = 30;
numbers[3] = 40;
numbers[4] = 50;
numbers[5] = 60;
numbers[6] = 70;
```

## Multidimensional Arrays
```c
// type name[size1][size2]...[sizeN];
int foo[1][2][3];

char vowels[1][5] = {
    {'a', 'e', 'i', 'o', 'u'}
};
```

#### Two-dimensional Arrays
```c
// type arrayName [x][y];
char vowels[][5] = {
    {'A', 'E', 'I', 'O', 'U'},
    {'a', 'e', 'i', 'o', 'u'}
};
// other ways of initialization
int a[3][4] = {0,1,2,3,4,5,6,7,8,9,10,11};

//Accessing Two-Dimensional Array Elements
int val = a[2][3];
```
#### space omitted rule
Array Type |First Dimension Omitted? |Second Dimension Omitted? |Conditions
|----|----|---|----|
Single-dimensional (int, float) |✅ (with initialization) |N/A |Size deduced from initializer.
Two-dimensional (int, float) |✅ (with initialization) |❌ |Compiler needs the size of the second dimension.
Single-dimensional (char) |✅ (with string literal) |N/A |Size deduced from string literal or initializer.
Two-dimensional (char) |✅ (with initialization) |❌ |Second dimension must be specified.


## Conditions
```c
int foo = 1;
int bar = 2;

if (foo < bar) {
    printf("foo is smaller than bar.");
} else if (foo == bar) {
    printf("foo is equal to bar.");
} else {
    printf("foo is greater than bar.");
}
```

## Strings
**Strings in C are actually arrays of characters.**
```c
char * name = "John"; //we can only use for reading.
char name[] = "John"; //can be manipulated.
// The empty brackets notation [] tells the compiler to calculate the size of the array automatically. 
```
* char *
1. Declares a pointer variable name of type char *, which points to a memory location holding a string.

* "John"
2. A string literal, stored in a read-only memory section. The string is null-terminated ("John\0), making it a valid C string.

* Pointer Assignment:
3. The pointer name is initialized to point to the beginning of the string literal "John".

#### Key Differences Between char * and char[]
Aspect |char *name = "John"; |char name[] = "John";
|----|----|----|
Storage |Points to a string literal in read-only memory. |Stores a copy of the string in writable memory.
Writable |No (modification causes undefined behavior). |Yes (contents can be changed).
Memory Usage |Only space for the pointer is allocated. |Allocates memory for the entire string.
Reassignable Pointer |Yes, can point to another string. |No, fixed size and location.



#### String formatting with printf
```c
char * name = "John Smith";
int age = 27;

/* prints out 'John Smith is 27 years old.' */
printf("%s is %d years old.\n", name, age);
```

#### String Length
```c
char * name = "Nikhil";
printf("%d\n",strlen(name)); // The function 'strlen' returns the length of the string 
```

#### String comparison
```c
char * name = "John";
//  returning the number 0 if they are equal, or a different number if they are different. 
if (strncmp(name, "John", 4) == 0) {
    printf("Hello, John!\n");
} else {
    printf("You are not John. Go away.\n");
}
// arguments are the two strings to be compared, and the maximum comparison length.
```

#### String Concatenation
```c
char dest[20]="Hello";
char src[20]="World";
strncat(dest,src,3);
printf("%s\n",dest); // HelloWor
strncat(dest,src,20);
printf("%s\n",dest); // HelloWorWorld
```



## loop

#### for loop
**For loops give the following functionality:**
* Initialize the iterator variable using an initial value
* Check if the iterator has reached its final value
* Increases the iterator
```c
int i;
for (i = 0; i < 10; i++) {
    printf("%d\n", i);
}
// This block will print the numbers 0 through 9 (10 numbers in total).
```

#### While loops
**While loops are similar to for loops, but have less functionality.**
```c
//similar to for loop above
int n = 0;
while (n < 10) {
    n++;
}

// condition is given which always evaluates as true (non-zero):
while (1) {
   /* do something */
}

```

#### break and continue
```c
// break
int n = 0;
while (1) {
    n++;
    if (n == 10) {
        break;
    }
}

// continue
int n = 0;
while (n < 10) {
    n++;

    /* check that n is odd */
    if (n % 2 == 1) {
        /* go back to the start of the while block */
        continue;
    }

    /* we reach this code only if n is even */
    printf("The number %d is even.\n", n);
}
```

## Functions
* Functions receive either a fixed or variable amount of arguments.
* Functions can only return one value, or return no value.
```c
int foo(int bar) {
    /* do something */
    return bar * 2;
}

int main() {
    foo(1);
}
```

#### initialize after use
```c
/* function declaration */
int foo(int bar);

int main() {
    /* calling foo from main */
    printf("The value of foo is %d", foo(1));
}

int foo(int bar) {
    return bar + 1;
}
```

#### don't return value
```c
void moo() {
    /* do something and don't return a value */
}

int main() {
    moo();
}
```

## Static
**By default, variables are local to the scope in which they are defined. Variables can be declared as static to increase their scope up to file containing them**
```c
//without static
#include<stdio.h>
int runner() {
    int count = 0;
    count++;
    return count;
}

int main()
{
    printf("%d ", runner());
    printf("%d ", runner());
    return 0;
}
// 1 1
```
```c
#include<stdio.h>
int runner()
{
    static int count = 0;
    count++;
    return count;
}

int main()
{
    printf("%d ", runner());
    printf("%d ", runner());
    return 0;
}
// 1 2
```

#### static function
**By default, functions are global in C. If we declare a function with static, the scope of that function is reduced to the file containing it.**
```c
static void fun(void) {
   printf("I am a static function.");
}
// can't access outside of file
```

Specifier	|Input Type	|Example Input	|Description|
|---|---|---|---|
%d	|int	|42	|Reads a decimal integer.
%f	|float	|3.14	|Reads a floating-point number.
%lf	|double	|3.14159	|Reads a double-precision floating-point number.
%c	|char	|a	|Reads a single character.
%s	|char[]	|hello	|Reads a string (up to the first whitespace).
%x	|int	|1a	|Reads a hexadecimal integer.
%o	|int	|52	|Reads an octal integer.