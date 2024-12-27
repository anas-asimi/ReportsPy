#!/usr/bin/env python3

from pdf_generator import generate_pdf
from ftp_handler import connect_to_ftp, read_file
from utils import line_to_obj, save_dict
from yaml_handler import (
    host,
    port,
    username,
    files_paths,
    json_path,
    pdf_path,
    html_path,
    BENI_AMMIR_STATIONS,
    BENI_MOUSSA_STATIONS,
)

# # connecting to ftp
# ftp = connect_to_ftp(host, port, username)

# # reading data from ftp
# data = {
#     "BENI AMMIR": [],
#     "BENI MOUSSA": [],
# }
# for name, path in files_paths.items():
#     # reading last lines
#     station_lines = read_file(ftp, path, -8, -1)
#     # converting lines to objs
#     station_data = list(map(line_to_obj, station_lines))
#     # Storing the objs
#     if name in BENI_AMMIR_STATIONS:
#         data["BENI AMMIR"].append({"records": station_data, "name": name})
#     if name in BENI_MOUSSA_STATIONS:
#         data["BENI MOUSSA"].append({"records": station_data, "name": name})

# # saving data to json file
# save_dict(data, json_path)

# creating the pdf
generate_pdf(pdf_path, html_path)


# ✅ Connecting to ftp
# ✅ Fetching data from ftp
# ✅ Generating json
# ❌ visulization
# ✅ exporting to pdf
