#include <stdio.h>
#include <stdlib.h>
#include <math.h>


void fillTable(int *t,int N){
printf("\nFILL :  \n");
for(int i=0;i<N;i++){
    printf("T[%d] = ",i);
    scanf("%d",t+i);
}
printf("\nFIN REMPLISSAGE");

}

void displayTable(int *t,int N){
    printf("\nDisplay :  \n");
for(int i=0;i<N;i++){
    printf("\nT[%d] = %d",i,*(t+i));
}


}

int deleteX(int *t,int taille,int x){ // here p1 = t
int *p1 = t ;
int *p2 = p1 + 1;
for(int i=0;i<taille;i++){

    if(*(t+i)==x){
            for(int j = i;j<taille-1;j++){
                 *(p1+j)=*(p2+j);
            }
    taille--;
    }
}
return taille;

}


void swap(int *a,int *b){
int tmp = *a;
*a = *b;
*b = tmp;
}
int triBulle(int *t,int taille){
    int *p1,*p2;
    for(int i=0;i<taille;i++){
        p1=t;
        p2=p1+1;
        for(int j=0;j<i-1;j++){
                if(*p1>*p2)swap(p1,p2);
               p1++;
               p2++;
        }
    }
}




int main(){
int N;


printf("Enter N : ");
scanf("%d",&N);
int *t = malloc(N*sizeof(int*));

fillTable(t,N);
int x;
printf("\nEnter  X  : ");
scanf("%d",&x);

printf("\nTable before : ");
displayTable(t,N);

triBulle(t,N);
printf("\nTable after : ");
displayTable(t,N);




free(t);
}
