#!/usr/bin/env python3
import bitdotio
import click
import sys
import json
from urllib.parse import urlparse
import posixpath



# Allows overriding the required `-k` when subcommands have `--help`
# From https://stackoverflow.com/questions/55818737/python-click-application-required-parameters-have-precedence-over-sub-command-he
class IgnoreRequiredWithHelp(click.Group):
    def parse_args(self, ctx, args):
        try:
            return super(IgnoreRequiredWithHelp, self).parse_args(ctx, args)
        except click.MissingParameter as exc:
            if '--help' not in args:

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
    if key:
        b = bitdotio.bitdotio(key)
        b.api_client.user_agent = b.api_client.user_agent + "/CLI"
        if verbose:
            b.api_client.configuration.debug = True
        ctx.obj = b


#  python3 bit.py -k your_api_key_here query -q "SELECT *  FROM \"a/demo_repo\".\"atl_home_sales\""
# echo  "SELECT *  FROM \"a/demo_repo\".\"atl_home_sales\"" | python3 bit.py -k your_api_key_here query -qf -
@bitio.command()
@click.option("-q", "--query", required=False, help="The SQL to run.")
@click.option("-qf", "--query_file", required=False, help="A SQL file run, containing a single query. Use - for stdin.", type=click.File('r'))
@click.pass_obj
def query(b, query, query_file):
    if query:
        query_string = query
    elif query_file:
        with query_file:
            query_string = query_file.read()
    else:
        raise click.UsageError("One of --query or --query_file is required.")

    query_obj = bitdotio.model.query.Query(query_string=query_string)
    print_json_model(b.create_query(query=query_obj))


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
    r = bitdotio.model.repo.Repo(name=repo_name)
    r.description = description
    r.is_private = is_private
    print_json_model(b.create_repo(repo=r))

@repo.command()
@click.pass_obj
def list(b):
    print_json_model_list(b.list_repos())

# bit.py -k your_api_key_here repo retrieve -n demo_repo
@repo.command()
@click.option("-r", "--repo_name", required=True, help="The repo name.")
@click.pass_obj
def retrieve(b, repo_name):
    print_json_model(b.retrieve_repo(repo_name))

# bit.py -k your_api_key_here repo destroy -n demo_repo
@repo.command()
@click.option("-n", "--name", required=True, help="The repo name.")
@click.option("-y", "--yes", default=False, is_flag=True, show_default=True, help="Skip the confirmation")
@click.pass_obj
def destroy(b, name, yes):
    if yes:
        print_json_model(b.destroy_repo(name))
    elif click.confirm(f"Are you sure you want destroy the repo {name}?"):
        print_json_model(b.destroy_repo(name))


@bitio.group(name="import")
@click.pass_obj
def import_stub(b):
    pass

@import_stub.command()
@click.option("-i", "--job_id", required=True, help="The importer job id.")
@click.pass_obj
def status(b, job_id):
    print_json_model(b.retrieve_ingestor_job(q_uuid=job_id))

@import_stub.command()
@click.option("-r", "--repo_name", required=True, help="The repo name.")
@click.option("-t", "--table_name", required=True, help="The table name.")
@click.option("--data", required=True, hidden=True, type=click.File('r'), default="-", help="The json data")
@click.pass_obj
def json_data(b, repo_name, table_name, data):
    with data:
        json_str = data.read()
        # this is a way to do local json validation
        json_obj = json.loads(json_str)
        import_json = bitdotio.model.import_json.ImportJson(json_str, table_name, repo_name)
        ingestor_job_details = b.create_import_json(import_json=import_json)
        print_json_model(ingestor_job_details)

@import_stub.command()
@click.option("-r", "--repo_name", required=True, help="The repo name.")
@click.option("-t", "--table_name", required=False, help="The table name.")
@click.option("-u", "--url", required=True, help="The url to import.")
@click.pass_obj
def url(b, repo_name, table_name, url):
    if table_name:
        import_url = bitdotio.model.import_url.ImportUrl(url, table_name, repo_name)
    else:
        path = urlparse(url).path
        filename = posixpath.basename(path)
        import_url = bitdotio.model.import_url.ImportUrl(url, filename, repo_name)

    ingestor_job_details = b.create_import_url(import_url=import_url)
    print_json_model(ingestor_job_details)

@import_stub.command()
@click.option("-r", "--repo_name", required=True, help="The repo name.")
@click.option("-t", "--table_name", required=False, help="The table name.")
@click.option("-f", "--file_name", required=True,  type=click.File('r'), default="-", help="The file to import; defaults to stdin.")
@click.pass_obj
def file(b, repo_name, table_name, file_name):

    if file_name.name == "<stdin>":
        if not table_name:
            raise click.UsageError("--table_name is required when reading a file from stdin.")

    if table_name:
        ingestor_job_details = b.create_import_file(file_name, repo_name, table_name=table_name)
    else:
        ingestor_job_details = b.create_import_file(file_name, repo_name)
    print_json_model(ingestor_job_details)

def print_json_model(model):
    print(json.dumps(model.to_dict(), indent = 4))

def print_json_model_list(models):
    print(json.dumps([x.to_dict() for x in models], indent = 4))

def main():
    try:
        bitio(auto_envvar_prefix="BITIO")
    except click.UsageError as e:
        raise e
        sys.exit(1)
    except bitdotio.exceptions.NotFoundException:
        print("Repo not found.")
        sys.exit(2)
    except Exception as e:
        print(e)
        sys.exit(3)

if __name__ == '__main__':
    main()
