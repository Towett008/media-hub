### Media Hub
Media sharing platform that has role based access
- teacher role -  manage assigned student content
- student role - share media uploads
- admin role - overseeing all content and managing the platform

### tools of use
- django
- python libraries (ready made snippets for a asa specific job)
    - pillow : allow media transaction in python frameworks (absolute media url, )
    -cloudinary : media storage and also url acccess generation (url -> save to database for an upload)
    - python-decaouple : media tracks

### Apps in projects
    - accounts : authentication and authorization (signups, login, forgot password)
    - media_assests : upload tasks, display, updates

### steps
- install the libraries:
    pip install libraryname
    pip install -r requiments.txt
- create our apps
- configure our project settings
    - register our apps
    - register cloudinary (give the cloudinary configs)
    - register a custom authentication process
    - emails registry
    - 

### Authentication and Authorization (accounts.py)
Authentication - identity identification , who are you ?
Authorizatiuon - access priviledges - role based authorization, token based authorization

1. Create our custom user model
2. Extend the intergrate form captures -forms.py
3. Create the views action for registration and login , logout and profile view , 
custompasswordresetview , custompasswordresetconfirmview - views.py
4. Register the views actions as URL route - urls.py 
5. Register the models for admin to use and manage content on - admin.py
6. Register the apps url to the projects urls - project/urls.py
7. Create the templates 
   - create a templates folder - within the app 
   - create a global templates folder - register it's configuration in the settings.py file 
   8. Make databases migrations and then populate the templates 
   python manage.py makemigrations 
   python manage.py migrate


   ### Template creation
1. Configuration level file : base.html 
   - Defining your blocks : title , extra_css , content (most important) , footer, extra_js
   - Linking to global stylesheet / style lib. (bootstrap)
   - Link to global js files 

2. Create other pages by simply extending the configs done on 1.
populate what is dynamic using the block.

## MVT -Model View Templates
### Media Assests app views
'''
1. Dashboard view : this allows my user to see uploaded items set as public
2. My Media : this allows users to see only their uploads
3. Uploaded media view : this allows users upload media
4. Edit media view : this  allolws user to edit uploaded data
5. Delete media view : this allolws user to delete their uploaded media 
6. Media Detail view : this allows users to see al their details for a media
'''

### Configuring our enviromental variables
1. Create a .env file for development purposes - store your info as a variable refrence
create a .gitignore file for github push purposes - include .env as one of the ignored files .This abstracts sensitive info from the main application code.
