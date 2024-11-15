This set of files is used to monitor network traffic and upload the pcaps to a NAS for inspection.
pytrace.py performs a constant packet capture and saves the file to the PCAPS folder every hour.
watchfile.py  watches the PCAPS folder and when a file is created in it, uploads it to the NAS at our office.
