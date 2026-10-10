"""Validate book PDF readability, page count and geometric page integrity."""

from __future__ import annotations

import argparse
from pathlib import Path

from pypdf import PdfReader


def validate_publication(path: Path, min_pages: int = 10) -> list[str]:
    errors: list[str] = []
    if not path.is_file() or path.stat().st_size < 1024:
        return ["PDF missing or implausibly small"]
    try:
        with path.open("rb") as file:
            if file.read(5) != b"%PDF-":
                return ["PDF signature missing"]
        reader = PdfReader(str(path), strict=False)
        if reader.is_encrypted:
            return ["publication PDF is encrypted; cannot verify pages"]
        count = len(reader.pages)
        if count < min_pages:
            errors.append(f"PDF has {count} pages; expected at least {min_pages}")
        # Sample first, middle and last page; a full render is a separate visual QA.
        for index in sorted({0, count // 2, count - 1}) if count else []:
            page = reader.pages[index]
            box = page.mediabox
            if float(box.width) <= 0 or float(box.height) <= 0:
                errors.append(f"page {index + 1} has non-positive page dimensions")
    except Exception as exc:  # PDF parser may raise multiple format-specific exceptions
        errors.append(f"PDF could not be parsed: {type(exc).__name__}: {exc}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--min-pages", type=int, default=10)
    args = parser.parse_args()
    issues = validate_publication(args.pdf, min_pages=args.min_pages)
    for issue in issues:
        print("ERROR:", issue)
    if issues:
        return 1
    print(f"PDF structure and sampled page dimensions verified: {args.pdf}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
