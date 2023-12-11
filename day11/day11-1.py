import re

def main():
    # Create initial array
    universe = []
    galaxy_count = 0
    with open("input.txt", 'r', encoding="UTF-8") as file:
        i = 0
        for line in file:
            universe.append([])
            for char in line:
                if char == '#':
                    galaxy_count = galaxy_count + 1
                    universe[i].append(str(galaxy_count))
                elif char != '\n':
                    universe[i].append(char)
            i = i + 1

    # Expand array vertically
    temp = []
    for e in universe:
        temp.append(e)
        if len(set(e)) == 1:
            temp.append(e)
    universe = temp

    # Expand array horizontally
    ### Flip the array°
    temp = []
    for i in range(len(universe[0])):
        temp.append([])
        for j in range(len(universe)):
            temp[i].append(universe[j][i])
    universe = temp
    ### Expand array vertically
    temp = []
    for e in universe:
        temp.append(e)
        if len(set(e)) == 1:
            temp.append(e)
    universe = temp
    ### Flip the array back°
    temp = []
    for i in range(len(universe[0])):
        temp.append([])
        for j in range(len(universe)):
            temp[i].append(universe[j][i])
    universe = temp

    # Register galaxies locations
    galaxies_locations = {}
    for i, row in enumerate(universe):
        for j, e in enumerate(row):
            if re.match(r'[0-9]+', e):
                galaxies_locations[e] = (i, j)

    # Register pairs and their shortest paths' lengths
    galaxy_pairs = {}
    for i in range(1, galaxy_count + 1):
        for j in range(i+1, galaxy_count + 1):
            galaxy_pairs[str(i)+'-'+str(j)] = \
            (max(galaxies_locations[str(i)][0], galaxies_locations[str(j)][0]) - min(galaxies_locations[str(i)][0], galaxies_locations[str(j)][0])) + \
            (max(galaxies_locations[str(i)][1], galaxies_locations[str(j)][1]) - min(galaxies_locations[str(i)][1], galaxies_locations[str(j)][1]))

    # Calculate answer
    answer = 0
    for e in galaxy_pairs.values():
        answer = answer + e

    # Display
    print(answer)
    """
    print("Universe :")
    for e in universe:
        print(e)
    print("Galaxies: ", galaxies_locations)
    print("Galaxy pairs: ", galaxy_pairs)
    """

main()
