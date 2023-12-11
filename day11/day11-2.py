import re

def main():
    # Create initial universe array
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

    # Create flipped universe array
    universe_flipped = []
    for i in range(len(universe[0])):
        universe_flipped.append([])
        for j in range(len(universe)):
            universe_flipped[i].append(universe[j][i])

    # Register galaxies locations
    galaxies_locations = {}
    for i, row in enumerate(universe):
        for j, e in enumerate(row):
            if re.match(r'[0-9]+', e):
                galaxies_locations[e] = [i, j]

    # Display
    """
    print("Universe :")
    for e in universe:
        print(e)
    print("Flipped universe :")
    for e in universe_flipped:
        print(e)
    print("Galaxies: ", galaxies_locations)
    """

    # Expand galaxies locations
    temp = {}
    for e in galaxies_locations.items():
        temp[e[0]] = e[1].copy()

    # + x
    for i, array in enumerate(universe):
        if len(set(array)) == 1:
            for j in range(1, galaxy_count + 1):
                if galaxies_locations[str(j)][0] > i:
                    temp[str(j)][0] += 999999

    # + y
    for i, array in enumerate(universe_flipped):
        if len(set(array)) == 1:
            for j in range(1, galaxy_count + 1):
                if galaxies_locations[str(j)][1] > i:
                    temp[str(j)][1] += 999999

    galaxies_locations = temp

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
    """
    print("Expanded galaxies: ", galaxies_locations)
    print("Galaxy pairs: ", galaxy_pairs)
    """
    
    print("Answer: ", answer)

main()
