"""[LEARNING LOGS] Pad Thai"""
def main():
    """Main function"""
    ingredients = {
        "Pad Thai Sauce", "Tofu", "Pickle Turnip",
        "Shrimp", "Bean Sprouts", "Noodle", "Chives",
        "Lime", "Egg", "Oil", "Peanuts"
    }

    taste = {"Sweet", "Sour", "Salty"}
    taste_input, ingre_input = set(), set()

    while True:
        ingre = input()
        if ingre == "Cook":
            break
        ingre_input.add(ingre)

    while True:
        t_input = input()
        if t_input == "End":
            break
        taste_input.add(t_input)

    ingred_is_correct = ingre_input == ingredients
    taste_is_correct = taste_input == taste

    if ingre_input.difference(ingredients):
        print("This is not Pad Thai!!!")
    elif not ingred_is_correct:
        print("This is bad!")
    elif ingred_is_correct and not taste_is_correct:
        print("Not Bad...")
    else:
        print("Delicious!")
main()
