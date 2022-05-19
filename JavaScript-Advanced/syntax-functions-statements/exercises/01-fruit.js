function fruit(fruit, grams, pricePerKg){
    let weight = (grams / 1000).toFixed(2);
    let money = ((grams * pricePerKg) / 1000).toFixed(2)

    return `I need \$${money} to buy ${weight} kilograms ${fruit}.`
}

console.log(fruit('apple', 1563, 2.35))