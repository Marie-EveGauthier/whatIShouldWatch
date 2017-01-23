What I Should Watch
===================


Installation & Configuration
----------------------------

PHP: don't use PHP 7

Update Symfony/app/config/parameters.yml to reflect
your MySQL installation.

Once done, from the Symfony directory:

     php app/console doctrine:database:create
     php app/console doctrine:generate:entities Tuto
     php app/console doctrine:generate:entities \
         Tuto/TestBundle
     php app/console doctrine:schema:update --force

Ref: http://symfony.com/doc/2.7/doctrine.html



Python Scripts
--------------

Python scripts can be found in the folder /bin

There are two scripts, one is called database_populate.py and one is called database.py
You will not need database.py, it is the script I used to create a table in the database using python.
For the official version we have used phpmyadmin to create the table.

Use database_populate.py to fill the database with the real data. You will need
the python library mySQLdb installed for it to work. Run the script in your terminal
by typing
     ```bin/python database_populate.py```

in the terminal. The script will prompt you for your mySQL password. If it works correctly,
the script should insert 3 columns of data into the database: title, year, and bechdel test



Symfony Variables
-----------------
Variables used for database data (and so have to be changed if the database is changed), are located in:

-Symfony/src/tuto/entity/films.php
-Symfony/src/tuto/testbundle/controller/defaultcontroller
result.
