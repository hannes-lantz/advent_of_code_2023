
def solve(grid):      
    r, c = len(grid), len(grid[0])
    pos = {}
    ans1 = set()
    ans2 = set()
    
    for row in grid:
        for col in row:
            if col == '.':
                continue
            
            if col not in pos:
                pos[col] = []
            pos[col].append((grid.index(row), row.index(col)))
    
    return part1(pos, ans1, r, c), part2(pos, ans2, r, c)
        
def part1(pos, ans, r, c):   
    for key in pos:
        for i in range(len(pos[key])):
            for j in range(i+1, len(pos[key])):
                lr, lc = pos[key][i]
                rr, rc = pos[key][j]
                dr, dc = rr - lr, rc - lc
                
                if lr - dr >= 0 and lr - dr < r and lc - dc >= 0 and lc - dc < c:
                    ans.add((lr - dr, lc - dc))
                
                if rr + dr >= 0 and rr + dr < r and rc + dc >= 0 and rc + dc < c:
                    ans.add((rr + dr, rc + dc))
    return ans

def part2(pos, ans, r, c):
    for key in pos:
        for i in range(len(pos[key])):
            for j in range(i+1, len(pos[key])):
                lr, lc = pos[key][i]
                rr, rc = pos[key][j]
                dr, dc = rr - lr, rc - lc
                
                tempr, tempc = lr, lc
                while(tempr >= 0 and tempr < r and tempc >= 0 and tempc < c):
                    ans.add((tempr, tempc))
                    tempr -= dr
                    tempc -= dc
                        
                tempr, tempc = rr, rc
                while(tempr >= 0 and tempr < r and tempc >= 0 and tempc < c):
                    ans.add((tempr, tempc))    
                    tempr += dr
                    tempc += dc
    return ans
                          
def read_input(file_path):
    with open(file_path) as f:
        return f.read().splitlines()

def main():
    grid = read_input('input.txt')
    p1, p2 = solve(grid)

    print(f"P1: {len(p1)}")
    print(f"P2: {len(p2)}")

if __name__ == '__main__':
    main()
