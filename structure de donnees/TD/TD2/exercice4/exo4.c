#include <stdio.h>
#include <stdlib.h>
#include <math.h>



void fillTable(int **tab,int n,int m){
    printf("\nFILL :  \n");
    for(int i=0;i<n;i++){

            for(int j=0;j<m;j++){
                    printf("\nT[%d][%d] = ",i,j);
                    //scanf("%d",&tab[i]+j);
                    scanf("%d",&tab[i][j]);
            }
}
printf("\nEnd of Fill");

}

void displayTable(int **tab,int n,int m){
    for(int i=0;i<n;i++){
            printf("[");
            for(int j=0;j<m;j++){
                    //printf(" %d ",*(&tab[i]+j));
                    printf(" %d ",tab[i][j]);
            }
            printf("]\n");
}

}

void displayTransposee(int **tab,int n,int m){

    for(int i=0;i<m;i++){
            printf("[");
            for(int j=0;j<n;j++){
                    //printf(" %d ",*(&tab[i]+j));
                    printf(" %d ",tab[j][i]);
            }
            printf("]\n");
}


}

void displayUni(int **tab, int n, int m) {
    printf("\nA = { ");

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            printf("%d", tab[i][j]);

            if (i != n - 1 || j != m - 1)
                printf(", ");
        }
    }

    printf(" }\n");
}

int allocateMemory(int ***tab, int n, int m) {
    *tab = malloc(n * sizeof(int *));

    if (*tab == NULL)
        return 0;

    for (int i = 0; i < n; i++) {
        (*tab)[i] = malloc(m * sizeof(int));

        if ((*tab)[i] == NULL) {
            for (int j = 0; j < i; j++)
                free((*tab)[j]);

            free(*tab);
            *tab = NULL;
            return 0;
        }
    }

    return 1;
}




int main(void) {

    int n, m;
    int **tab = NULL;

    printf("N (number of rows): ");
    scanf("%d", &n);

    printf("M (number of columns): ");
    scanf("%d", &m);

    if (n <= 0 || m <= 0) {
        printf("Invalid dimensions.\n");
        return 1;
    }

    if (!allocateMemory(&tab, n, m)) {
        printf("Memory allocation failed.\n");
        return 1;
    }

    fillTable(tab, n, m);

    printf("\nMatrix A:\n");
    displayTable(tab, n, m);

    printf("\nTranspose of A:\n");
    displayTransposee(tab, n, m);

    printf("\nUnidimensionel  A:\n");
    displayUni(tab, n, m);

    for (int i = 0; i < n; i++)
        free(tab[i]);

    free(tab);

    return 0;
}
