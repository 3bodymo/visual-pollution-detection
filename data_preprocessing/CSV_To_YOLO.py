import os
import pandas as pd

data = pd.read_csv('train.csv')
numOfRows = len(data.index)

def main():
    for i in range(numOfRows):
        row = data.iloc[i]
        classOfObject = int(row[0])
        imageName = os.path.splitext(row[1])[0]
        x_max = row[3]
        x_min = row[4]
        y_max = row[5]
        y_min = row[6]
        x_center = ((x_max - x_min) / 2) + x_min
        x_center_percentage = (x_center / 1920) * 2
        y_center = ((y_max - y_min) / 2) + y_min
        y_center_percentage = (y_center / 1080) * 2
        widthOfBox = (x_max - x_min) / 1920
        heightOfBox = (y_max - y_min) / 1080
        with open(f"./train/{imageName}.txt", "a") as f:
            f.write(f"{classOfObject} {x_center_percentage} {y_center_percentage} {widthOfBox} {heightOfBox}\n")
            f.close()

    for path in os.listdir("./train"):
        if os.path.isfile(os.path.join("./train", path)):
            with open(f'./train/{path}', 'a') as f:
                f.truncate(f.tell()-1)


if __name__ == "__main__":
    main()