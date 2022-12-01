def main() -> int:
    with open('../input.txt', 'r') as file:

        # Part 1
        a = [x.strip().split('\n') for x in file.read().split('\n\n')]
        b = [eval("+".join(x)) for x in a]
        print(max(b))
        
        # Part 2
        c = b
        s = 0
        for i in range(0,3):
            s += max(c)
            c.remove(max(c))
        print(s)

    return 0

if __name__ == '__main__':
    exit(main())
