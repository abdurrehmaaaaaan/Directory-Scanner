import os
from pathlib import Path
from datetime import datetime


class FileEntry:
    # file metadata

    def __init__(self, path: Path, is_dir: bool):
        self.path = path
        self.is_dir = is_dir
        self.size = 0 if is_dir else self._get_size()
        self.extension = "" if is_dir else path.suffix.lower()
        self.last_modified = self._get_last_modified()

    def _get_size(self) -> int:
        # get size
        try:
            return self.path.stat().st_size
        except OSError:
            return -1

    def _get_last_modified(self) -> str:
        # get date
        try:
            timestamp = self.path.stat().st_mtime
            return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
        except OSError:
            return "unknown"

    def format_size(self) -> str:
        # readable size
        if self.is_dir:
            return "<DIR>"
        size = self.size
        for unit in ("B", "KB", "MB", "GB"):
            if size < 1024:
                return f"{size:.1f} {unit}"
            size /= 1024
        return f"{size:.1f} TB"

    def to_line(self, relative_to: Path) -> str:
        # format line
        kind = "DIR " if self.is_dir else "FILE"
        rel_path = self.path.relative_to(relative_to)
        ext = self.extension if self.extension else "-"
        return (
            f"[{kind}] {str(rel_path):<50} "
            f"size={self.format_size():>10}  "
            f"ext={ext:<8}  "
            f"modified={self.last_modified}"
        )


class DirectoryScanner:
    # scan folder

    def __init__(self, root_path: str):
        self.root_path = Path(root_path).resolve()
        self.entries = []

        if not self.root_path.exists():
            raise FileNotFoundError(f"Path does not exist: {self.root_path}")
        if not self.root_path.is_dir():
            raise NotADirectoryError(f"Not a directory: {self.root_path}")

    def scan(self):
        # walk tree
        self.entries = []
        for current_root, dirs, files in os.walk(self.root_path):
            current_path = Path(current_root)

            for d in dirs:
                self.entries.append(FileEntry(current_path / d, is_dir=True))

            for f in files:
                self.entries.append(FileEntry(current_path / f, is_dir=False))

        return self.entries

    def summary(self) -> dict:
        # totals
        total_files = sum(1 for e in self.entries if not e.is_dir)
        total_dirs = sum(1 for e in self.entries if e.is_dir)
        total_size = sum(e.size for e in self.entries if not e.is_dir and e.size > 0)
        return {
            "total_files": total_files,
            "total_dirs": total_dirs,
            "total_size_bytes": total_size,
        }

    def build_report_lines(self) -> list:
        # build lines
        if not self.entries:
            self.scan()

        summary = self.summary()
        lines = []

        lines.append("Directory Scan Report")
        lines.append(f"Root: {self.root_path}")
        lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append("=" * 90)

        for entry in sorted(self.entries, key=lambda e: (not e.is_dir, str(e.path))):
            lines.append(entry.to_line(self.root_path))

        lines.append("=" * 90)
        lines.append(f"Total folders: {summary['total_dirs']}")
        lines.append(f"Total files:   {summary['total_files']}")
        lines.append(f"Total size:    {summary['total_size_bytes']:,} bytes")

        return lines

    def print_report(self):
        # show results
        lines = self.build_report_lines()
        for line in lines:
            print(line)

    def save_report(self, output_path: str = "scan_result.txt"):
        # write file
        lines = self.build_report_lines()
        with open(output_path, "w", encoding="utf-8") as f:
            for line in lines:
                f.write(line + "\n")
        return output_path


def main():
    # run scan
    target = input("Enter folder path to scan (leave blank for current directory): ").strip()
    target = target if target else "."

    try:
        scanner = DirectoryScanner(target)
        scanner.scan()
        scanner.print_report()
        output_file = scanner.save_report("scan_result.txt")
        print(f"\nReport saved to: {output_file}")

    except (FileNotFoundError, NotADirectoryError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
