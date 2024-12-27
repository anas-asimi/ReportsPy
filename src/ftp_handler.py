from ftplib import FTP, error_perm, error_temp, error_proto, error_reply
from datetime import datetime
from io import StringIO


def connect_to_ftp(host, port, username, password=""):
    print(f"Connecting to ftp://{username}@{host}:{port}")
    ftp = FTP()
    try:
        ftp.connect(host, port)
        print("Connected successfully.")
        ftp.login(user=username, passwd=password)
        print("Logged in successfully.")
        return ftp
    except (error_perm, error_temp, error_proto, error_reply) as ftp_error:
        print(f"FTP error: {ftp_error}")
        raise
    except ConnectionRefusedError:
        print("Error: Connection refused. Check if the FTP server is reachable.")
        raise
    except TimeoutError:
        print("Error: Connection timed out. Check your network and server status.")
        raise
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise
    finally:
        if "ftp" in locals() and ftp.sock is None:
            print("Closing connection.")
            ftp.quit()


# def download_file(ftp, remote_path):
#     local_path = remote_path + "-" + datetime.now()
#     print(local_path)
#     return
#     with open(local_path, "wb") as f:
#         ftp.retrbinary(f"RETR {remote_path}", f.write)
#     return local_path


def read_file(ftp, filepath, start_line=1, end_line=-1):
    print(f"Reading {filepath}")
    # Retrieve the file content
    lines = []
    ftp.retrlines(f"RETR {filepath}", lines.append)

    # Return the specified range of lines
    return lines[start_line:end_line]
