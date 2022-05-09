function solve(arr){
    let sortedNumbers = arr.sort((a, b) => a - b);
    let twoNumbers = sortedNumbers.slice(0, 2);
    console.log(twoNumbers.join(' '))
}

solve([30, 15, 50, 5])