from flask import Flask
from flask_graphql import GraphQLView
import graphene

app = Flask(__name__)

class Query(graphene.ObjectType):
    is_authenticated = graphene.Boolean(description='Indicates whether the user is logged in or not')

    def resolve_is_authenticated(self, info):
        print(info)
        return False

class Mutation(graphene.ObjectType):
    dummy_mutation = graphene.String()

    def resolve_dummy_mutation(self, info):
        return "this is a dummy mutation"

schema = graphene.Schema(query=Query, mutation=Mutation)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
