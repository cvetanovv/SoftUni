function sameNumbers(num){
    let number = num.toString();
    let result = 0
    let bool = true;
    for (let index = 1; index < number.length; index++) {
        if (number[index] !== number[index - 1]){
            bool = false;
            break;
        }       
    }
    for (let index = 0; index < number.length; index++) {
        result += parseInt(number[index]);
    }
    console.log(bool)
    console.log(result)
}

sameNumbers(2222222)