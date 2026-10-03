// Écrire une fonction qui retourne le nombre de chiffres d’un entier positif.


#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int CalDigits(int n){
int count = 0;
if(n==0)return 1;
while(n !=0 ){

    n = n / 10;
    count ++;


}
return count;

}
int main(){

int n;


do{
        printf("Enter Number  : ");
        scanf("%d",&n);
    
}while(n<0);


int numberOfDigits = CalDigits(n);
printf("\nNumber of digits : %d",numberOfDigits);

printf("\n\n\n<===-- Thank You For Using This Program --===>\n\n\n");
return 0;
}

