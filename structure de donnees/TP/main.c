
#include <stdio.h>
#include <stdlib.h>


#define max_size 100

void display(int T[],int n){
    printf("Tableau : \n");
for(int i=0 ; i < n ; i++){

    printf("T[%d] = %d",i,T[i]);
    printf("\n");


}



}

void remplir(int T[],int n){

    for(int i=0;i< n ; i++){
             printf("T[%d] = ",i);
             scanf("%d",&T[i]);
    }



}


int insert(int n,int T[],int valeur , int position){

if(max_size<n || position<0 || position>=n){
    return n;
}




for(int i=n;i>position;i--){
    T[i]=T[i-1];


}
T[position]=valeur;
return n+1;



}


int removeByIndex(int n,int T[], int position){

for(int i=position  ;i<n;i++){

    T[i]=T[i+1];

}
T[n-1]=0;
return n-1;



}
int main(){

int T[max_size];
int n;
printf("Enter the size of the table : ");
scanf("%d",&n);
printf("Remplissage");
remplir(T,n);
display(T,n);
printf("Insertion");
n=insert(n,T,20,0);
display(T,n);

int position = 1;
printf("Suprimer");
n = removeByIndex(n,T,position);
display(T,n);



return 0;
}



