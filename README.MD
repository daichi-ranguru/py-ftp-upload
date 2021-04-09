# Upload files via ftp protocol

This is a useful py script for those who struggled on repeatedly uploading files to webhosting via some ftpclient.<br/>

## Usage

**U have to have installed python on your machine first**
<br/>
<br/>
1. Create or download this project and save it whenever you want
1. Set .env like this:
  * UWF_FTP_SERVER **(is for server url, required)**
  * UWF_FTP_USER **(is for ftp user, required)**
  * UWF_FTP_PASS **(is for ftp password, required)**
  * UWF_FTP_FOLDER **(specifies folder in which files will be stored, optional, default is "/")**
  * UWF_ROOT **(specifies starting point folder form find and upload, optional, default is "./")**
  * UWF_EXCLUDE **(specifies folder names that those should be excluded from uploading (multiple options devide by ','), optional, default is [])**
1. Run the py script
1. Watch it go and end!