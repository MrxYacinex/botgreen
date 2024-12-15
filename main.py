import os
from datetime import datetime, timedelta
from random import randint

# Start- und Enddatum definieren
start_date = datetime(2024, 12, 15)
end_date = datetime(2025, 2, 26)

# Anzahl der Tage im Bereich berechnen
days_range = (end_date - start_date).days + 1

# Datei initialisieren
with open('file.txt', 'w') as file:
    file.write('Initial commit\n')

for i in range(days_range):
    commit_date = start_date + timedelta(days=i)
    formatted_date = commit_date.strftime('%Y-%m-%d %H:%M:%S')

    # Zufällige Anzahl an Commits pro Tag
    for _ in range(randint(1, 10)):
        with open('file.txt', 'a') as file:
            file.write(f'Commit am {formatted_date}\n')

        os.system('git add .')
        os.system(f'git commit --date="{formatted_date}" -m "commit on {formatted_date}"')

# Push to GitHub
os.system('git push -u origin main')
