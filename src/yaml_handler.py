import yaml


# Read YAML file
with open("settings.yaml", "r") as stream:
    settings = yaml.safe_load(stream)


host, port, username, password, files_paths = settings["ftp"].values()
json_path = settings["json path"]
pdf_path = settings["pdf path"]
html_path = settings["html path"]

BENI_AMMIR_STATIONS = settings["BENI AMMIR STATIONS"]
BENI_MOUSSA_STATIONS = settings["BENI MOUSSA STATIONS"]
