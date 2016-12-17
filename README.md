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


