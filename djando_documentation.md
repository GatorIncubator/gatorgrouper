#### Django

Django is a free and open source web application framework that is written in Python and helps to implement websites in a convenient manner. With the collection of modules embedded within its framework, development is made easier and one would not have to work on creating the website from scratch but just use the components that are already built within which saves a lot of time. Acknowledging the fact that we have a short span of time to work on the GatorGrouper project, we decided to use Django as it provides the developer with simpler tools to grasp the project's structure. In addition to this, it supports Object-Relational Mapping, which allows the user to create a bridge between the data model and the database engine, and supports a large set of database systems including SQLite.

#### Running

After the successful installation of Django, we inclined towards running the application. In order to run the application smoothly, please make sure that you are in the correct directory which is GatorGrouper_Django.

Next, make sure to run this command in the terminal: `python manage.py runserver`

To check if your server is set up and running, open up your browser and type: `local host:80000`

#### Design and Configuration

The web applications in Django have access to the data and manage it through objects in Python which are referred to as models. A model is a special type of object that is saved in the database. It defines the structure of the stored data, includes the field types along with their size if possible, and contains behaviors of the data that is being stored. After creating the model structure for the project, Django handles all the communication that goes within.

The Django web framework comes with a built-in object-relational mapping module, ORM, which allows interaction with the database in an object-oriented setup. Prior to dealing with ORM, we define model classes that translate to data tables and the relation between them. For the GatorGrouper project, we created six classes entitled as: Professor, Classes, Assignment, Students, Traits, and Grouped Students. In order to establish a relationship between these classes, we define foreign keys using `django.db.models.ForeignKey`. The different entities within the classes are linked by a means one-to-many, many-to-one, and many-to-many relationship.
