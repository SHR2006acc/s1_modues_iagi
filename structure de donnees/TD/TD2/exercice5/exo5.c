#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct
{
    int Num;
    int Den;

} NbrRationnel;

void AfficherRationnel(NbrRationnel r)
{
    printf("%d/%d", r.Num, r.Den);
}

int ComparerRationnel(NbrRationnel r1, NbrRationnel r2)
{
    int Num1, Num2;
    if (r1.Den == r2.Den)
    {
        Num1 = r1.Num;
        Num2 = r2.Num;
    }
    else
    {

        Num1 = r1.Num * r2.Den;
        Num2 = r2.Num * r1.Den;
    }
    if (Num1 > Num2)
        return 1;
    else if (Num1 < Num2)
        return -1;
    return 0;
}

void SommeRationnel(NbrRationnel r1, NbrRationnel r2)
{
    NbrRationnel r;
    if (r1.Den == r2.Den)
    {
        r.Den = r1.Den;
        r.Num = r1.Num + r2.Num;
    }
    else
    {
        r.Den = r1.Den * r2.Den;
        r.Num = r1.Num * r2.Den + r2.Num * r1.Den;
    }
    printf("\n");
    AfficherRationnel(r1);
    printf(" + ");
    AfficherRationnel(r2);
    printf(" = ");
    AfficherRationnel(r);
    printf("\n");
}

void PlusPetitRationnel(NbrRationnel t[], int N)
{

    NbrRationnel min;
    min.Num = t[0].Num;
    min.Den = t[0].Den;
    for (int i = 1; i < N; i++)
    {
        if (ComparerRationnel(min, t[i]) == 1)
        {
            min.Den = t[i].Den;
            min.Num = t[i].Num;
        }
    }
    printf("\n The smallest Rationnel : ");
    AfficherRationnel(min);
}

int main(void)
{

    NbrRationnel t1[] = {{12, 7}, {8, 13}, {14, 2}, {1, 9}, {2, 3}};
    printf("\nAffichage :");
    for (int i = 0; i < 5; i++)
    {
        printf("\n t[%d] : ", i);
        AfficherRationnel(t1[i]);
    }

    PlusPetitRationnel(t1, 5);

    return 0;
}
