# Directory Scanner

A simple Python script that scans a folder and shows details about every file and subfolder inside it - size, extension, and last modified date.

## What it does

You give it a folder path, and it walks through all the files and folders inside (including subfolders), then:

- Prints a report to the screen showing whether each item is a file or folder, its size (in B, KB, MB, or GB), its extension, and when it was last modified
- Saves the same report to a text file called `scan_result.txt`

At the end it also shows totals - how many folders, how many files, and the combined size.

## How to run it

```bash
python main.py
```

It'll ask you for a folder path. You can type one in, or just hit Enter to scan the folder you're currently in.

## How it's built

- `FileEntry` - holds the info for one file or folder (size, extension, date)
- `DirectoryScanner` - walks through the folder, creates a `FileEntry` for everything it finds, and builds the report. The same report is used both to print to the screen and to save to the text file, so they always match.

## Example Output

```
Directory Scan Report
Root: C:\Users\HP\OneDrive - FAST National University\Desktop\INTERNSHIP\TASK 1
Generated: 2026-07-09 15:38:27
==========================================================================================
[FILE] main.py                                            size=    4.4 KB  ext=.py       modified=2026-07-09 15:36:31
[FILE] scan_result.txt                                    size=   622.0 B  ext=.txt      modified=2026-07-09 15:38:07
==========================================================================================
Total folders: 0
Total files:   2
Total size:    5,103 bytes
```
