# Upload files via ftp protocol

This is a useful py script for those who struggled on repeatedly uploading files to webhosting via some ftpclient.<br/>

## Usage

**U have to have installed python on your machine first**
<br/>
<br/>
1. Install this project on your machine globally
1. Set .env in your project which will be sent like this:
    1. UWF_FTP_SERVER **(is for server url, required)**
    1. UWF_FTP_USER **(is for ftp user, required)**
    1. UWF_FTP_PASS **(is for ftp password, required)**
    1. UWF_FTP_FOLDER **(specifies folder in which files will be stored, optional, default is "/")**
    1. UWF_ROOT **(specifies starting point folder form find and upload, optional, default is "./")**
    1. UWF_EXCLUDE **(specifies folder names that those should be excluded from uploading (multiple options devide by ','), optional, default is [])**
1. Run this "npm run upload < your_root_folder_to_upload >"
1. Watch it go and end!
