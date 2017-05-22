# The Password Manager
 * Dont require internet ( Never worry for password leak online, unlike other password managers which promise to be safest softwares online, but trading your data for money ) 
 * Encrypts your stored password's with AES-256 Encryption ( Without S-key not even you can see the Database )
 * Command line interface
 * Generates Strong & Random Password ( Cannot be guessed/brute forced )

## Installation Guide `Read Carefully`
Downloading The Password Manager tool
* [Download .zip file ( Direct Link )](https://codeload.github.com/roothaxor/The-Password-Manager/zip/master)

Installing "Python + Required modules"

* [Download Python 2.7](https://www.python.org/downloads/windows/)
* Install modules using command `pip install -r requirements.txt` ( Make sure you are in " C:/tools/pass/ " directory to use pip command

Creating "Directory"

```
Goto C:/
Create Folder named `tools`
Goto tools folder and create Folder named `pass`
Goto pass folder and extract .zip file there

ie: Extract files in C:/tools/pass/
```
Adding `Generate Password` option to mouse right click button

``` 
Open `registry-file` folder and run regadd.reg
```
#### Configuration
Goto __files folder edit author.py
mostly change only these, if you are going to change the cipher key. you will have to delete the jesus.db and create a new one
why? - jesus.db with this tool is already encrypted using cipher in author.py

```
example:
ionfdsnfdisncdscnso = 'password'
panicpassword = 'roothaxor'
```
##### Panic Password

Ok, incase you are forced to open the password manager, Enter the panic password
this will move your database file to C:\users\user\appdata\roaming
so password manager won't work untill you move that file back.

## ScreenShots
#### Right-Click :
![Screenshot](https://raw.githubusercontent.com/roothaxor/The-Password-Manager/master/Screenshots/screenshot_1.png)
#### Command line interface :
![Screenshot](https://raw.githubusercontent.com/roothaxor/The-Password-Manager/master/Screenshots/Screenshot_2.png)
#### Generating password, recording the reason for password
![Screenshot](https://raw.githubusercontent.com/roothaxor/The-Password-Manager/master/Screenshots/Screenshot_3.png)
#### To access the database
![Screenshot](https://raw.githubusercontent.com/roothaxor/The-Password-Manager/master/Screenshots/Screenshot_4.png)
#### Database-view.bat :)
![Screenshot](https://raw.githubusercontent.com/roothaxor/The-Password-Manager/master/Screenshots/Screenshot_5.png)
#### Example of Database after login
![Screenshot](https://raw.githubusercontent.com/roothaxor/The-Password-Manager/master/Screenshots/Screenshot_6.png)
#### Here is an view of Password file ( AES Encrypted )
![Screenshot](https://raw.githubusercontent.com/roothaxor/The-Password-Manager/master/Screenshots/Screenshot_7.png)
