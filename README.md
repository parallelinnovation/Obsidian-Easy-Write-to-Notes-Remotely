# Obsidian-Easy-Write-to-Notes-Remotely

From your daily notes, you can easily send a block of text to another note by linking it like this: >[[Note]]. 

For example, lets say you wanted to add to your grocery list note. You could write this in your daily notes:

> - Buy avocados >[[Grocery list]]

You can tell that the block of text was successfully added when the greater than symbol (>) disappears. In a few seconds, it will look like this:

> - Buy avocados [[Grocery list]]

In the grocery list note, The text will appear at the end of the linked file with the daily note it comes from linked, like this:

> - Buy avocados [[November 12th, 2021]]

The link must be at the end of the line, anything after the link will not be copied. 

---

# Getting started

1. Open the python script "Obsidian Easy Write To Notes Remotely.py" in a text editor. 
2. Add your obsidian vault folder path and daily notes folder path into the variables "ObsidianVaultFolder" and "DailyNotesFolder". 
3. Ensure your daily notes titles are in the format **MMMM Do, YYYY** (example: **November 12th, 2021**)
4. Run the python script. 
5. [Optional] Compile the .py file into an .exe file and have it automatically run when your computer starts up.
  5.1. Download [Auto-py-to-exe](https://pypi.org/project/auto-py-to-exe/) using pip
  5.2. Run Auto-py-to-exe and create the exe file. 
  5.3 Copy the file to your startup folder (you can find it on Windows by using Win+R and type shell:startup)

# Example:

[Example](https://preview.redd.it/9xqp6eivmdz71.gif?format=mp4&s=db7714a0ddb43a4d1e05ba78298d39721c16922c)
