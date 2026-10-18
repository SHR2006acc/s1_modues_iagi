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

N=deleteX(t,N,x);
printf("\nTable after : ");
displayTable(t,N);




free(t);
}
