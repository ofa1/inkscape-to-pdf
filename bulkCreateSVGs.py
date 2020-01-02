'''
Program to take a source SVG file, find the placeholder text 'Participant'
and replace it with each participant's name which is read from a names.txt 
 having the full name in each line
'''

import os, sys, re
import traceback

try:
    textToSearchAndReplace = 'Participant'
    output_folder = "certificates"

    assert len(sys.argv) == 2, "Insufficient arguments provided"
    sourcefolder = sys.argv[1]
    
    assert os.path.isfile(os.path.join(sourcefolder, 'sourcefile.svg')), "sourcefile.svg not found in the folder specified:"+sourcefolder
    assert os.path.isfile(os.path.join(sourcefolder, 'names.txt')), "names.txt not found in the folder specified:"+sourcefolder
    
    with open(os.path.join(sourcefolder, 'sourcefile.svg'), 'r') as file :
        sourcesvg = file.read()
    
    nameslist = open(os.path.join(sourcefolder, 'names.txt'), "r").readlines()
    
    if not os.path.isdir(os.path.join(sourcefolder, output_folder)):
        os.makedirs(os.path.join(sourcefolder, output_folder), exist_ok=True)
    
    for n in nameslist:
        name = " ".join(n.split())
        name = name.title()
        name = name.replace("\n", "")
        name = re.sub(r"[^\w\s\-]*", "", name)
        print("Currently processing:", name)
        # Replace the target string
        currfile = sourcesvg.replace(textToSearchAndReplace, name)
        # Write the file out
        with open(os.path.join(sourcefolder, output_folder) + "/" + name + '.svg', 'w', encoding='utf-8') as file:
            file.write(currfile)
        os.chdir(os.path.join(sourcefolder, output_folder))
        os.system(f'inkscape --without-gui --export-pdf="'+ name + '.pdf" "'+ name + '.svg" --export-area-page')
except:
    print("Exception occured!")
    print(traceback.format_exc())
    input("Press any key to exit")
