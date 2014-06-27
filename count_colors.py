from PIL import Image
from collections import defaultdict

category_color = {(226, 7, 135): 'CAT 1'
                 ,(143, 82, 161): 'CAT 2' 
                 ,(246, 139, 31): 'CAT 3'
                 ,(57, 181, 74): 'CAT 4'
                 ,(209, 197, 204): 'Cortesia'
                 ,(35, 31, 32): 'Suítes'
                 }

def count_colors(image_file='./imagem_estadios/sp.png'):
    im = Image.open(image_file)
    by_color = defaultdict(int)
    for pixel in im.getdata():
        if category_color.has_key(pixel):
            by_color[category_color[pixel]] += 1
    return by_color

stadium_images = !ls ./imagem_estadios/*png
stadium_colors = {si: count_colors(si) for si in stadium_images}
stadium_colors