import os
from random import randint

print(dir(os))

for i in range(200,100):
    for j in range(0,randint(1,10)):
        d = str(i)+"day"
        print(d)
        with open('data.txt','a') as file:
            file.write(d)
        os.system('git add --all')
        os.system('git commit --date="' + d + '" -m "commit" ')



os.system('git push -u origin main')

