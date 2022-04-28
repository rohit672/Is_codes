#include <stdio.h>
#include <string.h>

int main(void)
{
    char buff[15];
    int pass = 0;

    printf("\nEnter the password :");
    gets(buff);

    if(strcmp(buff, "password"))
    {
        printf ("Wrong Password \n");
    }
    else
    {
        printf ("Correct Password \n");
        pass = 1;
    }

    if(pass)
    {
        printf ("You are logged in as an administrator\n");
    }

    return 0;
}
