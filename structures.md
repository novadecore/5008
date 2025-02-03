## Structures

```c
struct point {
    int x;
    int y;
};

//without struct
/* draws a point at 10, 5 */
int x = 10;
int y = 5;
draw(x, y);

//with struct
/* draws a point at 10, 5 */
struct point p;
p.x = 10;
p.y = 5;
draw(p);
```

## Typedefs
**typedef is a keyword used to create an alias (alternative name) for an existing type.**
```c
struct Point {
    int x, y;
};

struct Point p1; // Must use 'struct' every time

// with typedef
typedef struct {
    int x, y;
} Point;

Point p1; // 'struct' keyword is no longer needed