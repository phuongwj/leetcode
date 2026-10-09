class Solution:
    def convertToMinutes(self, time: str) -> int:
        timeSeparate = time.split(":")

        time1 = int(timeSeparate[0])
        time2 = int(timeSeparate[1])

        timeMinute = (time1 * 60) + time2

        return timeMinute

    def alertNames(self, keyName: list[str], keyTime: list[str]) -> list[str]:
        nKeys = len(keyName)
        storage = {}

        # put all times in names for dictionary
        for i in range(nKeys):
            if keyName[i] not in storage:
                timeMinute = self.convertToMinutes(keyTime[i])
                storage[keyName[i]] = [timeMinute]
            else:
                timeMinute = self.convertToMinutes(keyTime[i])
                storage[keyName[i]].append(timeMinute)
        
        output = set()

        # sort the minutes
        for name in keyName:
            storage[name].sort()

            for i in range(2, len(storage[name])):
                subtraction = storage[name][i] - storage[name][i-2]
                if subtraction <= 60:
                    output.add(name)

        # sort the output
        output = list(output)
        outputSorted = sorted(output)
        return outputSorted