# abborders

This app is used to provide list of water orders by lateral.  This is used by another application internally.

### Install and Setup
#### Windows:
* This app requires "ODBC Driver 17 for SQL Server"
* cd to apps directory
* git clone https://github.com/jcarter62/abborders
* cd abborders
* modify start_app.cmd, modify the directory if needed
* Create virtual environment with: python -m venv ./venv 
* Activate virtual environment: .\venv\Scripts\activate.bat
* Install libraries & requirements: pip install -r requirements.txt
* Start app: .\ 
* Add rule to firewall to allow port 5200, or the port specified in start_app.cmd


