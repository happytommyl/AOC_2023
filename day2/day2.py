import itertools
import operator
import functools


def read_input(path):
    with open(path, mode="r") as f:
        return f.readlines()

def part1(games):
    sum = 0
    for i, game in enumerate(games, 1):
        picks = game.replace(";", ",").replace('\n', '').split(', ')
        for pick in picks:
            num, color = pick.split(' ')
            match color:
                case "red":
                    i *= 1 if int(num) <= 12 else 0
                                   
                case "green":
                    i *= 1 if int(num) <= 13 else 0
                    
                case "blue":
                    i *= 1 if int(num) <= 14 else 0     
        sum += i
    return sum

def part2(games):
    power =[]
    for i, game in enumerate(games, 1):
        picks = game.replace(";", ",").replace('\n', '').split(', ')
        m = {"red": 0, "green": 0, "blue": 0}
        
        for pick in picks:
            num, color = pick.split(' ')
            num = int(num)
            match color:
                case "red":
                    m["red"] = num if num > m["red"] else m["red"]
                                   
                case "green":
                    m["green"] = num if num > m["green"] else m["green"]
                    
                case "blue":
                    m["blue"] = num if num > m["blue"] else m["blue"]
        power.append(functools.reduce(operator.mul, m.values()))
    return sum(power)

def part1(games):
    sum = 0
    for i, game in enumerate(games, 1):
        picks = game.replace(";", ",").replace('\n', '').split(', ')
        for pick in picks:
            num, color = pick.split(' ')
            match color:
                case "red":
                    i *= 1 if int(num) <= 12 else 0
                                   
                case "green":
                    i *= 1 if int(num) <= 13 else 0
                    
                case "blue":
                    i *= 1 if int(num) <= 14 else 0     
        sum += i
    return sum

def main():
    if __name__ == "__main__":
        lines = read_input("input.txt")
        games = [line.split(": ")[1] for line in lines]
        sum_part1 = part1(games)
        sum_part2 = part2(games)
        print(sum_part1)
        print(sum_part2)
main()