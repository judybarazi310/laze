## For those who don't know how to run our project locally and would like to see what it looks like right now, in 'Web/laze', there is a file named 'manage.py' that you can run using your virtual environment. At the end, I will demonstrate using my folder structure using Git Bash. ##

#### 1. Make sure you have the correct version of Django installed, version 2.1.2 in your virtual environment. ####
#### 2. In Git Bash, change your directory using: ####
    cd virtual/environment/directory/here
#### Once in this directory, run the virtual environment by calling the command: ####
    source Scripts/activate
#### You can check if you're in your virtual environment by calling the command: ####
    python -m pip list
#### or by looking at the terminal with the following lines: ####
    (virtual_env_name_here)
    your/current/working/directory
#### 3. From here, we go to the directory where the project exists: ####
    cd directory/where/you/pulled/laze/Web/laze
#### 4. From here, run the command: ####
    python manage.py runserver 
#### 5. You'll see in your terminal the following message: ####
----------------------------------------
	Performing system checks...

	System check identified no issues (0 silenced).
	DATE HERE AND TIMESTAMP
	Django version 2.1.2, using settings 'laze.settings'
	Starting development server at http://127.0.0.1:8000/
	Quit the server with CTRL-BREAK

#### 6. Now go to the url 'http://127.0.0.1:8000/' and you can view the map. For login, go to 'http://127.0.0.1:8000/accounts/login'. ####

#### 7. When you want to quit the server, in your console, press CTRL-C. ####
#### 8. To get out of your virtual environment, call the following command in your terminal: ####
    deactivate
    
#### For my folder structure, I have the following directories: ####
    C:/Users/Anthony/Documents/cp-master/CP317/laze
    C:/Users/Anthony/Documents/cp-master/CP317/venv-laze
#### These are the commands to run the server using my folder structure on Windows: ####
    Anthony@Anthony-PC MINGW64 ~
    $ cd Documents/cp-master/CP317/venv-laze/
    
    Anthony@Anthony-PC MINGW64 ~/Documents/cp-master/CP317/venv-laze
    $ source Scripts/activate
    (venv-laze)
    Anthony@Anthony-PC MINGW64 ~/Documents/cp-master/CP317/venv-laze
    $ cd ..
    (venv-laze)
    Anthony@Anthony-PC MINGW64 ~/Documents/cp-master/CP317
    $ cd laze/Web/laze/
    (venv-laze)
    Anthony@Anthony-PC MINGW64 ~/Documents/cp-master/CP317/laze/Web/laze (master)
    $ python manage.py runserver
    Performing system checks...

    System check identified no issues (0 silenced).
    November 21, 2018 - 22:44:00
    Django version 2.1.2, using settings 'laze.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.
    
    (venv-laze)
    Anthony@Anthony-PC MINGW64 ~/Documents/cp-master/CP317/laze/Web/laze (master)
    $ deactivate
    
    Anthony@Anthony-PC MINGW64 ~/Documents/cp-master/CP317/laze/Web/laze (master)
    $ 
