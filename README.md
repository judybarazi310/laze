
## This is a tutorial on how to setup your virtual environment and to view your project locally. Although this is long, the steps to view the current project should be very clear. At the end, I provide an example using my folder structure. Please message Anthony Sukadil or anyone from backend on Slack if you are struggling with setting this up. ##
----------------------------------------------------------------------------------
#### 1. Install the latest version of Python, Python 3.7.1 at https://www.python.org/downloads/release/python-371/ ####
#### 2. I use Git Bash, so for this tutorial, install Git Bash at https://git-scm.com/downloads
#### 3. Open Git Bash and type in the following command:
    pip install virtualenv
#### 4. Change your current directory to a directory where you'd like to have your virtual environment. I would keep it in a CP317 folder:
    cd your/directory/here/CP317
#### 5. Create the virtual environment using the command:
    python -m venv venv-laze
#### 6. From here activate your newly created virtual environment:
    source venv-laze/Scripts/activate
#### 6a. You can check if you're in your virtual environment by calling the command: ####
    python -m pip list
### and noting that the only packages installed are pip 10.0.1 and setuptools 39.0.1
    Package    Version
    ---------- -------
    pip        10.0.1
    setuptools 39.0.1
#### or by looking at the terminal with the following lines: ####
    (venv-laze)
    your/current/working/directory
#### 7. Install Django using the following command in your virtual environment: ####
    pip install django==2.1.2
#### Again, check using step 6a and you should see Django installed.
#### 8. From here, go to the directory where the project exists: ####
    cd directory/where/you/pulled/laze/Web/laze
#### 9. Run the command: ####
    python manage.py runserver 
#### 10. You'll see in your terminal the following message: ####

	Performing system checks...

	System check identified no issues (0 silenced).
	DATE HERE AND TIMESTAMP
	Django version 2.1.2, using settings 'laze.settings'
	Starting development server at http://127.0.0.1:8000/
	Quit the server with CTRL-BREAK

#### 11. Now go to the url 'http://127.0.0.1:8000/' and you can view the map. For login, go to 'http://127.0.0.1:8000/accounts/login'. ####

#### 12. When you want to quit the server, in your console, press CTRL-C. ####
#### 13. To get out of your virtual environment, call the following command in your terminal: ####
    deactivate
----------------------------------------------------------------------------------

#### For my folder structure, I have the following directories: ####
    C:/Users/Anthony/Documents/cp-master/CP317/laze
    C:/Users/Anthony/Documents/cp-master/CP317/venv-laze
#### These are the commands to run the server using my folder structure on Windows and I have skipped the steps to create the virtual environment and install Django since it should be very clear: ####
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
