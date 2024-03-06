# Now we are goint to explore what and how to use pipes in c

## Topics

References: 
- https://www.programacaoprogressiva.net/2014/09/Pipes-em-C-Comunicao-entre-Processos-IPC-Interprocess-Communication.html
- https://www.geeksforgeeks.org/pipe-system-call/
- https://www.geeksforgeeks.org/pipe-system-call/

---

## What are pipes ?

When dealing with process it is normal to want to transmit information between them,  so for this problem, pipes and relating syscalls  were created.

In a pipe information can only flow in one way so we need two things to define a pipe, a integer to define the sdt input [read()] and another to define the sdt output [write()], this are the file descriptors for our pipe, so in reality we only need a vector with two position.

The first element (element 0) of the vector defines the reading (output) of data, and the second element (with index 1) defines the writing of data to the pipe (input).  **V[READ, WRITE]**.

## How to Program ?
```
// return -1 if an error ocour 
int fd[2];

if (pipe(fd) == -1) {
        perror("pipe");
        exit(1);
}
```
### example: 
In this example we will transfer a message from the parent to the child

```
#include <stdio.h> 
#include <stdlib.h>
#include <sys/types.h> // for funtion pid_t, used for get an process IDs
#include <unistd.h> // provides access to the POSIX operating system API
```

```

int main(void)
{
    int fd[2]; /* File descriptors for Pipe*/
    pid_t pid; /* Variable to store the pid */

    /* Creating our Pipe */
    if(pipe(fd)<0) {
        perror("pipe") ;
        return -1 ;
    }
```
```

    /* Creating the child process */
    if ((pid = fork()) < 0)
    {
        perror("fork");
        exit(1);
    }
```
Because the parent will WRITE, we will close the READ Pipe on this side

(failure in to do can cause an infinity loop)
```
    
    /* Parent Process */
    if (pid > 0)
    {
        close(fd[0]); <--- closing the read end

        char str[256] = "I learned how to use Pipes in C!";
        printf("String sent by the parent in the Pipe: '%s'", str);

        write(fd[1], str, sizeof(str) + 1); <--- Writing the string to the pipe
        // sizeof(str) + 1 is to accommodate the \0 character, which delimits a string.
        exit(0);
    }
```
Because we are gonna READ we will close the WRITE Pipe on this side
```
    /* Child Process */
    else
    {
        char str_received[256];
        
        close(fd[1]); <--- closing the write end

        /* Reading what was written to the pipe, and storing it in 'str_recebida' */
        read(fd[0], str_recebida, sizeof(str_recebida));

        printf("String read by the child in the Pipe: '%s'\n\n", str_received);
        exit(0);
    }

    return(0);
}
```
