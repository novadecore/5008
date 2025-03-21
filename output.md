### printf
%d → print integer
%f → print double/float
%s → print null-terminated string
%c → print a single character
\n → newline

### scanf
```c
int x;
printf("Enter an integer: ");
scanf("%d", &x);
printf("You entered %d\n", x);
```
```c
int a, b;
int ret = scanf("%d %d", &a, &b);
if (ret < 2) {
    // means it didn't successfully read 2 integers
    fprintf(stderr, "Invalid input.\n");
    // handle error or re-prompt
}
else {
    // proceed with valid input
}
```
* If ret is 2, both integers were read successfully.
* If ret is 1 or 0, input was invalid (like typing letters or only one integer).
* If ret is EOF, user ended input (Ctrl+D, or file ended).
```c
//clean buffer
while (scanf("%d", &num) != 1) {
    printf("Invalid input. Please enter a number: ");
    // discard remaining invalid characters until newline
    while (getchar() != '\n');  
}
// now 'num' is valid
```

### read/write a line
**fget()**
* On success, returns str (the same pointer you passed in).
* Returns NULL if no character read (EOF or error).
* Reads up to n-1 characters, plus '\0'.
* Stops if it sees a newline or hits EOF.
```c
char line[100];
printf("Enter a line: ");
if (fgets(line, sizeof(line), stdin) != NULL) {
    // Strip trailing newline if desired
    // Process 'line'
}
```
```c
scanf("%s", str)
```

### read/write by char
* getchar() reads one character from stdin.
* putchar(ch) writes a single character to stdout.
```c
int ch;
while ((ch = getchar()) != EOF) {
    putchar(ch);  // Echo input back
}
```