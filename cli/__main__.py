import click
from core.services.file import file_severity_to_console


@click.command()
@click.option('--file', required=True, help='This is the path to the file to parse')
@click.option('--severity', default='ERROR', help='This is the severity of the log you want to get')
@click.option('--console', default=True, is_flag=True)
@click.option('--no-duplicates', default=False, is_flag=True)
def cli(file, severity, console, no_duplicates):
    try:
        if console:
            file_severity_to_console(file, severity, no_duplicates)
        else:
            print("Please select the printing option :)")
    except Exception as e:
        raise click.ClickException(e)


if __name__ == '__main__':
    cli()
