#include <iostream>
using namespace std;

int main() {
    int num, sum = 0;
    cout << "Enter an integer: ";
    cin >> num;

    while (num != 0) {
        int remainder = num % 10;
        sum += remainder;
        num /= 10;
    }

    cout << "Sum of digits = " << sum << endl;
    return 0;
}
