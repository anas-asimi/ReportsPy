import yaml


# Read YAML file
with open("config/settings.yaml", "r") as stream:
    data_loaded = yaml.safe_load(stream)


host, port, username, password = data_loaded["ftp"].values()
files_paths = data_loaded["files paths"]
