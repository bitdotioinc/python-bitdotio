#!/usr/bin/env python3
import click
import sys
import json



# Allows overriding the required `-k` when subcommands have `--help`
# From https://stackoverflow.com/questions/55818737/python-click-application-required-parameters-have-precedence-over-sub-command-he
class IgnoreRequiredWithHelp(click.Group):
    def parse_args(self, ctx, args):
        try:
            return super(IgnoreRequiredWithHelp, self).parse_args(ctx, args)
        except click.MissingParameter as exc:
            if '--help' not in args:
                raise
            # remove the required params so that help can display
            for param in self.params:
                if param.name == "key":
                    param.required = False
                    break
            return super(IgnoreRequiredWithHelp, self).parse_args(ctx, args)


@click.group(cls=IgnoreRequiredWithHelp)
@click.option("-k", "--key", required=True, help="Your bit.io API key, available when you click the connect button in bit.io")
@click.option("-v", "--verbose", default=False, is_flag=True, show_default=True, help="Verbose output")
@click.pass_context
def bitio(ctx, key, verbose):
    raise NotImplementedError


#  python3 bit.py -k your_api_key_here query -q "SELECT *  FROM \"a/demo_repo\".\"atl_home_sales\""
# echo  "SELECT *  FROM \"a/demo_repo\".\"atl_home_sales\"" | python3 bit.py -k your_api_key_here query -qf -
@bitio.command()
@click.option("-q", "--query", required=False, help="The SQL to run.")
@click.option("-qf", "--query_file", required=False, help="A SQL file run, containing a single query. Use - for stdin.", type=click.File('r'))
@click.pass_obj
def query(b, query, query_file):
    raise NotImplementedError


@bitio.group()
@click.pass_obj
def repo(b):
    pass


# python3 bit.py -k your_api_key_here repo create -n foobarsadsasds -d "foo bar baz" -p False
@repo.command()
@click.option("-r", "--repo_name", required=True, help="The repo name.")
@click.option("-d", "--description", default="", help="The repo description.")
@click.option("-p", "--is_private", show_default=True, default=True, help="Is this repo private or not.")
@click.pass_obj
def create(b, repo_name, description, is_private):
    raise NotImplementedError

@repo.command()
@click.pass_obj
def list(b):
    raise NotImplementedError

# bit.py -k your_api_key_here repo retrieve -n demo_repo
@repo.command()
@click.option("-r", "--repo_name", required=True, help="The repo name.")
@click.pass_obj
def retrieve(b, repo_name):
    raise NotImplementedError

# bit.py -k your_api_key_here repo destroy -n demo_repo
@repo.command()
@click.option("-n", "--name", required=True, help="The repo name.")
@click.option("-y", "--yes", default=False, is_flag=True, show_default=True, help="Skip the confirmation")
@click.pass_obj
def destroy(b, name, yes):
    raise NotImplementedError


@bitio.group(name="import")
@click.pass_obj
def import_stub(b):
    raise NotImplementedError

@import_stub.command()
@click.option("-i", "--job_id", required=True, help="The importer job id.")
@click.pass_obj
def status(b, job_id):
    raise NotImplementedError

@import_stub.command()
@click.option("-r", "--repo_name", required=True, help="The repo name.")
@click.option("-t", "--table_name", required=True, help="The table name.")
@click.option("--data", required=True, hidden=True, type=click.File('r'), default="-", help="The json data")
@click.pass_obj
def json_data(b, repo_name, table_name, data):
    raise NotImplementedError

@import_stub.command()
@click.option("-r", "--repo_name", required=True, help="The repo name.")
@click.option("-t", "--table_name", required=False, help="The table name.")
@click.option("-u", "--url", required=True, help="The url to import.")
@click.pass_obj
def url(b, repo_name, table_name, url):
    raise NotImplementedError

@import_stub.command()
@click.option("-r", "--repo_name", required=True, help="The repo name.")
@click.option("-t", "--table_name", required=False, help="The table name.")
@click.option("-f", "--file_name", required=True,  type=click.File('r'), default="-", help="The file to import; defaults to stdin.")
@click.pass_obj
def file(b, repo_name, table_name, file_name):
    raise NotImplementedError

def print_json_model(model):
    print(json.dumps(model.to_dict(), indent = 4))

def print_json_model_list(models):
    print(json.dumps([x.to_dict() for x in models], indent = 4))

def main():
    try:
        bitio(auto_envvar_prefix="BITIO")
    except click.UsageError as e:
        raise e
    except Exception as e:
        print(e)
        sys.exit(3)

if __name__ == '__main__':
    main()
