#include <stdio.h>

int length = 1;

int get_cycle_number(int n) {
	
	printf("%d ", n);

	if (n == 1) {
		return length;
	}

	length += 1;

	if (n % 2) {
		get_cycle_number(n * 3 + 1);
	}
	else {
		get_cycle_number(n / 2);
	}
}

int main() {
	printf(" ±Ê¿Ã : %d", get_cycle_number(22));

	return 0;
}
