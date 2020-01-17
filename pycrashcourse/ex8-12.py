def make_sandwich(*ingredients):
    print("Making a sandwich with: ")
    for ingredient in ingredients:
        print("-" + ingredient)



make_sandwich("bacon", "sourdough", "lettuce", "tomato")
make_sandwich("egg", "cheese", "turkey")
make_sandwich("peanut butter", "Jelly")