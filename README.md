What I Should Watch
===================


Installation & Configuration
----------------------------

PHP: don't use PHP 7

1. Go to the folder `Symfony/app/config/`
2. Copy the file `parameters.yml.dist` and save it as `parameters.yml`
3. Update `Symfony/app/config/parameters.yml` to reflect
your MySQL installation.
4. Once done, from the Symfony directory :

```Bash
     php app/console doctrine:database:create
     php app/console doctrine:generate:entities Tuto
     php app/console doctrine:generate:entities \
         Tuto/TestBundle
     php app/console doctrine:schema:update --force
```
Ref: http://symfony.com/doc/2.7/doctrine.html



Python Scripts to populate the database
----------------------------------------

There are five scripts for the five tables.  You will need the python library mySQLdb installed
 for them to work. 

Run the first script in your terminal by typing

     ```python bin/python populate_database_film.py```

in the terminal. The script will prompt you for your mySQL password and then your SQL port number.

You can then run the scripts to populate the writer and director tables:

     ```python bin/python populate_database_writers.py```

     ```python bin/python populate_database_directors.py```

You can then run the scripts to populate the connector tables:

     ```python bin/python populate_database_writerfilm.py```

     ```python bin/python populate_database_directorfilm.py```


Symfony Variables
-----------------
Variables used for database data (and so have to be changed if the database is changed), are located in:

-Symfony/src/tuto/entity/films.php
-Symfony/src/tuto/testbundle/controller/defaultcontroller
result.
