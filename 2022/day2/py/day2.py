def main() -> int:
    o_c = ['A', 'C', 'B']
    s_c = ['X', 'Z', 'Y']
    with open('../input.txt', 'r') as f:
        p1_score=0
        p2_score=0
        for line in f:
            o,s = line.strip().split(' ')
           
            s_idx = s_c.index(s) 
            o_idx = o_c.index(o) 
            
            # Part 1
            if s_idx == o_idx:
                p1_score += 3
            elif (s_idx + 1) % 3 == o_idx:
                p1_score += 6
            p1_score += (ord(s) - 87)

            # Part 2 
            a = 0
            if s_idx == 0:
                a = (o_idx + 1) % 3
            elif s_idx == 1:
                a = (o_idx - 1) % 3
                p2_score += 6
            else:
                a = (o_idx)
                p2_score += 3
            p2_score += ord(s_c[a]) - 87

        print(p1_score)
        print(p2_score)
    return 0

if __name__ == '__main__':
    exit(main())
