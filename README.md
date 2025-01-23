# A Simple Todo Application built using VueJS

- This application is built using VueJS
- The backend is built using FastAPI
- The database is a SQLite database in a file called tasks.db
- There is a proxy for **/api/** */ from the frontend to backend

## Running the application

### Running the frontend
- Run `npm install`
- To start the dev server, run `npm run serve`
- Open `http://localhost:8080/` in a browser

### Running the backend
- Go to the server folder `cd server`
- To create a virtual environment, run `python3 -m venv venv`
- Activate virtual environment, `source venv/bin/activate`
- Run `pip3 install requirements.txt`
- To start the uvicorn server, run `uvicorn server:app --reload`
- Open `http://localhost:8000/docs` in a browser to access the swagger documentation
- This will create a tasks.db file with seed data and start the backend server

## Technologies used
- VueJS
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn