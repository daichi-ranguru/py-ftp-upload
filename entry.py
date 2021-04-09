import os
from dotenv import load_dotenv
import ftplib

def missingValues(name): 
  raise AttributeError("Env '{}' value missing!".format(name))

envir = os.environ
load_dotenv(".env")
root = envir.get("UWF_ROOT") if envir.get("UWF_ROOT") is not None else missingValues("root")
ftpRoot = envir.get("UWF_FTP_FOLDER") if envir.get("UWF_FTP_FOLDER") is not None else "/"
excludeFolders = set(envir.get("UWF_EXCLUDE").split(",") if envir.get("UWF_EXCLUDE") is not None else [])
excludeFiles = ["upload-with-python.py"]


ftpConfig = {
  'server': envir.get("UWF_FTP_SERVER"), 
  'user': envir.get("UWF_FTP_USER"),
  'passw': envir.get("UWF_FTP_PASS")
}

for key in ftpConfig:
  if ftpConfig[key] is None:
    missingValues(key)

session = ftplib.FTP(ftpConfig["server"],ftpConfig["user"],ftpConfig["passw"])
session.cwd(ftpRoot)

print("Uploading started!")

for dname, dirs, files in os.walk(root, topdown=True):
  dirs[:] = [d for d in dirs if d not in excludeFolders] 
  files[:] = [f for f in files if f not in excludeFiles] 
  curFolder = dname.replace("./", "")
  print("Current folder: {}".format(curFolder))

  # change to current working folder
  if curFolder != "":
    toChange = ftpRoot + "/" + curFolder.replace('\\', '/')
    if session.pwd() is not (toChange):
      session.cwd(toChange)

  # create folder if does not exists
  if len(dirs) != 0:
    for dirName in [a for a in dirs if a not in session.nlst()]:
      session.mkd(dirName)

  for fname in files:
    fileName = os.path.join(dname, fname)
    session.storbinary(
      'STOR {}'.format(fname), 
      open(fileName, 'rb')
    )

print("Done! Stopping...")
session.quit()
print("Bye!")