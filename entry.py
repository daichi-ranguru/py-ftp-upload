from os import environ, path, walk
from pathlib import Path
from urllib.parse import urlparse, unquote
from sys import argv
from dotenv import load_dotenv
import ftplib

def missingValues(name): 
  raise AttributeError("Env '{}' value missing!".format(name))

if len(argv) != 2:
  raise ValueError("Command wrong. Should be like this: 'python <py_script> <root_folder_of_files>'")
root = Path(argv[1])
if root.exists() is False:
  raise ValueError("Specified root folder does not exist.")

load_dotenv("{}/.env".format(root))

excludeFolders = set(environ.get("UWF_EXCLUDE").split(",") if environ.get("UWF_EXCLUDE") is not None else [])
excludeFiles = ["upload-with-python.py"]

ftpConfig = {
  'server': environ.get("UWF_FTP_SERVER"), 
  'user': environ.get("UWF_FTP_USER"),
  'passw': environ.get("UWF_FTP_PASS"),
  'root': environ.get("UWF_FTP_FOLDER") if environ.get("UWF_FTP_FOLDER") is not None else "/"
}

for key in ftpConfig:
  if ftpConfig[key] is None:
    missingValues(key)

session = ftplib.FTP(ftpConfig["server"],ftpConfig["user"],ftpConfig["passw"])
session.cwd(ftpConfig["root"])

print("Uploading started!")

for dname, dirs, files in walk(root, topdown=True):
  dirs[:] = [d for d in dirs if d not in excludeFolders] 
  files[:] = [f for f in files if f not in excludeFiles] 
  ndname = Path(dname).as_uri()

  curFolder = ndname.replace(root.as_uri(), "")

  print("Current folder: {}".format(curFolder))
  # change to current working folder
  if curFolder != "":
    toChange = ftpConfig["root"] +  curFolder
    if session.pwd() is not (toChange):
      session.cwd(toChange)

  # create folder if does not exists
  if len(dirs) != 0:
    for dirName in [a for a in dirs if a not in session.nlst()]:
      session.mkd(dirName)

  # store files
  for fname in files:
    fileName = path.join(dname, fname)
    session.storbinary(
      'STOR {}'.format(fname), 
      open(fileName, 'rb')
    )
  

print("Done! Stopping...")
session.quit()
print("Bye!")
