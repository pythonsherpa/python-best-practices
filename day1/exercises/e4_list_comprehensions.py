"""
Exercise
Replace the code below with a list comprehension.
Follow the example shown in the demo.
"""
ingredients = ["SPAM", "BaCon", "haM", "EggS"]

# Loop
ingredients_lowercase = []
for item in ingredients:
    ingredients_lowercase.append(item.lower())
print(ingredients_lowercase)

# List comprehension
ingredients_lowercase = ...  # your code
print(ingredients_lowercase)


# Extra: dictionary comprehension
# Replace the code below with a dict comprehension.
languages = ["C", "Java", "Python", "JavaScript"]

language_lengths = {}
for lang in languages:
    language_lengths[lang] = len(lang)
print(language_lengths)  # prints {'C': 1, 'Java': 4, 'Python': 6, 'JavaScript': 10}

# Dict comprehension
language_lengths = ...   # your code
print(language_lengths)
