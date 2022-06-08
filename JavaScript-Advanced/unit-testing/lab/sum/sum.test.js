const {expect} = require('chai');
const {sum} = require('./sum');


describe('Test sum function', () => {
    it('sums multiple numbers', () => {
        expect(sum([1, 2])).to.equal(3);
    });

    it('sums single number', () => {
        expect(sum([1])).to.equal(1);
    });

    it('not take string', () => {
        expect(isNaN(sum([1, 2, 'abc']))).to.equal(true);
    });
})