// Exercice 4:
// 1. Ecrire une fonction int puissance(int a,int b) qui renvoie =a*a*a*a (b fois). 
// 2. Écrire une fonction int somme(int n) qui calcule et renvoie le terme d’indice de la suite :



#include <stdio.h>
#include <stdlib.h>

void cleanCmd(){
#ifdef _WIN32
    system("cls");
#else
    system("clear");
#endif
}

int puissance(int a, int b) {
    if(b==0)return 1;
    int produit = 1;

    for (int i = 0; i < b; i++) {
        produit *= a;
    }

    return produit;
}


int factoriel(int n){
if(n==0)return 1;
int prod=1;
for(int i=1;i<=n;i++)prod*=i;
return prod;
}

int somme(int n){

    int s=0;
    for(int k=0;k<=n;k++)s+=puissance(factoriel(k),3);
    return s;

}

void setAandB(int *t){
  do{
   cleanCmd();
   printf("\nEnter a : ");
   scanf("%d",t);
   printf("\nEnter b: ");
   scanf("%d",t+1);
  }while(*t==0 && *(t+1)==0); // this condition will prevent from 0^0 and 0^negative number
}

int main(){
    int *p=malloc(2*sizeof(int)); // pointer that allocate memory for 2 integers a and b
     printf(" Part 1 : \n\n");
    setAandB(p);
    printf("\n Result : %d ^ %d = %d",*(p),*(p+1),puissance(*(p),*(p+1)));
    free(p);
    printf("\nClick Enter to move : ");
    int c=getchar();
    c=getchar();
    cleanCmd();
    printf("\nPart 2 : \n\n");
    int n;
    do{
        printf("Enter n :");
        scanf("%d",&n);

    }while(n<0);

    printf("\n S(%d) = %d",n,somme(n));






}
