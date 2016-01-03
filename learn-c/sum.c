/*
 * sum.c
 * Copyright (C) 2016 dhilipsiva <dhilipsiva@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */
#include <stdio.h>

int sum(int num1, int num2){
	return num1 + num2;
}

int main(int argc, const char *argv[])
{
	printf("Sum: %d", sum(4, 5));
	return 0;
}
