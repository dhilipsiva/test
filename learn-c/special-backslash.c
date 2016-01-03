/*
 * special-backslash.c
 * Copyright (C) 2016 dhilipsiva <dhilipsiva@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <stdio.h>

int main(int argc, const char *argv[])
{
	printf("backspace:bs\b\b");
	printf("form feed:\f");
	printf("new line:\ncont1");
 	printf("return:\rcont2");
	printf("horizontal tab:\tcont3");
	printf("\"Double Quotes\"");
	printf("\'Single Quote\'");
	printf("\\Back Slash\\");
	printf("vertical\vtab");
	printf("\aalert");
	printf("question mark\?");
	return 0;
}
