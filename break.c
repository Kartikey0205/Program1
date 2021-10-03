#include<stdio.h>
void main()
{
	int i=1;
	for(i;i<=4;i++)
	{
		int j=1;
		for(j;j<=4;j++)
		{
			if((i+j)%4==1)
			   break;
			printf(" ");
		}
		int k=1;
		for(k;k<=4;k++)
		{
			if(k>i)
			   break;
			printf("%d",i);
		}
		printf("\n");
	}
}
