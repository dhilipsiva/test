#include <stdio.h>

int main() {
    char *name;
    printf("Please enter your name: ");
    scanf(&name);
    printf("Hello %s, welcome!\n", &name);
}
