# 0X00. AirBnB Clone - The Console

## Learning Objectives

- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is \*args and how to use it
- What is \*\*kwargs and how to use it
- How to handle named arguments in a function

### General

 This project will be our first venture into creating and maintaining our
 own website. The concepts we will need to learn in the process are, among others:

- Console
- HTML
- MySQL
- Fabric
- Flask

#### Capabilities:
- Creates new objects (i.e. a new User)
- Retrieves objects from a file, database etc...
- Perform operations on objects (count, compute stats, etc...)
- Modify object attributes
- Destroy objects

## Table of Content
- [Environment](#environment)
- [Installation](#installation)
- [File Descriptions](#file-descriptions)
- [Usage](#usage)
- [Examples of use](#examples-of-use)
- [Bugs](#bugs)
- [Authors](#authors)
- [License](#license)

## Environment
Written and tested in Python3 (v3.4.3) on Ubuntu 14.04 LTS

## Installation
- Clone Me! `git clone "https://github.com/dhreyes/AirBnB_clone`
- Access Me! `cd AirBnB_clone`
- Run me! (interactive mode): `./console`
- Run me! (non-interactive mode): `echo "<command>" | ./console.py`

## Key Features
[console.py](console.py) - a simple command-line interpreter
Supported console commands:

- `EOF` - exits
- `quit` - exits
- `<emptyline>` - does nothing and issues a new prompt
- `create` - Creates and saves an instance of `BaseModel` and prints its uuid
- `destroy` - Deletes an instance.
- `show` - Prints the string representation of an instance.
- `all` - Prints all string representations of all instances.
- `update` - Updates an instance by modifying its attribute.

## Directories
#### the `models/` directory contains all classes:
[base_model.py](/models/base_model.py) - The BaseModel class from which future classes will be derived

Classes that inherit from Base Model:
- [amenity.py](/models/amenity.py)
- [city.py](/models/city.py)
- [place.py](/models/place.py)
- [review.py](/models/review.py)
- [state.py](/models/state.py)
- [user.py](/models/user.py)

#### the `engine/` directory manages file storage and JSON conversion:
[file_storage.py](/models/engine/file_storage.py) - serializes and deserealizes between objects and JSON file

#### the `tests/` directory all contains unit tests
[/test_models/test_base_model.py](/tests/test_models/test_base_model.py) - unit test cases

## Usage

To run the console:
```
AirBnB_clone$ ./console.py
(hbnb)
(hbnb) EOF
```

The console handles empty arguments by issuing a new prompt and waiting for input.
*EOF* and *quit* are both commands that exit the console.

The *all* command prints datetime stamped string representations of every instance
```
(hbnb) all
[User] (188bb8a5-1530-4916-ba3e-a202b2c698ae) {&apos;created_at&apos;:
datetime.datetime(2021, 6, 30, 13, 24, 43, 757395), &apos;updated_at&apos;:
datetime.datetime(2021, 6, 30, 13, 24, 43, 757428), &apos;id&apos;: &apos;
188bb8a5-1530-4916-ba3e-a202b2c698ae&apos;}
```

The *create* command starts a new instance of User.
```
(hbnb) create User
d0d71a7c-75cf-44d6-8099-4faca5ebdea7
(hbnb)
```

*** Unknown syntax: exit
The *destroy* command undos the above process. It takes as argument name & id
```
(hbnb) create User
26aeb04f-7804-42aa-9022-96340d33e6f0
(hbnb) show User 26aeb04f-7804-42aa-9022-96340d33e6f0
[User] (26aeb04f-7804-42aa-9022-96340d33e6f0) {&apos;created_at&apos;: datetime.datetime(2021, 6, 30, 13, 42, 57, 34807), &apos;updated_at&apos;: datetime.datetime(2021, 6, 30, 13, 42, 57, 34838), &apos;id&apos;: &apos;26aeb04f-7804-42aa-9022-96340d33e6f0&apos;}
(hbnb) destroy User 26aeb04f-7804-42aa-9022-96340d33e6f0
(hbnb) show User 26aeb04f-7804-42aa-9022-96340d33e6f0
** no instance found **
```

The *update* command allows you to modify data within the instance attributes
```
(hbnb) create User
*** Unknown syntax: exit
041a4c45-355c-4e75-ae44-ecfabbaa8727
(hbnb) update User 041a4c45-355c-4e75-ae44-ecfabbaa8727 name Tim
(hbnb) show User 041a4c45-355c-4e75-ae44-ecfabbaa8727
[User] (041a4c45-355c-4e75-ae44-ecfabbaa8727) {'updated_at': datetime.datetime(2021, 6, 30, 13, 48, 24, 61743), 'id': '041a4c45-355c-4e75-ae44-ecfabbaa8727', 'created_at': datetime.datetime(2021, 6, 30, 13, 47, 13, 957226), 'name': 'Tim'}
```

The *help* or *?* command prints out a list of commands on which helpful information can be summoned.
```
./console.py
Welcome to our HBnB console! Type ? or help for commands
(hbnb) help
```

Documented commands (type help <topic>):
========================================
`EOF`  `all`  `create`  `destroy`  `help`  `quit`  `show`  `update`

```
(hbnb) help create
 Create a new instance of BaseModel, save to JSON file, print id
(hbnb) help all
 Prints all string representation of all instances 
(hbnb) help EOF
 End Of File condition to terminate program 
(hbnb) help destroy
 Delete instanced based on class name and id 
(hbnb) help help
List available commands with "help" or detailed help with "help cmd".
(hbnb) help quit
 Quit command to exit the program 
(hbnb) help show
 Print string representation of instance, given id 
(hbnb) help update
 Updates an instanced based on class name and id 
(hbnb) quit
vagrant@vagrant-ubuntu-trusty-64:~/Projects/AirBnB_clone$
```

## Bugs
None reported.

## Authors
- David Harvey - [Github](https://github.com/dhreyes)
- Gabriel Vazquez - [Github](https://github.com/gavazcal)

## License
Public Domain and open source.
