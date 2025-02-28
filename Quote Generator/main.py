import requests
import tkinter as tk


def get_random_quote():
    try:
        response = requests.get("https://api.quotable.io/random")
        data = response.json()
        quote = data["content"]
        author = data["author"]
        quote_text.set(f'"{quote}" - {author}')
    except requests.exceptions.RequestException as e:
        quote_text.set("Failed to fetch a quote. Check your internet connection.")



root = tk.Tk()
root.title("Random Quote Generator")

quote_text = tk.StringVar()
quote_label = tk.Label(
    root, textvariable=quote_text, wraplength=300, font=("Helvetica", 12)
)
quote_label.pack(pady=20)


new_quote_button = tk.Button(root, text="Get a New Quote", command=get_random_quote)
new_quote_button.pack()

get_random_quote()

root.mainloop()
