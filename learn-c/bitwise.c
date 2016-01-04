/*
 * bitwise.c
 * Copyright (C) 2016 dhilipsiva <dhilipsiva@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <stdio.h>

int sum(int a, int b)
{
	return a + b;
}


int main(int argc, const char *argv[])
{
	int a = 3;
	printf("%d", sum(a << a, a));
	return 0;
}
