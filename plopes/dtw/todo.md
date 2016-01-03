# To-do

## Requirements.txt

## Reload must be dynamically generated
When you create a new python file, you need to automatically get a reloader for it.
This could be dynamically generated from pd. Here's a possible sketch:
- nameOfMyFile-reloader.py: ** would be the filename for the new reloader ** 
- which would be a copy of: `cp base-reloader.py nameOfMyFile-reloader.py`
- then only four lines must be changed dynamically, as follows:
	- `import nameOfMyFile` (line 1)
	- `if (self.DEBUG) pdgui.post("Started reloader for:" + nameOfMyFile)` (line 6)
	- `reload(nameOfMyFile)` (line 9)
        - `if (self.DEBUG) pdgui.post("Done reloading:" + nameOfMyFile)` (line 10)

## or can it reload by receiving arguments on what to reload? (maybe easier)
The class would receive the name of what to reload as a reload function? But can the import be done?

## dollar zero is issing
The patch right now seems to only work for one instance at a time. This is likely because the $0-name is missing from dynamically created objects. 

## Which file should be searched to get the current directory?
Ideally the patch itself, this will be broken as soon as the user copies to their patch.
How to circunvent? Search for $0? Backup: Ask on list?

