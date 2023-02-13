# Sandia function
def sandia(w, c, xs, xe, ys, ye):
    if c == 0:
        #Iterate over the watermelon and return total
        total = 0
        for i in range(xs, xe):
            for j in range(ys, ye):
                total += w[i][j]
        return total

    # Get mid points
    xm = (xs + xe) // 2
    ym = (ys + ye) // 2

    # Recursive calling. Return the minimum of the totals
    total1 = sandia(w, c-1, xs, xm, ys, ym)
    total2 = sandia(w, c-1, xm, xe, ys, ym)
    total3 = sandia(w, c-1, xs, xm, ym, ye)
    total4 = sandia(w, c-1, xm, xe, ym, ye)
    return min(total1, total2, total3, total4)


# MAIN PROGRAMME
n, c = map(int, input().strip().split())
watermelon = []
for _ in range(n):
    watermelon.append(list(map(int, input().strip().split())))

print(sandia(watermelon, c, 0, len(watermelon), 0, len(watermelon)))
