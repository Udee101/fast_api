### REST API built with python FastAPI

#### Run locally

- Create a parent directory that houses the cloned project by inputting the following command in the terminal:
  ```
  mkdir fast-api
  ```

- Clone the repository
  ```
  git clone https://github.com/Udee101/fast_api.git
  ```

- In the parent directory `/fast-api`, create a virtual environment by iputting the folowing command in the terminal:
  ```
  python3 -m venv .venv
  ```

- Run/activate the virtual environment byt inputting the following command in the terminal:
  ```
  source .venv/bin/activate
  ```

- Once the virtual enviroment is activated, install all the dependencies listed in `fast-api/requirements.txt`
  ```
  pip install -r requirements.txt
  ```

- In the project's directory `fast-api/sql_app`, create a `.env` file, which will contain the environment variable for the database connection
  ```
  touch .env
  ```

- After setting up the environment variables, change the working directory to the parent directory
  ```
  cd ../
  ```

- Run the app
  ```
  uvicorn sql_app.main:app --reload
  ```

The app will lauch on port 8000
