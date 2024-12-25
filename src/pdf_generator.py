#!/usr/bin/env python3
import subprocess
import time


def generate_pdf(output_file, url):
    start_time = time.time()  # Start the timer

    command = [
        "google-chrome-stable",
        "--headless",
        "--disable-gpu",
        f"--print-to-pdf={output_file}",
        url,
    ]

    result = subprocess.run(command, capture_output=True, text=True)

    end_time = time.time()  # End the timer
    elapsed_time = end_time - start_time  # Calculate the elapsed time

    if result.returncode == 0:
        print(f"PDF successfully generated: {output_file}")
    else:
        print(f"Failed to generate PDF. Error: {result.stderr}")

    print(f"Time taken: {elapsed_time:.2f} seconds")


# Example usage:
# output_file = "output.pdf"
# file_path = "./template/report.html"
# generate_pdf(output_file, file_path)
