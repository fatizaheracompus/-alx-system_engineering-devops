#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <sys/wait.h>

/**
 * infinite_while - Rune infinite while loop.
 *
 * Return: Alway 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Creates 5 zombie processes.
 *
 * Return: Alway 0.
 */
int main(void)
{
	pid_t pidz;
	char cnt = 0;

	while (cnt < 5)
	{
		pidz = fork();
		if (pidz > 0)
		{
			printf("Zombie process created, PID: %d\n", pidz);
			sleep(1);
			cnt++;
		}
		else
			exit(0);
	}

	infinite_while();

	return (EXIT_SUCCESS);
}
