import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import paramiko
from scp import SCPClient
from dotenv import load_dotenv
import os

# Define the directory to watch
DIRECTORY_TO_WATCH = "PCAPS"

# Define a function to run when a file is saved
def process_new_file(file_path):
    print(f"File saved: {file_path}")
    # Add additional processing code here
    # time.sleep(5)
    scp_upload(file_path)

# Define the event handler for the directory
class WatcherHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # Only respond to files, not directories
        if not event.is_directory:
            process_new_file(event.src_path)

    def on_created(self, event):
        # Only respond to files, not directories
        if not event.is_directory:
            process_new_file(event.src_path)


def scp_upload(fileName):

    hostname = os.getenv('serverNas')
    port = 22
    username = os.getenv('userName')
    password = os.getenv('passWord')

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, port=port, username=username, password=password)

    sftp = ssh.open_sftp()
    file_name = fileName.split("/")
    print(file_name[7])
    sftp.put(f'{fileName}', f'array1/Temp/{file_name[7]}')
    sftp.close()
    ssh.close()

# Set up the observer and start watching
if __name__ == "__main__":
    event_handler = WatcherHandler()
    observer = Observer()
    observer.schedule(event_handler, path=DIRECTORY_TO_WATCH, recursive=False)
    
    print(f"Watching directory: {DIRECTORY_TO_WATCH}")
    observer.start()

    try:
        while True:
            time.sleep(1)  # Keeps the program running
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
