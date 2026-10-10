"""Regression tests for publication integrity rules."""

import tempfile
import unittest
from pathlib import Path

from pypdf import PdfWriter

from scripts.validate_publication import validate_publication


class PublicationIntegrityTests(unittest.TestCase):
    def test_missing_file_is_error(self):
        self.assertTrue(validate_publication(Path("does-not-exist.pdf")))

    def test_invalid_signature_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "invalid.pdf"
            path.write_bytes(b"X" * 2048)
            self.assertIn("signature", str(validate_publication(path)))

    def test_valid_multipage_pdf_is_accepted(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "valid.pdf"
            writer = PdfWriter()
            for _ in range(3):
                writer.add_blank_page(width=612, height=792)
            with path.open("wb") as handle:
                writer.write(handle)
            self.assertEqual(validate_publication(path, min_pages=3), [])
            self.assertTrue(validate_publication(path, min_pages=5))


if __name__ == "__main__":
    unittest.main()
