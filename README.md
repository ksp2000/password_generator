# Password Generator
A secure password generator RestAPI made with flask

## Setup
- Download the repository.
- Extract .zip file.
- Open command prompt in the repository location.
- Create a python virtual environment
  ```
	$ python -m venv env
	```
- Install requirements
  ```
  $ pip install -r requirements.txt
  ```
- Run the development server on your local machine
  ```
  $ python api.py
  ```
- Now the password generator is up and running at `https://localhost:5000/`. Ready to answer your requests.

## How to use?

- Send `GET` request to `http://localhost:5000/v1/password/<password_length>` to get password of length equal to `password_length` parameter passed in the url.
- Response is in json format.
