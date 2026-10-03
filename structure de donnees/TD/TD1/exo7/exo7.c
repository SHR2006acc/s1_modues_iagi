
// 1. Écrivez un programme qui affiche un triangle d&#39;étoiles de hauteur N.
// Exemple pour N=5 :
// *
// **
// ***
// ****
// *****

// 2. Écrivez un programme qui affiche une pyramide d&#39;étoiles de hauteur N.
// Exemple pour N=5 :
// *
// ***
// *****
// *******
// *********


#include <stdio.h>
#include <stdlib.h>
#include <math.h>




void cleanCmd(){
#ifdef _WIN32
        system("cls");
#else
        system("clear");
#endif

}
void clearInputBuffer(){
    int c;
    while((c = getchar()) != '\n' && c != EOF);
}


void menu(){ // this the menu function
    printf("\n --------------------------------");
    printf("\n|                                |");
    printf("\n| Type [1] : Create Rectangle    |");
    printf("\n| Type [2] : Create Triangle     |");
    printf("\n| Type [3] : Quit                |");
     printf("\n|                                |");
    printf("\n --------------------------------");
}

void clickEnter(){
    printf("\n\n\n<===-- Click Enter Button --===>");
    int c = getchar();
}

int getN(char *type){
int n;
do{
    cleanCmd();
    printf("Menu > %s > ",type);
    printf("\n\nEnter N : ");
    scanf("%d",&n);
    clearInputBuffer();

}while(n<0);
return n;

}
void rectangle(){
int n = getN("Rectangle");

for(int i=0;i<n;i++){

    for(int j=0;j<i+1;j++)printf("* ");

    printf("\n");
}
printf("\n\n");
}

void triangle(){

int n = getN("Triangle");
printf("\n");
  for(int i=0;i<n;i++){
    for( int j=0;j<2*n-1;j++){
        if((j<=i+n-1 && j>= -i+n-1) || i==n-1 )printf("*");
        else printf(" ");
    }
    printf("\n");
  }


}

int main(){

int choice ;

do{ // this big loop to go out of program when to click 5

    do{  // to choose from Menu
        cleanCmd();
        printf("Menu > ");
        printf("\n");
        menu();
        printf("\n\n||");
        scanf("%d",&choice);
        clearInputBuffer();

}while( choice != 1 && choice != 2 && choice != 3 && choice != 4 && choice != 5 );


   switch (choice){
   case 1: // rectangle
       cleanCmd();
       rectangle();
       clickEnter();
       break;

   case 2 : //traingle
       cleanCmd();
       triangle();
       clickEnter();
       break;
   }


}while(choice!=3);

printf("Thanks For the test || ");
}
