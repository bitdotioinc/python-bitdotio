#!/usr/bin/env python3
import os
import click
import sys
import json

from bitdotio import __version__, bitdotio


USER_AGENT = f"python-bitdotio-cli/{__version__}"


def printj(obj):
    print(json.dumps(obj))


# Allows overriding the required `-k` when subcommands have `--help`
# From https://stackoverflow.com/questions/55818737/python-click-application-required-parameters-have-precedence-over-sub-command-he
class IgnoreRequiredWithHelp(click.Group):
    def parse_args(self, ctx, args):
        try:
            return super().parse_args(ctx, args)
        except click.MissingParameter:
            if "--help" not in args:
                raise

            # HACK: if just doing --help, pass in a phony key that passes regex
            # validation.
            return super().parse_args(ctx, ["-k", "v2_help", "--help"])


@click.version_option(__version__, '-v', '--version', is_flag=True, help="Print bit version and exit")
@click.group(cls=IgnoreRequiredWithHelp)
@click.option(
    "-k",
    "--key",
    required=False,
    help="Your bit.io API key, available when you click the connect button in bit.io",
)
@click.pass_context
def bitio(ctx, key):
    if key is None:
        key = os.environ.get("BITIO_KEY")
        if key is None:
            raise click.MissingParameter(
                "Your bit.io key must be set either using the -k/--key argument or as the environment variable BITIO_KEY"
            )

    b = bitdotio(key)
    b._api_client.set_header("User-Agent", USER_AGENT)
    ctx.obj = b


# bit -k <api-key> query -d <db-name> -q "SELECT 1"
@bitio.command()
@click.option("-d", "--database", required=True, help="Name of the database to query")
@click.option("-q", "--query", required=False, help="The SQL to run.")
@click.option(
    "-qf",
    "--query_file",
    required=False,
    help="A SQL file to run, containing a single query. Use - for stdin.",
    type=click.File("r"),
)
@click.option(
    "-o",
    "--objects",
    is_flag=True,
    help="Return data as an array of JSON objects instead of row arrays",
)
@click.pass_obj
def query(b, database, query, query_file, objects):
    if query:
        query_string = query
    elif query_file:
        with query_file:
            query_string = query_file.read()
    else:
        raise click.UsageError("One of --query or --query_file is required")

    if objects:
        printj(b.query(database, query_string, data_format="objects"))
    else:
        printj(b.query(database, query_string))


@bitio.group()
@click.pass_obj
def db(b):
    pass


@db.command()
@click.pass_obj
def list(b):
    printj(b.list_databases())


@db.command()
@click.option("-n", "--name", required=True, help="The database name")
@click.option(
    "-p",
    "--is_private",
    show_default=True,
    default=True,
    help="Whether or not the database is set to private",
)
@click.pass_obj
def create(b, name, is_private):
    printj(b.create_database(name, is_private=is_private))


@db.command()
@click.option("-d", "--database", required=True, help="Name of the database to show")
@click.pass_obj
def info(b, database):
    printj(b.get_database(database))


@db.command()
@click.option("-d", "--database", required=True, help="Name of the database to show")
@click.option(
    "-n", "--name", required=False, default=None, help="New name for the database"
)
@click.option(
    "-p",
    "--is_private",
    required=False,
    default=None,
    help="Whether or not the database is set to private",
)
@click.pass_obj
def update(b, database, name, is_private):
    printj(b.update_database(database, name=name, is_private=is_private))


@db.command()
@click.option("-d", "--database", required=True, help="Name of the database to show")
@click.pass_obj
def delete(b, database):
    b.delete_database(database)
    print(f"Successfully deleted database: {database}")


def main():
    try:
        bitio(auto_envvar_prefix="BITIO")
    except click.UsageError as e:
        raise e
    except Exception as e:
        print(e)
        sys.exit(3)


if __name__ == "__main__":
    main()
