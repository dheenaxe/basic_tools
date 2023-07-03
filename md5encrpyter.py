import click
import hashlib

@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.argument('output_file', type=click.Path())

def encode_md5(input_file, output_file):
    """Simple Program that encrypts the given text file"""
    with open(input_file, 'r') as file:
        with open(output_file, 'w') as output:
            for line in file:
                line = line.strip()  # Remove leading/trailing whitespaces
                md5_hash = hashlib.md5(line.encode()).hexdigest()
                output.write(md5_hash + '\n')

if __name__ == '__main__':
    encode_md5()
