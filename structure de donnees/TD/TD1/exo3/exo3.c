#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define max_size 100


void cleanCmd(){
#ifdef _WIN32
        system("cls");
#else
        system("clear");
#endif

}

void menu(){ // this the menu function

    printf("\n| Type [1] : Fill Table");
    printf("\n| Type [2] : Display Table");
    printf("\n| Type [3] : Insert By Index");
    printf("\n| Type [4] : Delete By Index ");
    printf("\n| Type [5] : Sortie");

}

void clickEnter(){
    printf("\n\n\n<===-- Click Enter Button --===>");
    int c = getchar();
    c = getchar();
}

int inputSize(){ // size function

int size ;
do{
       printf("Enter the size of the table (None Null Integer ) : ");
       scanf("%d",&size);


}while(size<=0 || size>max_size);
return size;
}

void fillTable(int T[],int size){ // this function fill the table

for(int i=0;i<size;i++){
    printf("\nEnter T[%d] : ",i);
    scanf("%d",&T[i]);
                   }
    }

void displayTable(int T[],int size){ //this function display the table
  printf("Table : ");
for(int i=0;i<size;i++){
    printf("\nT[%d] : %d",i,T[i]);
}

}

int insertTable(int T[], int size, int valeur, int position){

 if(size>=max_size || position < 0 || position > size)return size;

  for(int i=size-1;i>=position;i--){
    T[i+1]=T[i];
  }

  T[position]=valeur;

  return size+1;
}


void fillNewInsert(int *tmp){
printf("\nEnter the index : ");
scanf("%d",(tmp+0));

printf("\nEnter the value : ");
scanf("%d",(tmp+1));
}


int deleteTable(int T[],int size,int position){

    if(position < 0 || position >= size)return size;

    for(int i=position;i<size-1;i++){
        T[i]=T[i+1];
    }

    return size-1;
}


int fill_delPos(){
int position;

printf("\nEnter the index : ");
scanf("%d",&position);

return position;
}




int main(){
int T[max_size];

int choice ;
int size = inputSize();

do{ // this big loop to go out of program when to click 5



    do{  // to choose from Menu
        cleanCmd();
        menu();
        printf("\n\n||");
        scanf("%d",&choice);

}while( choice != 1 && choice != 2 && choice != 3 && choice != 4 && choice != 5 );


   switch (choice){
   case 1:
       cleanCmd();
       fillTable(T,size);
       clickEnter();
       break;

   case 2 :
       cleanCmd();
       displayTable(T,size);
       clickEnter();
       break;

   case 3 :
       cleanCmd();
       int *tmp = malloc(2*sizeof(int));

       if (tmp == NULL) {
               printf("Memory allocation failed.\n");
               break;
                      }

       fillNewInsert(tmp);

       size=insertTable(T,size,*(tmp+1),*(tmp+0));

       free(tmp);

       clickEnter();
       break;

   case 4:
       cleanCmd();

       int position = fill_delPos();

       size = deleteTable(T,size,position);

       clickEnter();
       break;
   }



}while(choice!=5);

printf("\n\n\n<===-- Thank You For Using This Program --===>\n\n\n");

}