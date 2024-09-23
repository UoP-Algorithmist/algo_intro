from urllib.request import urlopen
from bs4 import BeautifulSoup


def draw(cols):
    grid_size = 0
    for i in range(0, len(cols), 3):
        # find the biggest number between x and y coordinates
        grid_size = max(max(int(cols[i].text), int(cols[i + 2].text)), grid_size)

    grid_canvas = []
    for _ in range(grid_size + 1):
        grid_canvas.append([' '] * (grid_size + 1))
    for i in range(0, len(cols), 3):
        x = int(cols[i].text)
        y = int(cols[i + 2].text)
        grid_canvas[y][x] = cols[i + 1].text
    grid_canvas.reverse()

    for g in grid_canvas:
        print(''.join(g))


def draw_secret(doc_url: str):
    sock = urlopen(doc_url)
    data = sock.read()
    sock.close()
    # Read doc file and delete it afterwards
    bs_soup = BeautifulSoup(data, features="lxml")
    cols = bs_soup.find_all('td', {'colspan': '1'})[3:]  # exclude the titles
    draw(cols)


# █▀▀▀
# █▀▀
# █


"""

[['█', '-', '-', '-'],
['█', '▀', '▀', '-'],
['█', '▀', '▀', '▀'],
['-', '-', '-', '-']]
"""

draw_secret(
    'https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYrEdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub')

"""
['x-coordinate', 'Character', 'y-coordinate']
'0', '█', '0']
'0', '█', '1']
'0', '█', '2']
'1', '▀', '1']
'1', '▀', '2']
'2', '▀', '1']
'2', '▀', '2']
'3', '▀', '2']



"""
