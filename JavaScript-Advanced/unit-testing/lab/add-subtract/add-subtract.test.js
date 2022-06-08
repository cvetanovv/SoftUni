const {expect} = require('chai');
const createCalculator = require('./add-subtract');

describe('Function work properly', () => {
    it('return object', () =>{
        expect(typeof createCalculator()).to.equals('object');
    })

    it('get function return internal sum', () =>{
        expect(createCalculator().get()).to.equal(0);
    })

    it('subtract method subtracts parsable input', () => {
        const calc = createCalculator()
        calc.add('2')
        calc.subtract('1')
        expect(calc.get()).to.equals(1)
    })

    it("should return 3 after add(10); subtract('7'); add('-2'); subtract(-1)", function () {
        let calculator = createCalculator();

        calculator.add(10);
        calculator.subtract('7');

        expect(calculator.get()).to.equal(3);
    });

    it("should return -1 add('-2'); subtract(-1)", function () {
        let calculator = createCalculator();

        calculator.add('-2');
        calculator.subtract(-1);

        expect(calculator.get()).to.equal(-1);
    });
})