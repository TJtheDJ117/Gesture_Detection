import os
import random

lowest_size = 1500
for letter in os.listdir("C:/Users/tomja/Downloads/Trial"):
    numbers = [item for item in range(1, 3001)]
    dir_path = "C:/Users/tomja/Downloads/Trial/" + letter
    file_count = 0
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            file_count += 1
    print('File count:', file_count)

    while(file_count > lowest_size):
        random_file = random.choice(numbers)
        file_path = os.path.join("C:/Users/tomja/Downloads/Trial/" + letter + "/", letter + str(random_file) + ".jpg")
        try:
            os.remove(file_path)
        except:
            numbers.remove(random_file)
        else:
            print(letter + str(random_file) + ".jpg DELETED")
            file_count -= 1
            print("New " + letter + " file count:" + str(file_count))
print("EVENING DONE")