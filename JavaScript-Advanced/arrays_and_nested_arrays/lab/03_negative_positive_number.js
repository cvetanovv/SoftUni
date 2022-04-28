function solve(arr) {
    result = [];

    for (const num of arr) {
        if (num < 0){
            result.unshift(num);
        }else{
            result.push(num);
        }
    }

    for (const n of result) {
        console.log(n);
    }
}