#!/usr/bin/env python3

from src.pdf_generator import generate_pdf


# Example usage:
output_file = "output.pdf"
file_path = "./template/report.html"
generate_pdf(output_file, file_path)
