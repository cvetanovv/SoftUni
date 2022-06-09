const {assert} = require('chai');
const isOddOrEven = require('./even-or-odd.js')


describe('check isOddOrEven function work properly', () => {
    
    it('if not a string return undefined', () =>{
        assert.equal(isOddOrEven(5), undefined)
    })

    it('if string is odd', () =>{
        assert.equal(isOddOrEven("Hello"), "odd")
    })

    it('if string is even', () =>{
        assert.equal(isOddOrEven("Hi"), "even")
    })
})