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
### Example: 
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
![Resulst](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEglptUwgF4sVwpE6raSVfIbxkP6xtgDFKRwzsJTMDwB_M0KaVLqdUDXPYbidHKyWuwnwD1qedCMyhnlvWP6-auqBEA6HAFQlWSDnr5zzWT2pVdLlFJHg7YrqFprUv6dlsVGwKbZf5lUsz4/s1600/pipes-em-c-como-enviar-string.png)



## Let's dive deeper
### Pipes behave
**FIFO**
(First in First out)

**Queue:**
Pipe behave like a data structure.  

**512**
Size of read and write don’t have to match here. We can write 512 bytes at a time but only read  1 byte at a time in a pipe.


### Let`s see this behavior
```
#include <stdio.h> 
#include <unistd.h> 
char* msg1 = "hello, world #1"; 
char* msg2 = "hello, world #2"; 
char* msg3 = "hello, world #3"; 

int main() 
{ 
	char inbuf[16]; 
	int p[2], pid, nbytes; 

	if (pipe(p) < 0) 
		exit(1); 

	// Here we are queuing some mensages
	if ((pid = fork()) > 0) { 
	    close(fd[0]);
		write(p[1], msg1, 16); 
		write(p[1], msg2, 16); 
		write(p[1], msg3, 16); 
		wait(NULL); 
	} 

    // Here we are dequeuing the mensages
	else { 
		close(p[1]); 
		while ((nbytes = read(p[0], inbuf, 16)) > 0) 
			printf("% s\n", inbuf); 
		if (nbytes != 0) 
			exit(2); 
		printf("Finished reading\n"); 
	} 
	return 0; 
} 

```
OUTPUT
```S
hello world, #1
hello world, #2
hello world, #3
(hangs) //program does not terminate but hangs because of the "wait(NULL);"
```


