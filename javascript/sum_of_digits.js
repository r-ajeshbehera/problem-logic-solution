let num = parseInt(prompt("Enter an integer: "));
let sumOfDigits = 0;

while (num != 0) {
    sumOfDigits += num % 10;
    num = Math.floor(num / 10);
}

console.log("Sum of digits =", sumOfDigits);
