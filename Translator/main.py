import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

def translate_text():
    try:
        input_text = input_text_box.get("1.0", tk.END).strip()
        if not input_text:
            messagebox.showwarning("Input Error", "Please enter text to translate.")
            return
        
        source_lang = source_lang_combobox.get()
        target_lang = target_lang_combobox.get()
        
        translated_text = GoogleTranslator(source=source_lang, target=target_lang).translate(input_text)
        
        output_text_box.delete("1.0", tk.END)
        output_text_box.insert(tk.END, translated_text)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

root = tk.Tk()
root.title("Simple Translator")

input_text_box = tk.Text(root, height=10, width=50)
input_text_box.pack(pady=10)

source_lang_label = tk.Label(root, text="Source Language:")
source_lang_label.pack()
source_lang_combobox = ttk.Combobox(root, values=["en", "fr", "de", "es", "it", "pt", "ru", "zh"])
source_lang_combobox.set("en")  # Default to English
source_lang_combobox.pack()


target_lang_label = tk.Label(root, text="Target Language:")
target_lang_label.pack()
target_lang_combobox = ttk.Combobox(root, values=["en", "fr", "de", "es", "it", "pt", "ru", "zh"])
target_lang_combobox.set("fr")  # Default to French
target_lang_combobox.pack()

translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack(pady=10)

output_text_box = tk.Text(root, height=10, width=50)
output_text_box.pack(pady=10)

root.mainloop()
