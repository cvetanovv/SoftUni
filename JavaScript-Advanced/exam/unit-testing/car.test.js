const {expect} = require('chai');
const carService = require('./car_service.js')

describe('Car Service tests', () => {

    describe('isItExpensive tests', () => {

        it('Test issue = Engine error', () => {
            expect(carService.isItExpensive('Engine')).to.equal("The issue with the car is more severe and it will cost more money");
        })
        it('Test issue = Transmission error', () => {
            expect(carService.isItExpensive('Transmission')).to.equal("The issue with the car is more severe and it will cost more money");
        })
        it('Test other issues', () => {
            expect(carService.isItExpensive('Oil')).to.equal("The overall price will be a bit cheaper");
        })
    })

    describe('discount tests', () => {
        it('Test number of parts is not a number', () => {
            expect(() => carService.discount("hello", 2000)).to.throw("Invalid input");
        })
        it('Test price is not a number', () => {
            expect(() => carService.discount(5, "Glass")).to.throw("Invalid input");
        })
        it('Test parts > 2 and parts <= 7', () => {
            expect(carService.discount(7, 100)).to.equal("Discount applied! You saved 15$");
        })
        it('Test parts over 7', () => {
            expect(carService.discount(10, 100)).to.equal("Discount applied! You saved 30$");
        })
        it('Test parts below 2', () => {
            expect(carService.discount(1, 100)).to.equal("You cannot apply a discount");
        })
    })

    describe('partsToBuy tests', () => {
        it('Test catalog is not array', () => {
            expect(() => carService.partsToBuy("hello", ['test', 'engine'])).to.throw("Invalid input");
        })
        it('Test catalog is not array', () => {
            expect(() => carService.partsToBuy(["hello"], 'test')).to.throw("Invalid input");
        })
        it('Test total sum', () => {
            let car = {part: "tyre", price: 10}
            expect(carService.partsToBuy([car], ["tyre"])).to.equal(10);
        })
        it('Test empty catalog', () => {
            let car = {part: "tyre", price: 10}
            expect(carService.partsToBuy([], ["tyre"])).to.equal(0);
        })


    })
})