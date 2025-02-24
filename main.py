import os
from random import randint

# Ensure that 'file.txt' is in the repository and contains initial data
with open('file.txt', 'w') as file:
    file.write('Initial commit\n')

for i in range(1, 365):
    for j in range(0, randint(1, 10)):
        d = str(i) + ' days ago'
        
        # Write the random date message to 'file.txt'
        with open('file.txt', 'a') as file:
            file.write(d + '\n')
        
        # Add the changes
        os.system('git add .')
        
        # Commit the changes with a date from 'd'
        os.system(f'git commit --date="{d}" -m "commit"')

# Push to GitHub
os.system('git push -u origin main')
