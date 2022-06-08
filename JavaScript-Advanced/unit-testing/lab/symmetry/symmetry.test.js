const { isSymmetric } = require("./symmetry");
const {expect} = require('chai');


describe('Symmetry Checker', () => {
    it('works with symmetric array', () =>{
        expect(isSymmetric([1,2,2,1])).to.be.true;
    })

    it('retuns false for non-symmetric', () =>{
        expect(isSymmetric([1,2,3])).to.be.false;
    })

    it('no array', () =>{
        expect(isSymmetric(10)).to.be.false;
    })

    it('it works with odd array', () =>{
        expect(isSymmetric([1,2,1])).to.be.true;
    })

    it('it not works with string number', () =>{
        expect(isSymmetric([1,2,"1"])).to.be.false;
    })
})