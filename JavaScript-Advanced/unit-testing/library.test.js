const {expect} = require('chai');
const library = require('./library.js')

describe('Library tests', () => {

    describe('calcPriceOfBook tests', () => {

        it('invalid input - name of the book', () => {
            expect(() => library.calcPriceOfBook(1, 1980)).to.throw("Invalid input");
        })
        it('invalid input - year of the book', () => {
            expect(() => library.calcPriceOfBook("Harry Potter", "Art of coding")).to.throw("Invalid input");
        })
        it('calc year < 1980', () => {
            expect(library.calcPriceOfBook('my book', 1900)).to.equal('Price of my book is 10.00');
        })
        it('calc year = 1980', () => {
            expect(library.calcPriceOfBook('my book', 1980)).to.equal('Price of my book is 10.00');
        })
        it('calc year > 1980', () => {
            expect(library.calcPriceOfBook('Harry Potter', 1998)).to.equal('Price of Harry Potter is 20.00');
        })
    })

    describe('findBook tests', () => {

        it('check empty arr', () => {
            expect(() => library.findBook([], "Invisible Man")).to.throw("No books currently available");
        })
        it('valid input - available book', () => {
            expect(library.findBook(["Troy", "Life Style"], "Troy")).to.equal("We found the book you want.");
        })
        it('valid input - not available book', () => {
            expect(library.findBook(["Troy", "Life Style"], "Invisible Man")).to.equal("The book you are looking for is not here!");
        })
    })

    describe('arrangeTheBooks', () => {
        it('check invalid input - string', () => {
            expect(() => library.arrangeTheBooks('abc')).to.throw("Invalid input");
        })
        it('check invalid input - negative number', () => {
            expect(() => library.arrangeTheBooks(-5)).to.throw("Invalid input");
        })
        it('check enough space', () => {
            expect(library.arrangeTheBooks(40)).to.equal("Great job, the books are arranged.");
        })
        it('check not enough space', () => {
            expect(library.arrangeTheBooks(41)).to.equal("Insufficient space, more shelves need to be purchased.");
        })
    })
})