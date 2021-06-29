[Image](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210629%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210629T003549Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=999c6bc2e8f5a5ba2e4ead9037528ff1a32108098605e3eb9f1bf823eb6c1b78)

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
placeholder for usage examples

## Bugs
None reported.

## Authors
- David Harvey - [Github](https://github.com/dhreyes)
- Gabriel Vazquez - [Github](https://github.com/gavazcal)

## License
Public Domain and open source. 
