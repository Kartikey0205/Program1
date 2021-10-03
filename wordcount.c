#include<stdio.h>
#include<string.h>
void main()
{
	char s1[40],s2[40];int i,c=0;
	gets(s1);
	gets(s2);
	for(i=0;i<strlen(s1);i++)
	{
	    if(s1[i]==s2[i])
		  c++;
		else if(s1[i]>s2[i])
		{
			printf(" s1 > s2");
			break;
		}		 
		else
		{
			printf("s1<s2");
			break;
	    } 
	}
	if(c==strlen(s1))
	 printf(" s1 = s2");
}

