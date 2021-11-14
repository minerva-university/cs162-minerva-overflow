# Minerva Overflow 

A CS162 Final Project.


| ![DOG](https://media2.giphy.com/media/JUji554QwdXwAuYkhP/giphy.gif?cid=ecf05e4762276arv388c0025qtogvfcpm03kwcnqgsdzjjko&rid=giphy.gif) | ![dog](https://media4.giphy.com/media/fbyGEE9mlqDyE/giphy.gif?cid=ecf05e477ed0jwqjysilm8q3bf8f7ll23mzwxxo3or3s3gpg&rid=giphy.gif&ct=g) |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![dog](https://media4.giphy.com/media/jkSvCVEXWlOla/giphy.gif?cid=ecf05e47w0m6d75cmujsj3udpys1jdg6c188v3njwzmmbh24&rid=giphy.gif&ct=g) | ![dog](https://media1.giphy.com/media/tyttpGT2apUm6wtb0kM/giphy.gif?cid=ecf05e47ruacetc9tf6eguzuv2ve5oenqcc6odhh68ry2neu&rid=giphy.gif&ct=g) |

![template ci](https://github.com/minerva-university/cs162-minerva-overflow/actions/workflows/ci.yaml/badge.svg)




## Envrionment Setup

<details>

  <summary>Detials on Virtual Environment </summary>

  Virtual environment is a key component in ensuring that the application is configured in the right environment

  Requirments: Python 3 and pip 3 

    `brew install python3`

  Pip3 is installed with Python3

    `pip3 install virtualenv`

  ##### Usage

  Creation of virtualenv:

  ```
  virtualenv -p python3 venv
  ```

  If the above code does not work, you could also do

  ```
  python3 -m venv venv
  ```

  To activate the virtualenv:

  ```
  source venv/bin/activate
  ```

  Or, if you are **using Windows** - [reference source:](https://stackoverflow.com/questions/8921188/issue-with-virtualenv-cannot-activate)

  ```
  venv\Scripts\activate
  ```

  To deactivate the virtualenv (after you finished working):

  ```
  deactivate
  ```

  Install dependencies in virtual environment:

  ```
  pip3 install -r requirements.txt
  ```

</details>



<details>

  <summary>On Environment Variables </summary>

  All environment variables are stored within the `.env` file and loaded with dotenv package.

  **Never** commit your local settings to the Github repository!

</details>


## Run Backend 

Start the server by running:
```
export FLASK_APP=application.app
flask run
```

## Run Frontend 

```
cd frontend
npm install 
npm run start 
```
## Run Tests
To run the unit tests use the following commands:
```
python3 -m venv venv_unit
source venv_unit/bin/activate
pip install -r requirements-unit.txt
export DATABASE_URL='sqlite:///web.db'
pytest unit_test
```
---
To run Integration Tests, tart by running the web server in a separate terminal.

Now run the integration tests using the following commands:
```
python3 -m venv venv_integration
source venv_integration/bin/activate
pip3 install -r requirements-integration.txt
pytest integration_test
```
## Deployment

We are using Heroku for the backend deployment. (API and Database). @Yueh Han have the access to the dashboard, and could help with confingurating branch deployment. 
