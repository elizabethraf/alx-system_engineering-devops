#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
* infinite_while - check the code
*
* Return: void
**/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
* main - check the code
*
* Return: void
**/
int main(void)
{
	pid_t zombie = fork();
	int k;

	for (k = 0; k < 5; k++)
	{

	if (zombie > 0)
		sleep(1);

	else
		printf("Zombie process created, PID: %i\n", getpid());
		exit(0);
	k += 1;
	}
	return (0);
}
