import tkinter as tk
from tkinter import ttk

tribal_dictionary = {
    "Yoruba": {
        "house": "ilé",
        "water": "omi",
        "fire": "ina",
        "food": "ounje",
        "love": "ifẹ",
        "friend": "ọrẹ",
        "tree": "igi",
        "child": "ọmọ",
        "earth": "ayé",
        "heaven": "orun",
        "river": "odò",
        "stone": "okuta",
        "market": "ọjà",
        "sun": "oorun",
        "moon": "osupa",
        "rain": "ọjo",
        "day": "ọjọ",
        "night": "alẹ",
        "road": "ọna",
        "money": "owo",
        "wind": "afẹfẹ",
        "time": "akoko",
        "king": "oba",
        "queen": "ayaba",
        "song": "orin"
    },
    
}

def invert_dictionary(dictionary):
    return {v: k for k, v in dictionary.items()}

def search_word(language, word):
    if language in tribal_dictionary:
        language_dict = tribal_dictionary[language]
        inverted_dict = invert_dictionary(language_dict)

        if word in language_dict:
            translation = language_dict[word]
            return f"Word Found: '{word}' in {language} means '{translation}'"
        elif word in inverted_dict:
            translation = inverted_dict[word]
            return f"Word Found: '{word}' in {language} is translated to English as '{translation}'"
        else:
            return f"Word '{word}' not found in {language}."
    else:
        return f"Language '{language}' not identified."

def on_search():
    language = language_var.get()
    word = word_entry.get().lower()
    result = search_word(language, word)
    result_label.config(text=result)

# Create the main window
root = tk.Tk()
root.title("Tribal Dictionary")

# Create and place the language dropdown
language_var = tk.StringVar()
language_label = tk.Label(root, text="Select Language:")
language_label.pack()
language_dropdown = ttk.Combobox(root, textvariable=language_var)
language_dropdown['values'] = list(tribal_dictionary.keys())
language_dropdown.pack()

# Create and place the word entry
word_label = tk.Label(root, text="Enter Word:")
word_label.pack()
word_entry = tk.Entry(root)
word_entry.pack()

# Create and place the search button
search_button = tk.Button(root, text="Search", command=on_search)
search_button.pack()

# Create and place the result label
result_label = tk.Label(root, text="")
result_label.pack()

# Run the application
root.mainloop()