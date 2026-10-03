
#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int inputSize(){

int size ;
do{
       printf("Enter the size of the table (None Null Integer ) : ");
       scanf("%d",&size);


}while(size<=0 || size>=100);
return size;
}

void fillTable(int T[],int size){

for(int i=0;i<size;i++){
    printf("\nEnter the value of the %d element : ",i+1);
    scanf("%d",&T[i]);
}
    }

void displayTable(int T[],int size){
  printf("\nTable : ");
for(int i=0;i<size;i++){
    printf("\nT[%d] : %d",i,T[i]);
}

}

int getMin(int T[],int size){
    int min=T[0];
for(int i=0;i<size;i++){
    if(T[i]<min)min = T[i];
}
return min;

}

int getMax(int T[],int size){
    int max=T[0];
for(int i=0;i<size;i++){
    if(T[i]>max)max = T[i];
}
return max;

}


int getOccurence(int T[],int size,int n){
int count = 0;
for(int i=0;i<size;i++){
    if(n== T[i])count++;
}
return count;
}

int main(){
int T[100];
int size = inputSize();
fillTable(T,size);
printf("\n********************\n\n");
displayTable(T,size);
int min = getMin(T,size);
int max = getMax(T,size);
printf("\n max : %d and min : %d",max,min);
int value;
printf("\n\nEnter n for the Occurence : ");
scanf("%d",&value);
int occurence=getOccurence(T,size,value);
if(occurence==0)printf("\n%d doesn t exist on the table",value);
else printf("\n%d  exist on the table : %d times ",value,occurence);
printf("\n\nThanks for the test");
return 0;
}
