import sys

filename = "input.txt"

frequency = 0
runNumber = 1

array_of_frequencies = [0]

def runFrequencyList():
    global frequency
    global array_of_frequencies

    with open(filename) as my_file:
        for line in my_file:
            frequency += int(line)
            if frequency in array_of_frequencies:
                print("Found first repeated frequency: ", frequency)
                sys.exit()
            array_of_frequencies.append(frequency)

while(True):
    print("Run : ", runNumber, " | Frequency Array Size: ", len(array_of_frequencies))
    runFrequencyList()
    runNumber += 1
