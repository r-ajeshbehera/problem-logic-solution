let num = parseInt(prompt("Enter an integer: "));
let reversed = 0;

while (num != 0) {
    let remainder = num % 10;
    reversed = reversed * 10 + remainder;
    num = Math.floor(num / 10);
}

console.log("Reversed number =", reversed);
