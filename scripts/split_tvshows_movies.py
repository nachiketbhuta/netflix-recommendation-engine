import os
import csv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

data_file = os.path.join(BASE_DIR, 'data')

colrow = ['show_id', 'title', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in', 'description', 'type']
movies = [] 
tv_shows = []

# Read the data file and split it into movies and tv shows
with open(os.path.join(data_file, 'original', 'netflix_titles.csv'), 'r', encoding='utf8', errors='ignore') as f:
    csv_reader = csv.reader(f, delimiter=',')
    for row in csv_reader:
        if (row[-1] == str('Movie')):
            movies.append(row)
        else:
            tv_shows.append(row)

# Write the movies into movies.csv
with open(os.path.join(data_file, 'netflix_movies.csv'), 'w', newline='', encoding='utf8', errors='ignore') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(colrow)
    for row in movies:
        writer.writerow(row)
        
# Write the tv shows into tv_shows.csv
with open(os.path.join(data_file, 'netflix_tv_shows.csv'), 'w', newline='', encoding='utf8', errors='ignore') as f:
    writer = csv.writer(f, delimiter=',')
    # writer.writerow(colrow)
    for row in tv_shows:
        writer.writerow(row)
     
