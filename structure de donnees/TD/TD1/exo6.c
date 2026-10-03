
// Exercice 6 :
// Écrivez un programme qui affiche un menu et effectue l&#39;opération choisie :
// === CALCULATRICE ===
// 1. Addition
// 2. Soustraction
// 3. Multiplication
// 4. Division
// 5. Quitter
// Votre choix :
// Utilisez switch pour traiter le choix. Gérez la division par zéro.

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
// #include <windns.h>
void clearCmd()
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

void menu(float ans)
{
    printf("Home>Menu");

    printf("\n\n---------------------------------");
    printf("\n| Type [1] For Addition ");
    printf("\n| Type [2] For Soustraction ");
    printf("\n| Type [3] For Multiplication ");
    printf("\n| Type [4] For Division ");
    printf("\n| Type [5] To Reset ANS ");
    printf("\n| Type [6] For EXIT ");
    printf("\n---------------------------------");
    printf("\n|");
    printf("\n|   ANS   :   %f      ", ans);
    printf("\n|");
    printf("\n---------------------------------");
    printf("\n\n->  ");
}

// void clickEnter(){
//     printf("\n\n\n<===-- Click Enter Button --===>");
// int c = getchar();
// c = getchar();
// }

void clickEnter()
{

    printf("\n\n\n<===-- Click Enter Button --===>");
    getchar();
}
void lobby()
{
    printf("Home>");
    printf("\nWelcome To Ht Calculator , where numbers become dream ...");
    printf("\n");
    clickEnter();
}
int fillChoice(float ans)
{ // this function fill the choice variable as output
    int choice;
    do
    {
        clearCmd();
        menu(ans);
        scanf("%d", &choice);
        clearInputBuffer();

    } while (choice != 1 && choice != 2 && choice != 3 && choice != 4 && choice != 5 && choice != 6);
    return choice;
}

int chooseAnsOrNormalOperation(char operation, char *operationName)
{
    int choice;
    do
    {
        clearCmd();
        printf("Home>Menu>%s", operationName);
        printf("\n----------------------------------------------");
        printf("\n| Type [1] For ANS %c b ", operation);
        printf("\n| Type [2] For a %c b ", operation);
        printf("\n----------------------------------------------");
        printf("\n  ->  ");
        scanf("%d", &choice);
        clearInputBuffer();
    } while (choice != 1 && choice != 2);

    return choice;
}

void enterAandB(float *pointer, bool isAns, float ans, bool isDivsion)
{

    if (isAns)
    {
        printf("\n|  Ans     :  %.3f", ans);
        *pointer = ans;
        do
        {
            printf("\n|  Enter b : ");
            scanf("%f", pointer + 1);
            clearInputBuffer();
            if (isDivsion && *(pointer + 1) == 0)
            {
                printf("\n< You can't divide by 0 >");
            }
        } while (isDivsion && *(pointer + 1) == 0);
    }
    else
    {

        printf("\n\n|  Enter a : ");
        scanf("%f", pointer);
        clearInputBuffer();

        do
        {
            printf("\n\n|  Enter b : ");
            scanf("%f", pointer + 1);
            clearInputBuffer();
            if (isDivsion && *(pointer + 1) == 0)
            {
                printf("\n< You can't divide by 0 >");
            }
        } while (isDivsion && *(pointer + 1) == 0);
    }
}

float addition(float *p)
{
    return *p + *(p + 1);
}

float additionPage(float ans)
{
    printf("Home>Menu>Addition");
    int choice = chooseAnsOrNormalOperation('+', "Addition");
    float *tmp = malloc(2 * sizeof(float)); // 1 to store b ; 2 to store a and b
    if (tmp == NULL)
    {
        printf("Memory allocation failed.");
        return ans;
    }
    clearCmd();
    printf("Home>Menu>Addition");
    if (choice == 2)
        enterAandB(tmp, false, ans, false);
    else
        enterAandB(tmp, true, ans, false);
    float result = addition(tmp);
    // printf("\nResult : %.3f + %.3f = %.3f",*tmp,*(tmp+1),result);
    free(tmp);
    clickEnter();
    return result;
}

float soustraction(float *p)
{
    return *p - *(p + 1);
}

float soustractionPage(float ans)
{
    printf("Home>Menu>Soutraction");
    int choice = chooseAnsOrNormalOperation('-', "Soustraction");
    float *tmp = malloc(2 * sizeof(float)); // 1 to store b ; 2 to store a and b
    if (tmp == NULL)
    {
        printf("Memory allocation failed.");
        return ans;
    }
    clearCmd();
    printf("Home>Menu>Soutraction");
    if (choice == 2)
        enterAandB(tmp, false, ans, false);
    else
        enterAandB(tmp, true, ans, false);
    float result = soustraction(tmp);
    // printf("\nResult : %.3f + %.3f = %.3f",*tmp,*(tmp+1),result);
    free(tmp);
    clickEnter();
    return result;
}
float multiplication(float *p)
{
    return (*p) * (*(p + 1));
}

float multiplicationPage(float ans)
{

    printf("Home>Menu>Multiplication");
    int choice = chooseAnsOrNormalOperation('*', "Multiplication");
    float *tmp = malloc(2 * sizeof(float)); // 1 to store b ; 2 to store a and b
    if (tmp == NULL)
    {
        printf("Memory allocation failed.");
        return ans;
    }
    clearCmd();
    printf("Home>Menu>Multiplication");
    if (choice == 2)
        enterAandB(tmp, false, ans, false);
    else
        enterAandB(tmp, true, ans, false);
    float result = multiplication(tmp);
    // printf("\nResult : %.3f + %.3f = %.3f",*tmp,*(tmp+1),result);
    free(tmp);
    clickEnter();
    return result;
}

float division(float *p)
{
    return (*p) / (*(p + 1));
}

float divisionPage(float ans)
{

    printf("Home>Menu>Division");
    int choice = chooseAnsOrNormalOperation('/', "Division");
    float *tmp = malloc(2 * sizeof(float)); // 1 to store b ; 2 to store a and b
    if (tmp == NULL)
    {
        printf("Memory allocation failed.");
        return ans;
    }
    clearCmd();
    printf("Home>Menu>Division");
    if (choice == 2)
        enterAandB(tmp, false, ans, true);
    else
        enterAandB(tmp, true, ans, true);
    float result = division(tmp);
    // printf("\nResult : %.3f + %.3f = %.3f",*tmp,*(tmp+1),result);
    free(tmp);
    clickEnter();
    return result;
}

int main()
{

    lobby();

    int choice;
    float ans = 0;

    do
    {

        choice = fillChoice(ans);
        switch (choice)
        {

        case 1:
            clearCmd();
            ans = additionPage(ans);
            break;
        case 2:
            clearCmd();
            ans = soustractionPage(ans);
            break;
        case 3:
            clearCmd();
            ans = multiplicationPage(ans);
            break;
        case 4:
            ans = divisionPage(ans);
            clearCmd();
            break;
        case 5:
            clearCmd();
            ans = 0;
            break;
        }

    } while (choice != 6);

    return 0;
}
