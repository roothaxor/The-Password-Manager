# The Password Manager
<p align="center">
  <img width=260 height=63 src="http://orig06.deviantart.net/f419/f/2013/294/b/4/animated_3d_python_powered_logo120frame_apng_by_metallicow-d6rdza2.png">
</p><br />

 * Dont require internet ( Never worry for password leak online, unlike other password managers which promise to be safest softwares online, but trading your data for money ) 
 * Encrypts your stored password's with AES-256 Encryption ( Without Password not even you can see the Database )
 * Command line interface, Generates Strong & Random Password ( Cannot be guessed/brute forced )

## Installation Guide `Read Carefully`
Downloading The Password Manager tool
* [Download .zip file ( Direct Link )](https://codeload.github.com/roothaxor/The-Password-Manager/zip/master)
* Unzip it to `C:/passmanager/` or something ( New directory )

Installing "Python & Required modules"

* [Download Python 2.7](https://www.python.org/downloads/windows/)
* Install modules using command `pip install -r requirements.txt` 

#### Configuration
Open `CMD` run `python config.py`
```
thats should do the rest of configuration work!
Just enter the Main Password, Panic Password and CipherKey
Make sure CipherKey is 16 letter long
```
Remember: Config.py will require admin privilege because it is going to access the windows registry to add Key's for Right-Click access to Password Generator
##### Panic Password

Ok, incase you are forced to open the password manager, Enter the panic password
this will move your database file to C:\users\user\appdata\roaming
so password manager won't work untill you move that file back.

## ScreenShots
`Automated Configuration` </br>
> ![Alt text](https://github.com/roothaxor/The-Password-Manager/blob/master/Screenshots/config.png)


`Right-Click` </br>
> ![Alt text](https://github.com/roothaxor/The-Password-Manager/blob/master/Screenshots/right_click.png)


`Password Generation working process!` </br>
> ![Alt text](https://github.com/roothaxor/The-Password-Manager/blob/master/Screenshots/pass_gen.png)


`Login! ( Main/Panic Password ) ` </br>
> ![Alt text](https://github.com/roothaxor/The-Password-Manager/blob/master/Screenshots/pass_view.png)


`Inside of Password Viewer!` </br>
> ![Alt text](https://github.com/roothaxor/The-Password-Manager/blob/master/Screenshots/pass_view_example.png)
