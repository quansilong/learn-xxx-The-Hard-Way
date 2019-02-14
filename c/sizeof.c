#include<stdio.h>

int main()
{
    printf("int  : %lu \n", sizeof(int));
    printf("long int  : %lu \n", sizeof(long int));
    printf("int  : %lu \n", sizeof( __INT16_MAX__ ), __INT16_MAX__);
    

    printf("int  : %lu \n", __INT32_MAX__);

    return 0;

}
