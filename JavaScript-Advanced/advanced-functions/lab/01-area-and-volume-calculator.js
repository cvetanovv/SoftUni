function areaVol(areaIn, volIn, input) {
    const data = JSON.parse(input);

    const result = [];

    for (let cube of data) {
        const current = {
            area: areaIn.call(cube),
            volume: volIn.call(cube)
        }

        result.push(current);
    }

    return result;
}