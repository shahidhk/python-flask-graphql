# GraphQL server using python-flask

A boilerplate Python GraphQL Server using Flask and Graphene
using Flask.

## Run the server

### Clone the repo

```bash
git clone https://github.com/shahidhk/python-flask-graphql
```

Run the webhook using any of the tree methods below:

### Run locally

```bash
# cython is a dependency
# sudo apt-get install cython
pip install -r requirements.txt

export FLASK_APP=server.py
flask run
```

GraphQL endpoint is `http://localhost:5000/graphql`

### Using Docker

```bash
docker build -t python-flask-graphql .
docker run -p 5000:5000 python-flask-graphql
```
