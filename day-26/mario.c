// Makes mario's pyramid - exercise for CS50 - Pset1
#include <stdio.h>
#include <cs50.h>
int n;

int main(void)
{
    do
    {
        printf("How tall should the pyramid be?[0-23]");
        n = get_int();
    }
    while (n < 0 || n > 23);
    // This is for each row of the pyramid
    for (int i = 0; i < n; i++)
    {
        // Add empty spaces in front of the #
        for(int j = 0; j < n-i-1; j++)
        {
            printf("%s", " ");
        }

        for(int k = 0; k < i+2; k++)
    		{
    			printf("#");
    		}
	printf("\n");
    }

}