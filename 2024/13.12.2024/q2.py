


def smallest(x1,y1,x2,y2,prize1,prize2):
    smallest = [10000000000000, 10000000000000]
    for a in range(10000000000000):
        for b in range(10000000000000):
            if (a*x1 + b*y1 == prize1) and (a*x2 + b*y2 == prize2):
                if (a < smallest[0] and b < smallest[1]):
                    smallest = [a,b]
    if smallest[0] and smallest[1] != 100:
        tokens = smallest[0]*3 + smallest[1]*1
        print("done")
        return tokens
    return 0 

# Main program
total_tokens = 0

with open("input.txt", "r") as file:
    lines = file.read().splitlines()

for i in range(0, len(lines), 4):  # Each case is 4 lines
    button_a = lines[i].split(":")[1].strip()
    button_b = lines[i + 1].split(":")[1].strip()
    prize = lines[i + 2].split(":")[1].strip()
    
    x1, y1 = map(int, [btn.split('+')[1] for btn in button_a.split(", ")])
    x2, y2 = map(int, [btn.split('+')[1] for btn in button_b.split(", ")])
    prize1, prize2 = map(int, [prz.split('=')[1] for prz in prize.split(", ")])

    prize1 += 10000000000000
    prize2 += 10000000000000
    
    # Re-mapping based on the corrected logic
    x1, y1, x2, y2 = x1, x2, y1, y2
    
    total_tokens += smallest(x1, y1, x2, y2, prize1, prize2)

print("Total tokens:", total_tokens)