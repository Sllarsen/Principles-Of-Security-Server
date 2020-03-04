## Dev Notes 
### Python virtual enviroment (Python3)
Virtual enviroments are built into Python3, and are used to localize and better keep track of dependencies. Before installing any pip libraries make sure that you are running your virtual enviroment, and pip them to requirements.txt if you want to save them. 

## Install on Mac / Linux

1. Creating virtual enviroment in local dir named "env"
```
$ python3 -m venv env 
```

2. Starting virtual enviroment "env" 
```
$ source env/bin/activate
```

3. Installing dependencies while in "env"
```
$ pip3 install -r requirements.txt 
```

3.5 Piping current pip installs to requirements.txt
```
$ pip3 freeze > requirements.txt 
```

4. Exiting virtual enviroment
```
$ deactivate
```

## Install on Windows using Gitbash

1. Creating virtual enviroment in local dir named "env"
```
$ python -m venv env
```

2. Starting virtual enviroment "env" 
```
$ source env/Scripts/activate
```

3. Installing dependencies while in "env"
```
$ pip install -r requirements.txt 
```

3.5 Piping current pip installs to requirements.txt
```
$ pip freeze > requirements.txt 
```

4. Exiting virtual enviroment
```
$ deactivate
```
 ## Running Server
 
1. Example of it activated

![alt text](https://github.com/Sllarsen/Principals-Server/blob/master/resources/readmepics/activate.png)

2. Navigate to where app.py is. This is the server and run
'''python ./app.py'''

![alt text](https://github.com/Sllarsen/Principals-Server/blob/master/resources/readmepics/activate%20server.png)

3. Request route (Postman was used)

![alt text](https://github.com/Sllarsen/Principals-Server/blob/master/resources/readmepics/setuppostman.gif)

4. After request, you can see the request in the terminal

![alt text](https://github.com/Sllarsen/Principals-Server/blob/master/resources/readmepics/request.png)
