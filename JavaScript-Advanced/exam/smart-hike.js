class SmartHike {
    constructor(username) {
        this.username = username
        this.goals = {}
        this.listOfHikes = []
        this.resources = 100
    }

    addGoal(peak, altitude) {
        if(peak in this.goals){
            return `${peak} has already been added to your goals`
        } 
        this.goals[peak] = altitude
        return `You have successfully added a new goal - ${peak}`
    }

    hike (peak, time, difficultyLevel) {
        if(!(peak in this.goals)) {
            throw new Error(`${peak} is not in your current goals`);
        }
        if (this.resources === 0) {
            throw new Error("You don't have enough resources to start the hike")
        }

        let difference = this.resources -= (time * 10)
        if(difference < 0) {
            return "You don't have enough resources to complete the hike";
        }
        
        let hike = {
            peak,
            time,
            difficultyLevel
        }

        this.listOfHikes.push(hike);

        return `You hiked ${peak} peak for ${time} hours and you have ${this.resources}% resources left`
    }

    rest (time) {
        this.resources += (time * 10);
        if (this.resources >= 100){
            this.resources = 100
            return `Your resources are fully recharged. Time for hiking!`
        }

        return `You have rested for ${time} hours and gained ${time *10 }% resources`
    }

    showRecord (criteria) {
        if (this.listOfHikes.length === 0) {
            return `${this.username} has not done any hiking yet`;
        }

        if (criteria === "all") {
            let result = ["All hiking records:",]
            this.listOfHikes.forEach(x => result.push(`${this.username} hiked ${x.peak} for ${x.time} hours`))
            return result.join('\n')
        }
    }
}
