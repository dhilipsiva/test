/*
 * function-experiment.c
 * Copyright (C) 2015 dhilipsiva <dhilipsiva@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include<stdio.h>

int sum(int a, int b) {
    return a + b;
}

int main() {
    /*
     * The `sum` function cannot be declared here.
     * */
    printf("Hello World\n");
    printf("Sum: %d\n", sum(5, 3));
    return 0;
}
