# Bambank

Welcome to Bambank
The one place to transact Bambeuros between your account and other users.
Sign up today to recieve a promotional 100 (B) Bambeuros.

# Installation

## Backend (app)

The Backend assumes you have python3 installed and a working postgresql database.

There is a Pipfile provided for installing any python3 dependencies.

You may install them using `pipenv`

```
$ cd app
$ pipenv install
```

In order to link to your postgresql database you will need to add a `.env` file in `/app` with the following variables:

```
DATABASE_URL = <db_url>
DATABASE_NAME = <db_name>
DATABASE_USER = <user>
DATABASE_PWORD = <password>
```

relevant to your postgresql installation.

### Run the Backend

To intialise the dependencies run the following:

```
$ cd app
$ pipenv shell
```

To run the backend application you can use the following:
```
uvicorn main:app --reload
```

You may then find the endpoints documented here: `http://localhost:8000/docs`

### Notes and Assumptions

I chose to use FastAPI for this project as I have been meaning to test it out as a quick to implementation, more lightweight API backend in comparison to Django and Django Rest Framework.

The framework was simple to get up and running and quick to an implementation. 

FastAPI is then combined with SQLAlchemy in order to connect to a Postgresql Database, which as we discussed both myself and the development teams at Silvercat are familiar with. This wasn't necessary for the full implementation but I thought it would be useful to show the capability of the ORM.

The Docs linked above should be comprehensive in describing the utility of the API and should (technically) meet the specification.

As one will notice one large assumption here is that as it is a prototype, security did not matter in implementation, but does when thinking about further versions (when you have longer than two hours to implement).

I was looking to overhaul the user login procedure with a JWT Authentication procedure and would likely be my next steps.

Another major assumption made was that Bambeuros are whole integers and can only be such. If we wished to change this to a float (either 2.d.p or unlimited) it would be easy to update in the backend. For now though, only whole Bambeuros can be transacted.

Finally much of the data is validated incorrectly, in my tests I have assumed a user would sign up with an email yet all the schema will check for is string.

## React Frontend (frontend) (WIP)

The installation and use of the Frontend React App assumes you have a working [`Node.js`](https://nodejs.org/en/download/package-manager/) installation on your machine.

To start the frontend React Application:
```
$ cd frontend
$ npm install
$ npm start
```

When the server is up and running you can then head to `http://localhost:3000/`.

There you will be greeted by the login page, and there is a link to create an account.

### Notes and Assumptions

Currently this really is where I ran out of time. There is a working form for both login and create account however at current this is not hooked up to the backend.

Both are ready to be implemented with the necessary hooks connecting to the API documented above.

There is also the `/balance` page to be implemented along with `/transactions` to see and perform transactions.

The assumption here again is that we do not mind how it looks, it is a prototype afterall.

We also again have put security to a side for now, the forms are currently passing the form data across in string. As mentioned in the previous segment, the next stage was to add somekind of JWT authentication, something that really shouldn't be too hard to implement.



