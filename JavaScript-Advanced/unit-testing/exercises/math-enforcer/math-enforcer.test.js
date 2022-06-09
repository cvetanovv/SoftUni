const {assert} = require('chai');
const mathEnforcer = require('./math-enforcer.js')


describe('check mathEnforcer function work properly', () => {
    
    it('check addFive function return num + 5', () =>{
        assert.equal(mathEnforcer.addFive(5), 10);
    })
    it('check addFive function return num + 5 with decimal', () =>{
        assert.equal(mathEnforcer.addFive(5.5), 10.5);
    })
    it('check addFive function return undefined if param not num', () =>{
        assert.equal(mathEnforcer.addFive("hello"), undefined);
    })
    it('check addFive function with negative number', () =>{
        assert.equal(mathEnforcer.addFive(-5), 0);

    })

    it('check subtractTen function return num - 10', () =>{
        assert.equal(mathEnforcer.subtractTen(5), -5);
    })
    it('check subtractTen function return num - 10 with decimal', () =>{
        assert.equal(mathEnforcer.subtractTen(10.5), 0.5);
    })
    it('check subtractTen function return undefined if param not num', () =>{
        assert.equal(mathEnforcer.subtractTen("10.5"), undefined);
    })
    it('check subtractTen function with negative number', () =>{
        assert.equal(mathEnforcer.subtractTen(-5), -15);
    })

    it('check sum function return sum of two params', () =>{
        assert.equal(mathEnforcer.sum(10, 10), 20);
    })
    it('check sum function return sum of two params with decimal numbers', () =>{
        assert.equal(mathEnforcer.sum(10.5, 10.5), 21);
    })
    it('check sum function first param is string, return undefined', () =>{
        assert.equal(mathEnforcer.sum("10", 10), undefined);
    })
    it('check sum function second param is string, return undefined', () =>{
        assert.equal(mathEnforcer.sum(10, "cat"), undefined);
    })
})