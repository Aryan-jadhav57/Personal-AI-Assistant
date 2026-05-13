import tkinter as tk
from tkinter import Entry, Label, Button
import webbrowser


# define the main window
root=tk.Tk()
root.title("YOUR AI ASSISTANT")
 
# adding a background color
root.configure(bg='steelblue')

# define the function to automate youtube search
def search_youtube():
  query=Entry.get()
  url=f"https://www.youtube.com/results?search_query={query}"
  webbrowser.open(url)

# define the function to automate Google search
def search_google():
  query=Entry.get()
  url=f"https://www.youtube.com/search?q={query}"
  webbrowser.open(url)

# define the function to automate instagram search
def search_instagram():
  Username=Entry.get().replace('@',"") # ensure username is clean of "@"
  url=f'www.instagram.com/{Username}/'
  webbrowser.open(url)
 
# create input field, Labels and buttons
Label(root, text="Enter your command: ").pack(pady=10)
Entry=Entry(root, width=50)
Entry.pack(pady=10)
Button(root, text = "search on youtube",command=search_youtube).pack(pady=5)
Button(root, text = "search on Google",command=search_google).pack(pady=5)
Button(root, text = "search on Instagram ",command=search_instagram).pack(pady=5)


# run the GUI event loop
root.mainloop()
