import csv

def collect_game_data():
    amount = int(input("How many video games do you want to enter? "))
    games = []

    for i in range(amount):
        print(f"\nEnter the details for video game #{i+1}")
        name = input("Name: ")
        genre = input("Genre: ")
        developer = input("Developer: ")
        rating = input("ESRB Rating (E, T, M, etc.): ")

        games.append({
            'name': name,
            'genre': genre,
            'developer': developer,
            'rating': rating
        })

    return games

def save_games_csv(file_path, games):
    headers = ['name', 'genre', 'developer', 'rating']
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers, delimiter='\t')  
        writer.writeheader()
        writer.writerows(games)

game_list = collect_game_data()
save_games_csv('videogames2_tabulados.csv', game_list)
print("\n Data successfully saved in 'videogames2_tabulados.csv'")

#Documentacion de referencia https://docs.python.org/3/library/csv.html
