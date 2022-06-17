#Day4
Install Xampp
change directory to downloads
chmod +x ....installer.run
./...installer.run

manage server 
>start the operation
>configure the port mysql to 81 and apache to 3305
>start all operation

goto
http://127.0.0.1:81/
http://localhost/phpmyadmin

create databases
create table 
save

create html file , views.py, setting.py and urls.py

python manage.py runserver

pip install firebase-admin
pip install python-firebase
pip install git+https://github.com/ozgur/python-firebase


 conection to firebase
#pip install firebase-admin
from firebase import firebase 
fb_app = firebase.FirebaseApplication('https://gas-lekage-detection-default-rtdb.firebaseio.com/', None)
#get data from the firebase and stored on result
result = fb_app.get('/', None)
print(result)
