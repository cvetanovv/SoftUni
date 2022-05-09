function solve(arr) {
    let result = 0;
    let firstNum = Number(arr.shift());
    let lastNum = Number(arr.pop());
    result = firstNum + lastNum;
    return result;
}