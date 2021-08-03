from pdf2image import convert_from_path
from tqdm import tqdm
import os, shutil
try:
    os.makedirs('./TIFFs')
except FileExistsError:
    # directory already exists
    pass

pdf_directory = input('\n'"Enter absolute path to PDF directory: ").strip()

for filename in os.listdir(pdf_directory):
    if filename.endswith('.pdf'):
        file = (os.path.join(pdf_directory, filename))
        pages = convert_from_path(file)
        img_file = file.replace('.pdf', "")

        count = 0
        pbar = tqdm(pages, colour = 'green', bar_format = '{l_bar}{bar:20}{r_bar}{bar:-10b}')
        for page in pbar:
            pbar.set_description("Extracting TIFFs from %s" % filename)
            count += 1
            tiff_file = img_file + "_" + str(count).zfill(3) + ".tif"
            page.save(tiff_file, dpi=(600, 600)), 'TIFF'
            shutil.move(tiff_file, './TIFFs')

print('\n'
'''
  ,-~~-.___.
 / |  '     \      "Finished!"
(  )         0
 \_/-, ,----'
    ====           //
   /  \-'~;    /~~~(O)
  /  __/~|   /       |
=(  _____| (_________|

''''\n')
