function string_Length(arg1, arg2, arg3) {
    let sumLength;
    let averageLength;

    let firstArgLength = arg1.length;
    let secondArgLength = arg2.length;
    let thirdArgLength = arg3.length;

    sumLength = firstArgLength + secondArgLength + thirdArgLength;
    averageLength = sumLength / 3;

    console.log(sumLength);
    console.log(Math.floor(averageLength));
}