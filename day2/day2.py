import itertools


def read_input(path):
    with open(path, mode="r") as f:
        return f.readlines()

def main():
    if __name__ == "__main__":
        lines = read_input("input.txt")
        line = [line.split(": ")[1] for line in lines]
        
        print(line)

main()