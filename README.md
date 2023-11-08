# poec-tp-docker

### Doc version : v1 - 08/11/2023

## Project description
Create script on Python with a function, which calculates VAT; make and run unit tests to check the function, use Docker to build and to check the tests

## Technical info / folder architecture
- src: 
  - main.py
  - tests.py
  - calc.py
- Dockerfile

## Prerequisites
- Docker
- Python 3.12

## How to dev
- Clone this repository to your local machine: https://github.com/anmy2121/poec-tp-docker.git
- Create docker by using the command docker build -t tp-docker .

## How to use
Check if the unit tests pass by launching the command: docker run -it tp-docker python src/tests.py 

## How to test
Make different tests to check the functionality: docker run -it tp-docker python src/main.py 100 20 by changing and adding different numbers (negative, positive, float) or symbols or words between ""


   




