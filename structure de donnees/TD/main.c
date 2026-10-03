
#include <stdio.h>
#include <stdlib.h>



int main(){
  int L,l;
  printf("Enter l : ");
  scanf("%d",&l);

  int i,j;
  for( i=0;i<l;i++){
    for( j=0;j<l;j++){
        if((j<=i+2 && j>= -i+2) || i==l-1 )printf("* ");
        else printf("  ");
    }
    printf("\n");
  }

return 0;
}



