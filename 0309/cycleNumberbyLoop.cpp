#include <stdio.h>

int get_cycle_number(int n) {
	int length = 1;

	printf("%d ", n);
	while (n != 1) {
		length += 1;
		if (n % 2) {
			n = n * 3 + 1;
			printf("%d ", n);
		}
		else {
			n = n / 2;
			printf("%d ", n);
		}
	}

	printf("\n");
	return length;
}


int main() {
	printf(" ±Ê¿Ã : %d", get_cycle_number(22));

	return 0;
}
