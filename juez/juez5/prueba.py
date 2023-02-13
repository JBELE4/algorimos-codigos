
def curacovid(molecules):
    if len(molecules) <= 2:
        common_prefix = ""
        shortest_string = min(molecules, key=len)
        if len(molecules) == 2:
            for i in range(len(shortest_string)):
                if molecules[0][i] == molecules[1][i]:
                    common_prefix += molecules[0][i]
                else:
                    break
        else:
            common_prefix = molecules[0]
        return common_prefix
    else:
        mid = len(molecules) // 2
        common_prefix_left = curacovid(molecules[:mid])
        print(common_prefix_left)
        common_prefix_right = curacovid(molecules[mid:])
        if len(common_prefix_left) == len(common_prefix_right):
            return common_prefix_left
        elif len(common_prefix_left) > len(common_prefix_right):
            return common_prefix_right
        else:
            return common_prefix_left


# MAIN PROGRAMME
n = int(input().strip())
molecules = []
for _ in range(n):
    molecules.append(input().strip())

common_prefix = curacovid(molecules)
print(common_prefix)
