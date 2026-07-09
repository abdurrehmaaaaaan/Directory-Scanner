 Directory Scanner
 
A Python CLI tool that recursively scans a folder and reports on every file and
subfolder it contains: size, extension, and last modified date. Results are
saved to a `.txt` report.
 
## Concepts used
- OOP: `FileEntry` (represents one scanned item) and `DirectoryScanner`
  (walks the tree, builds entries, writes the report) — separation of concerns,
  encapsulated formatting logic.
- File handling: `pathlib.Path`, `os.walk`, writing to disk with `open()`.
- Exception handling: invalid/missing paths raise clear errors instead of
  crashing.
## Usage
 
```bash
python directory_scanner.py
```
 
You'll be prompted for a folder path (leave blank to scan the current
directory). A report is written to `scan_result.txt` in the working directory.
 
### Example output
 
```
Enter folder path to scan (leave blank for current directory): 

Scan complete.
Folders: 1339  Files: 6933  Total size: 720,961,988 bytes
Report saved to: scan_result.txt
```
 
## Project structure
 
```
Directory Scanner/
├── main.py   
└── README.md
```
