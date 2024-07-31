COLOR_TO_CODE = {'absolutezero': '#0048ba', 'acidgreen': '#b0bf1a', 'aliceblue': '#f0f8ff', 'aqua': '#00ffff',
                 'ashgrey': '#b2beb5', 'blueviolet': '#8a2be2', 'brightube': '#d19fe8', 'brilliantrose': '#ff55a3',
                 'smokyblack': '#100c08', 'crimson': '#dc143c'}

color = input('Color: ').lower()
while color != '':
    try:
        print(COLOR_TO_CODE[color])
    except KeyError:
        print('Invalid color or unrecorded color')
    color = input('Color: ').lower()
