#include<stdio.h>
#include<conio.h>
void main()
{
int a,b,c;
clrscr();
printf("Enter three numbers:");
scanf("%d%d%d",&a,&b,&c);
printf("%d is largest",(a>b)?((a>c)?a:c):((b>c)?b:c));
getch();
}
