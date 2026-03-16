let a = parseInt(prompt("Enter first number: "));
let b = parseInt(prompt("Enter second number: "));

while (b) {
    let temp = b;
    b = a % b;
    a = temp;
}

console.log("GCD is " + a);
