import os
os.chdir('/Users/mac/Downloads/R语言就应该这样学')
os.stat('67581656_nb2-1-80.flv').st_birthtime

# initiate a list for time and filename
filename_and_time = []
# get all flv file names
flv_list = [x for x in os.listdir() if 'flv' in x]


# sort filenames based on creation time ( started downloading in order)
for file in flv_list:
    filename_and_time.append((os.stat(file).st_birthtime, \
                              file))
filename_and_time.sort()

# read every 2nd line of code (get the title)
with open('name_of_33ps_R语言学习.txt') as f:
    lines = f.readlines()
# format the filename
proper_filenames = [x.replace('\n','').replace(' ','_') \
                    for x in lines[2:-1:3]]
# add order to the filename
for i in range(0,len(proper_filenames)):
    proper_filenames[i] = str(i).zfill(2) + '_' + proper_filenames[i] + '.flv'
    
# rename files
for i in range(0, len(filename_and_time)):
    time, old = filename_and_time[i]
    new = proper_filenames[i]
    os.rename(old, new)
