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

Note that this is still experimental. 

1. Open the python script "Obsidian Easy Write To Notes Remotely.py" in a text editor. 
2. Add your obsidian vault folder path and daily notes folder path into the variables "ObsidianVaultFolder" and "DailyNotesFolder". 
3. Ensure your daily notes titles are in the format **MMMM Do, YYYY** (example: **November 12th, 2021**)
4. Run the python script. 
