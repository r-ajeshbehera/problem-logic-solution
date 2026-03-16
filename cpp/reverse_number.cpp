#include <iostream>
using namespace std;

int main() {
    int num, reversed = 0;
    cout << "Enter an integer: ";
    cin >> num;

    while (num != 0) {
        int remainder = num % 10;
        reversed = reversed * 10 + remainder;
        num /= 10;
    }

    cout << "Reversed number = " << reversed << endl;
    return 0;
}
