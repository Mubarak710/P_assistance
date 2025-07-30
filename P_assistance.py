import random

def get_user_data():
    questions = [
        ("What is your name? ", "name"),
        ("How old are you? ", "age"),
        ("What is your favorite color? ", "color"),
        ("What is your favorite food? ", "food"),
        ("Which city do you live in? ", "city"),
        ("Which SHS did you attend? ", "shs"),
        ("What is your favorite soccer team? ", "team")
    ]
    random.shuffle(questions)

    answers = {}
    for question, key in questions:
        answers[key] = input(question)

    return answers

def create_summary(data):
    summary = f"""
Hello, {data['name']}!
You are {data['age']} years old, love the color {data['color']}, and enjoy eating {data['food']}.
Life must be awesome in {data['city']}!
You attended {data['shs']} and support {data['team']} in soccer.
"""
    return summary

def save_to_file(name, summary, rating):
    filename = f"{name}.txt"
    with open(filename, "w") as file:
        file.write(summary)
        file.write(f"\nUser rating: {rating}/5\n")
    print(f"Summary saved to {filename}.")

def main():
    while True:
        user_data = get_user_data()
        summary = create_summary(user_data)
        print("\n--- Personalized Summary ---")
        print(summary)

        # Save to file?
        save_choice = input("Would you like to save this summary to a file? (yes/no): ").strip().lower()
        if save_choice == "yes":
            rating = input("Rate this assistant (1 to 5): ").strip()
            save_to_file(user_data['name'], summary, rating)

        # Restart?
        restart = input("Would you like to restart the assistant? (yes/no): ").strip().lower()
        if restart != "yes":
            print("Goodbye!")
            break

# Run the program
if __name__ == "__main__":
    main()
