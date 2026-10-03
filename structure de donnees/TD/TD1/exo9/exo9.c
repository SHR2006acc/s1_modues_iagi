// Écrivez un programme manipulant des matrices 3×3 :
// 1) Saisit une matrice
// void saisirMatrice(int mat[N][N]);
// 2) Affiche une matrice
// void afficherMatrice(int mat[N][N]);
// 3) Calcule la somme de deux matrices
// void additionMatrices(int A[N][N], int B[N][N], int C[N][N]);
// 4) Calcule la transposée
// void transposer(int mat[N][N], int result[N][N]);
// 5) Calcule la somme de la diagonale principale
// int sommeDiagonale(int mat[N][N]);

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

void cleanCmd()
{
#ifdef _WIN32
    system("cls");
#else
    system("clear");
#endif
}
void clearInputBuffer()
{
    int c;
    while ((c = getchar()) != '\n' && c != EOF)
        ;
}

void saisirMatrice(int mat[][3])
{

    printf("Saisir la matrice 3*3 : \n");

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            printf("\nEnter T[%d][%d] : ", i, j);
            scanf("%d", &mat[i][j]);
        }
    }
}

void afficherMatrice(int mat[][3])
{
    printf("\nMatrice : \n");
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            printf("\n T[%d][%d] : %d ", i, j, mat[i][j]);
        }
    }
}

void afficherFormeMatrice(int mat[][3])
{
    printf("\nMatrice : \n");
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            printf("T[%d][%d]=%d   ", i, j, mat[i][j]);
        }
        printf("\n");
    }
}

void additionMatrices(int A[][3], int B[][3], int C[][3])
{

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            C[i][j] = A[i][j] + B[i][j];
        }
    }
}

int sommeDiagonale(int mat[][3])
{
    int somme = 0;
    for (int i = 0; i < 3; i++)
    {
        somme += mat[i][i];
    }
    return somme;
}

void transposer(int mat[][3], int result[][3])
{
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            result[i][j] = mat[j][i];
        }
    }
}
int main()
{

    int A[3][3];
    printf("Matrice A --");
    saisirMatrice(A); // saisir
    // afficherMatrice(A); // afficher
    afficherFormeMatrice(A);

    // somme de 2 matrice
    int B[3][3];
    printf("\nMatrice B --");
    saisirMatrice(B); // saisir
    // afficherMatrice(B); // afficher
    afficherFormeMatrice(B);

    // somme
    int C[3][3];
    printf("\nLa somme de A et  B : ");
    additionMatrices(A, B, C);
    afficherMatrice(C);

    int result[3][3];
    // transpose
    transposer(A, result);
    printf("\nMatrice A : ");
    afficherFormeMatrice(A);
    printf("\nMatrice transpose de A  : ");
    afficherFormeMatrice(result);

    // somme de diagonale d une matrice
    printf("\nLa somme de la diagonale de A : %d", sommeDiagonale(A));
    printf("\nLa somme de la diagonale de B : %d", sommeDiagonale(B));
    printf("\nLa somme de la diagonale de C : %d", sommeDiagonale(C));
}
