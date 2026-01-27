# global var
file_path = "day1/input.txt"
directions = []
currentPos = 50
password = 0


# main function
def main():
    global currentPos, password
    try:
        with open(file_path, "r") as file:
            for line in file:
                directions.append(line.strip())
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    for direction in directions:
        if direction[0] == "L":
            currentPos -= int(direction[1:]) % 100
            if currentPos < 0:
                currentPos = 100 + currentPos
        elif direction[0] == "R":
            currentPos += int(direction[1:]) % 100
            if currentPos > 99:
                currentPos = currentPos - 100
        if currentPos == 0:
            password += 1

    print(f"Part 1: {password}")

    # reset for part 2
    currentPos = 50
    password = 0
    for direction in directions:
        if direction[0] == "L":
            ticks = int(direction[1:])
            while ticks > 100:
                ticks -= 100
                password += 1
            if currentPos - ticks > 0:
                currentPos -= ticks
            elif currentPos - ticks < 0:
                if currentPos == 0:
                    currentPos = 100 - ticks
                    continue
                elif currentPos != 0:
                    currentPos -= ticks
                    currentPos = 100 + currentPos
                    password += 1
            elif currentPos - ticks == 0:
                currentPos = 0
                password += 1
        elif direction[0] == "R":
            ticks = int(direction[1:])
            while ticks > 100:
                ticks -= 100
                password += 1
            if currentPos + ticks < 100:
                currentPos += ticks
            elif currentPos + ticks > 99:
                if currentPos == 0:
                    currentPos = ticks - 100
                    password += 1
                    continue
                elif currentPos != 0:
                    currentPos = currentPos + ticks
                    currentPos = currentPos - 100
                    password += 1
            elif currentPos + ticks == 100:
                currentPos = 0
                password += 1

        print(f"Current position: {currentPos}, Current password: {password}")

    print(f"Part 2: {password}")


if __name__ == "__main__":
    main()


# part 2
# consider the fact thatwhen i read the next instructioe=n, it will currentPos from 0. dont miscount the 0
