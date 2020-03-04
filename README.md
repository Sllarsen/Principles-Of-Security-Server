## Dev Notes 
### Python virtual enviroment (Python3)
Virtual enviroments are built into Python3, and are used to localize and better keep track of dependencies. Before installing any pip libraries make sure that you are running your virtual enviroment, and pip them to requirements.txt if you want to save them. 

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


