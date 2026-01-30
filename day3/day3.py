filename = "day3/input.txt"
totalJoltage = 0


def main():
    global totalJoltage
    try:
        with open(filename, "r") as file:
            for line in file:
                batteriesString = line.strip()
                batteries = [int(char) for char in batteriesString]
                print(f"Batteries: {batteries}")
                num1 = max(batteries)
                print(f"Max battery: {num1}")
                num1Index = batteries.index(num1)
                num2 = int(str(max(batteries[:num1Index], default=0)) + str(num1))
                # check if there are elements after num1Index
                if num1Index + 1 >= len(batteries):
                    num3 = 0
                else:
                    num3 = int(
                        str(num1) + str(max(batteries[num1Index + 1 :], default=0))
                    )

                if num2 > num3:
                    totalJoltage += num2
                elif num3 > num2:
                    totalJoltage += num3
                else:
                    totalJoltage += num2
                print(f"Num2: {num2}, Num3: {num3}, TotalJoltage: {totalJoltage}")
    except FileNotFoundError:
        print(f"Error: The file at {filename} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    print(f"Part 1: {totalJoltage}")


if __name__ == "__main__":
    main()
