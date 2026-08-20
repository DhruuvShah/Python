players = { 
"Virat": 85, 
"Rohit": 72, 
"Dhoni": 64, 
"Rahul": 91 
} 

name = input("Enter player name: ") 
if name in players: 
    print(name, "scored", players[name], "runs") 
else: 
    print("Player not found")