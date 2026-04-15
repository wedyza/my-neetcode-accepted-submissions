class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = [(position[i], speed[i]) for i in range(n)]
        cars.sort()
        if n == 0:
            return 0
        stack = [[n-1]]
        fleet_start = cars[n-1][0]
        fleet_speed = cars[n-1][1]
        print(cars)
        for i in range(n-2, -1, -1):
            start = cars[i][0]
            speed = cars[i][1]
            
            fleet = stack[-1]
            leader_start = cars[fleet[0]][0]
            leader_speed = cars[fleet[0]][1]

            if leader_start == start:
                fleet.append(i)
                continue

            if leader_speed < speed:
                if (leader_start - start) / (speed - leader_speed) <= (target - leader_start) / leader_speed:
                    fleet.append(i)
                else:
                    stack.append([i])
            else:
                stack.append([i])
        print(stack)
        return len(stack)