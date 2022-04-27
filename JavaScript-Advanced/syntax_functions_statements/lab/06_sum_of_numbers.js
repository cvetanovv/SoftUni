function solve(num1, num2) {
    let firstNum = Number(num1);
    let secondNum = Number(num2);
    let result = 0

    for (let i = firstNum; i <= secondNum; i++) {
        result += i;
    }
    return result;
}

console.log(solve('1', '5'))