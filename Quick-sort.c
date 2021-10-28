#include<stdio.h>
#include<stdlib.h>
int partition(int[],int,int);
void quicksort(int[],int,int);

void main()
{
  int lower=0,i,upper;
  int a[]={10,6,3,67,5,9};
  int element;
  element=sizeof(a)/sizeof(int);
  upper=element-1;
  printf("\n before sorting array:\n");
  for(i=lower;i<=upper;i++)
  printf("%4d",a[i]);
  quicksort(a,lower,upper);
  printf("\n after sorting array:\n");
  for(i=lower;i<=upper;i++)
  printf("%4d",a[i]);
}
void quicksort(int b[],int l,int u)
{
  int j;
  if(l<u)
  {
    j=partition(b,l,u);
    quicksort(b,l,j-1);
    quicksort(b,j+1,u);
  }
}
int partition(int a[],int l,int u)
{
  int pivot,i,j,temp;
  pivot=a[l];
  i=l+1;
  j=u;
  while(i<j)
  {
    while(pivot>a[i])
    i++;
    while(pivot<a[j])
    j--;
    if(i<j)
    {
      temp=a[i];
      a[i]=a[j];
      a[j]=temp;
    }
  }
  temp=a[l];
  a[l]=a[j];
  a[j]=temp;
  return j;
}
