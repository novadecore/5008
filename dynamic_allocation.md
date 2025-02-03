```c
typedef struct {
    char * name;
    int age;
} person;
//To allocate a new person in the myperson argument, we use the following syntax:

person * myperson = (person *) malloc(sizeof(person));

//To access the person's members, we can use the -> notation:

myperson->name = "John";
myperson->age = 27;
//After we are done using the dynamically allocated struct, we can release it using free:

free(myperson);
```