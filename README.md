# Unchained
An open-source Django/MySQL/Apache/WSGI web application boilerplate/template, designed for use with AWS EC2.

### Features
* API and API pages
* Admin panel
* Code tests
* Static or dynamic site integration
* Deployment instructions for AWS EC2 Ubuntu server

### Future Features
* AWS RDS Implementation
* AWS Auto-scaling Group Implementation
* Auto-deploy via GitHub
* Deployment Scripts to automate the instructions below

### Todo: Dev Environment Setup

### Pre-deployment Prep
0. In `settings.py` change `DEBUG = True` to be `DEBUG = False`
0. Set new `SECRET_KEY` in `settings.py` ([recommended key generator](http://www.miniwebtool.com/django-secret-key-generator/))
0. Create new database user password ([recommended password generator](https://identitysafe.norton.com/password-generator/)) and put it in `init.sql` (inbetween the quotes after `IDENTIFIED BY`) and `settings.py` (under the `DATABASES` object find the property named `PASSWORD`). Note: You can also change the username and database names in these places if desired.
0. Add AWS server IP address and production domain names to `ALLOWED_HOSTS` array in `settings.py`

### Production Deployment
0. (Create AWS EC2 Ubuntu server and login via SSH)
0. Update server: `sudo apt-get update && sudo apt-get upgrade -y`
0. Install required server software: `sudo apt-get install python-pip python-dev build-essential git mysql-server libmysqlclient-dev`
0. Navigate to deployment folder: `cd /var/www`
0. Create "www" user group: `sudo groupadd www`
0. Add "ubuntu" user to "www" user group: `sudo usermod -a -G www ubuntu`
0. Exit console (`exit`) and reconnect to activate user changes.
0. Make "www" user group own the /var/www folder: `sudo chown -R root:www /var/www`
0. Set folder to 'everyone can execute and read but only owners/owner groups can write': `sudo chmod 2775 /var/www`
0. Set each subdirectory to the same permissions: `find /var/www -type d -exec sudo chmod 2775 {} \;`
0. Set each file to 'everyone can read but only owners/owner groups can write': `find /var/www -type f -exec sudo chmod 0664 {} \;`
0. Clone repo to folder: `git clone https://github.com/pbadeer/unchained.git .`
0. Setup bare minimum security on MySQL: `sudo mysql_secure_installation` ([recommended password generator](https://identitysafe.norton.com/password-generator/)
0. Open MySQL console: `sudo mysql -p`
0. Run MySQL setup script: `source init.sql`
0. Exit MySQL console: `\q`
0. Install virtual environment wrapper: `sudo pip install virtualenvwrapper`
0. Add virtual environment info to terminal config (part 1): `sudo echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.bashrc`
0. Add virtual environment info to terminal config (part 2): `sudo echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc`
0. Reload terminal: `source ~/.bashrc`
0. Create virtual environment called "unchained": `mkvirtualenv unchained --no-site-packages`
0. Load the virtual environment called "unchained": `workon unchained`
0. Install required python packages: `pip install -r requirements.txt`
0. Move Django static files to your static folder: `python manage.py collectstatic`
0. Copy Apache configuration into proper folder: `cp unchained.conf /etc/apache2/sites-available/`
0. Enable Apache site: `sudo a2ensite unchained.conf`
0. Disable default Apache site: `sudo a2dissite 000-default.conf`
0. Reload Apache config: `sudo service apache2 reload`
0. Restart Apache: `sudo service apache2 restart`

#### Troubleshooting
* View Apache error log with: `tail /var/log/apache2/error.log`