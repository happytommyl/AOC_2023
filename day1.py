import itertools

def read_input(path):
    with open(path, mode="r") as f:
        return f.readlines()


def repl(s:str):
    strings = itertools.accumulate(s, lambda x, y: x.replace("one", "1ne").replace("two", "2wo").replace("three", "3hree").replace("four", "4our").replace("five", "5ive").replace("six", "6ix").replace("seven", "7even").replace("eight", "8ight").replace("nine", "9ine") +y)

    return list(strings)[-1]

def main():
    if __name__ == "__main__":
        lines = read_input("input.txt")
        part1_nums = ["".join([char if char.isdigit() else "" for char in line]) for line in lines]
        part2_nums = ["".join([char if char.isdigit() else "" for char in repl(line)]) for line in lines]
        print(f"part1: {sum([int(num[0]) * 10 + int(num[-1]) for num in part1_nums])}")
        print(f"part2: {sum([int(num[0]) * 10 + int(num[-1]) for num in part2_nums])}")
main()