import random
import string

adjectives = [
    "Cool", "Happy", "Fast", "Mighty", "Brave", "Clever", "Sneaky", "Funky", "Epic", "Crazy",
    "Legendary", "Fearless", "Chill", "Witty", "Electric", "Wild", "Bold", "Charming", "Sly", "Loyal",
    "Mysterious", "Cheerful", "Energetic", "Vibrant", "Magical", "Fierce", "Glorious", "Jolly", "Fearless", "Playful",
    "Savage", "Daring", "Cunning", "Noble", "Reckless", "Radiant", "Spunky", "Thunderous", "Zany", "Ambitious",
    "Gracious", "Crafty", "Stormy", "Jumpy", "Sassy", "Eager", "Swift", "Rebellious", "Wicked", "Fearsome"
]

nouns = [
    "Tiger", "Dragon", "Panda", "Ninja", "Wizard", "Gamer", "Racer", "Wolf", "Phoenix", "Joker",
    "Falcon", "Knight", "Shadow", "Sniper", "Champion", "Beast", "Wanderer", "Assassin", "Demon", "Viking",
    "Samurai", "Gladiator", "Titan", "Ghost", "Spartan", "Hunter", "Rebel", "Ranger", "Warrior", "Master",
    "Guardian", "Specter", "Sorcerer", "Legend", "Sage", "Brawler", "Nomad", "Predator", "Sentinel", "Pirate",
    "Warden", "Slayer", "Commander", "Ronin", "Explorer", "Duelist", "Prophet", "Monarch", "Invoker", "Storm"
]

def generate_username(number=True, special=True):
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adj + noun
    
    if number:
        username += str(random.randint(10, 99))  

    if special:
        username += random.choice(string.punctuation)  

    return username

def save_usernames(usernames, filename="usernames.txt"):
    with open(filename, "a") as file:
        for username in usernames:
            file.write(username + "\n")
    print(f"Usernames saved to {filename}!")

def main():
    print("Welcome to the Random Username Generator")
    
    num_usernames = int(input("How many usernames do you want to generate? "))
    number = input("Include numbers? (yes/no): ").strip().lower() == "yes"
    special = input("Include special characters? (yes/no): ").strip().lower() == "yes"

    # generated_usernames = [generate_username(number, special) for _ in range(num_usernames)]
    generated_usernames = []
    for _ in range(num_usernames):
        username = generate_username(number, special)
        generated_usernames.append(username)

    print("\n Generated Usernames")
    for username in generated_usernames:
        print(username)

    save_choice = input("\nDo you want to save these usernames to a file? (yes/no): ").strip().lower()
    if save_choice == "yes":
        save_usernames(generated_usernames)

if __name__ == "__main__":
    main()
