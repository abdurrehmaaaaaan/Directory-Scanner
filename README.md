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
Directory Scan Report
Root: /home/user/project
Generated: 2026-07-09 10:16:17
==========================================================================================
 
[DIR ] sub1                                               size=     <DIR>  ext=-         modified=2026-07-09 10:16:14
[FILE] file1.txt                                          size=    12.0 B  ext=.txt      modified=2026-07-09 10:16:14
[FILE] sub1/script.py                                     size=    12.0 B  ext=.py       modified=2026-07-09 10:16:14
 
==========================================================================================
Total folders: 1
Total files:   2
Total size:    24 bytes
```
 
## Project structure
 
```
directory-scanner/
├── directory_scanner.py   # main script
└── README.md
```
