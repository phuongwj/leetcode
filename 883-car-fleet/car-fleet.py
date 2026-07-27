class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = sorted(zip(position, speed), key=lambda car:car[0], reverse=True)
        fleet = []

        for i in range(len(cars)):
            remaining_distance = target - cars[i][0] 
            arrival_time = remaining_distance / cars[i][1]

            if fleet:
                top = fleet[-1]
                if arrival_time > top:
                    fleet.append(arrival_time)
            else:
                fleet.append(arrival_time)

        return len(fleet)