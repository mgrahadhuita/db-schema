#!/usr/bin/env python
import argparse
import os

########################################################################################################################
# Main Script Start Here
########################################################################################################################
# Instantiate the parser
parser = argparse.ArgumentParser(description='SchemaSpy Helper')
# Required positional argument
parser.add_argument('--user', required=True, type=str, help='Postgres user is required argument. E.g: root')
parser.add_argument('--pwd', required=True, type=str, help='Postgres password is required argument. E.g: password')
parser.add_argument('--db', required=True, type=str, help='Postgres database is required argument. E.g: kycdb')
parser.add_argument('--schemas', required=True, type=str,
                    help='Postgres database is required argument. E.g: <schema_1>,<schema_2>')
parser.add_argument('--host', required=True, type=str,
                    help='Postgres database url is required argument. E.g: localhost or '
                         '<staging aws link>')
parser.add_argument('--team', required=True, type=str,
                    help='Team is required argument. E.g: kyc or payout or cfp')

# Optional positional argument
parser.add_argument('--port', required=True, type=int,
                    help='Postgres database port is optional argument. Default value 5432')

args = parser.parse_args()
print("Passed-in arguments:", args.__str__())

# Default file and batch configs
port = 5432

user = args.user
pwd = args.pwd
database = args.db
host = args.host
schemas = args.schemas.split(sep=",")
team = args.team

if args.port is not None:
    port = args.port

for schema in schemas:
    schema_spy_command = "java -jar schemaspy-6.1.0.jar -t pgsql -dp postgresql-42.2.23.jar -db " + database + " -host " + host + " -port " + port.__str__() + " -s " + schema + " -u " + user + " -p " + pwd + " -o " + team + "/" + database + "/" + schema
    print(schema_spy_command)
    os.system(schema_spy_command)
