const {assert} = require('chai');
const lookupChar = require('./char-lookup.js')


describe('check lookupChar function work properly', () => {
    
    it('if first param is not string return undefined', () =>{
        assert.equal(lookupChar(5, 6), undefined);
    })

    it('if second param is not number return undefined', () =>{
        assert.equal(lookupChar("Dog", "Cat"), undefined);
    })

    it('if string length bigger that index', () =>{
        assert.equal(lookupChar("Cat", 15), "Incorrect index");
    })

    it('if index below zero', () =>{
        assert.equal(lookupChar("Cat", -15), "Incorrect index");
    })

    it('return correct char', () =>{
        assert.equal(lookupChar("Cat", 1), "a");
    })

    it('if string length and index is equal return incorrect index', () =>{
        assert.equal(lookupChar("Cat", 3), "Incorrect index");
    })

    it('if index is decimal', () =>{
        assert.equal(lookupChar("Cat", 3.5), undefined);
    })
});