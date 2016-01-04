/*
 * bitwise.c
 * Copyright (C) 2016 dhilipsiva <dhilipsiva@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <stdio.h>

int main(int argc, const char *argv[])
{
	int a = 3;
	a = a << a;
	printf("%d", a);
	return 0;
}
