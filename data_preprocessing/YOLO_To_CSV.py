import os
import pandas as pd
import glob

df = pd.DataFrame(columns=['class', 'image_path', 'name', 'xmax', 'xmin', 'ymax', 'ymin'])

classes = { 0:'GRAFFITI',
            1:'FADED_SIGNAGE',
            2:'POTHOLES',
            3:'GARBAGE',
            4:'CONSTRUCTION_ROAD',
            5:'BROKEN_SIGNAGE',
            6:'BAD_STREETLIGHT',
            7:'BAD_BILLBOARD',
            8:'SAND_ON_ROAD',
            9:'CLUTTER_SIDEWALK',
            10:'UNKEPT_FACADE' }


directory = 'val\labels'

def main():

    # iterate over files in that directory
    
    for filename in glob.iglob(f'{directory}/*.txt'):
        with open(filename, "r") as f:

            # iterate over lines in that file

            for line in f:
                all_values = [float(x) for x in line.split()]

                Class = int(all_values[0])
                image_path = f"{os.path.splitext(os.path.basename(filename))[0]}.jpg"
                name = classes[all_values[0]]
                
                xmax = int(((1920*all_values[1]) + (1920*all_values[3]))/2)
                xmin = int(xmax - (1920*all_values[3]))
                
                ymax = int(((1080*all_values[2]) + (1080*all_values[4]))/2)
                ymin =int( ymax - (1080*all_values[4]))

                df.loc[len(df.index)] = [Class, image_path, name, xmax, xmin, ymax, ymin] 

            f.close()

    # saving the dataframe to CSV

    df.to_csv('final_test.csv', index=False)

if __name__ == "__main__":
    main()