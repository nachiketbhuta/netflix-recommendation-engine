import csv , json

csvFilePath = 'D:/Github-Projects/DM IA/netflix-recommendation-engine/data/netflix_movies.csv'
jsonFilePath = 'D:/Github-Projects/DM IA/netflix-recommendation-engine/data/netflix_movies_intents.json'

data = {}
intents = []
with open(csvFilePath ,  'r', encoding='utf8', errors='ignore') as csvFile:
    csvReader = csv.DictReader(csvFile)
    print(csvReader)
    for csvRow in csvReader:
        show_id = csvRow['show_id']
        data[show_id] = csvRow
# print(data)

with open(jsonFilePath , 'w', encoding='utf8', errors='ignore') as jsonFile:
    jsonFile.write(json.dumps(data , indent=4))