import math

filename = "day2/input.txt"
ranges = []
count = 0


def get_factors(n):
    pairs = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            pairs.append((i, n // i))
            pairs.append((n // i, i))
    return pairs


def checkForDupesInList(list, lookup):
    for item in list:
        if item == lookup:
            return True
    return False


def main():
    global count
    try:
        with open(filename, "r") as file:
            # file is a long line, store each range where they are denoted at each comma
            line = file.readline().strip()
            for r in line.split(","):
                ranges.append(r)
    except FileNotFoundError:
        print(f"Error: The file at {filename} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    for rangeID in ranges:
        lower, upper = map(int, rangeID.split("-"))
        for num in range(lower, upper + 1):
            numString = str(num)
            if len(numString) % 2 == 1:  # odd length number
                continue
            elif len(numString) % 2 == 0:  # even length number
                mid = len(numString) // 2
                firstHalf = numString[:mid]
                secondHalf = numString[mid:]
                if firstHalf == secondHalf:
                    count += num

    print(f"Part 1: {count}")

    # part 2
    count = 0
    invalidIDs = set()
    for rangeID in ranges:
        lower, upper = map(int, rangeID.split("-"))
        for num in range(lower, upper + 1):
            factors = get_factors(len(str(num)))
            numString = str(num)
            for factorPair in factors:
                group, repetition = factorPair
                if repetition == 1:
                    continue
                numLookup = numString[0:group]
                constructedNum = numLookup * repetition
                if constructedNum == numString:
                    invalidIDs.add(num)

    for IDs in invalidIDs:
        count += IDs
    print(f"Part 2: {count}")


if __name__ == "__main__":
    main()
