#include <stdio.h>

// Rudimentary Triple integral calculator
// By Michael Scafe
// 2022-12-27, still lacks support for variables and more complicated functions. 

int area(int a, int b, int c)
{
	int soln = 0;
	soln = (c * b) - (c * a);

	return soln;
}

int main(int argc, char* argv[])
{
	char ticker[20];
	int coefficient = 0;
	int original = coefficient;
	int variable = 0;
	int ab0 = 0;
	int ab1 = 0;
	int cd0 = 0;
	int cd1 = 0;
	int ef0 = 0;
	int ef1 = 0;
	printf("Hello, world! Please enter a number to integrate: ");
	scanf_s("%d", &coefficient);
	original = coefficient;
	printf("\nYou entered %d", coefficient);
	printf("\nPlease enter [a,b]: ");
	scanf_s("%d %d", &ab0, &ab1);
	coefficient = area(ab0, ab1, coefficient);
	printf("\nStep: %d", coefficient);
	printf("\nPlease enter [c,d]: ");
	scanf_s("%d %d", &cd0, &cd1);
	coefficient = area(cd0, cd1, coefficient);
	printf("\nStep: %d", coefficient);
	printf("\nPlease enter [e,f]: ");
	scanf_s("%d %d", &ef0, &ef1);
	coefficient = area(ef0, ef1, coefficient);
	printf("\nStep: %d", coefficient);
	printf("\nIntegral is: /// %d dx over [%d,%d] x [%d,%d] x [%d,%d]",original,ab0,ab1,cd0,cd1,ef0,ef1);
	printf("\n\nThe final answer (area) is: %d", coefficient);
	printf("\nThank you for using Triple Integrals.");
	return 0;
}