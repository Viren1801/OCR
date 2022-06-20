from pdf2image import convert_from_path
import os


def convert(file, outputDir):
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)         
    pages = convert_from_path(file, 500)
    counter = 1
    for page in pages:
        myfile = outputDir + 'output' + str(counter) + ".jpg"
        counter = counter + 1
        page.save(myfile, 'JPEG')
    


file1 = 'Easy_recipes.pdf'
outputDir1 = 'images/'
convert(file1, outputDir1)
print("Done")