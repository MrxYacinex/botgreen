import os
from datetime import datetime, timedelta
from random import randint, sample

# Start- und Enddatum definieren
start_date = datetime(2025, 2, 19)
end_date = datetime(2025, 3, 4)

# Alle Tage im Zeitraum berechnen
total_days = (end_date - start_date).days + 1

# Zufällige Anzahl an Tagen auswählen (ca. 60% der Tage werden genutzt)
num_commit_days = int(total_days * 0.3)  # 60% der Tage
commit_days = sorted(sample(range(total_days), num_commit_days))

# Datei initialisieren
with open('file.txt', 'w') as file:
    file.write('Initial commit\n')

for day_offset in commit_days:
    commit_date = start_date + timedelta(days=day_offset)
    formatted_date = commit_date.strftime('%Y-%m-%d %H:%M:%S')

    # Zufällige Anzahl an Commits pro Tag (1–5)
    for _ in range(randint(1, 5)):
        with open('file.txt', 'a') as file:
            file.write(f'Commit am {formatted_date}\n')

        os.system('git add .')
        os.system(f'git commit --date="{formatted_date}" -m ' '"commit on {formatted_date}"')

# Push to GitHub
os.system('git push -u origin main')
