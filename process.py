import glob, os, sys

if len(sys.argv) != 2:
    print("Usage: process.py <img dir>")
    sys.exit()


# Current directory
current_dir = os.path.abspath(sys.argv[1])


# current_dir = 'Your dataset path.'

# Directory where the data will reside, relative to 'darknet.exe'
#path_data = './NFPAdataset/'

# Percentage of images to be used for the test set
percentage_test = 10

# Create and/or truncate train.txt and test.txt
file_train = open('train.txt', 'w')
file_test = open('test.txt', 'w')

# Populate train.txt and test.txt
counter = 0
index_test = round(100 / percentage_test)
print(index_test)
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpg")):
    title, _ = os.path.splitext(os.path.basename(pathAndFilename))

    if counter == 0:
        file_test.write(current_dir + "/" + title + '.jpg' + "\n")
    else:
        file_train.write(current_dir + "/" + title + '.jpg' + "\n")
    
    counter = (counter + 1) % index_test
