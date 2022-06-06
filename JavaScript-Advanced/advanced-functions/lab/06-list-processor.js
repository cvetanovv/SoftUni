function solution(arr) {
    let collections = [];

    arr.forEach(x => {
        let touple = x.split(' ');
        let command = touple[0];

        if (command === 'print'){
            console.log(collections.join(','))
        }

        let word = touple[1];

        if (command === 'add'){
            collections.push(word);
        } else if (command === 'remove') {
            collections = collections.filter(function(x) {
                return x !== word;
            })
        }
        
    })
}



let array = solution(['add hello', 'add again', 'remove hello', 'add again', 'print'])