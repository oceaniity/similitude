import click
from docmentation import conf

@click.command()
@click.argument('--image_file', default='examples/images/test1.jpg',help='Image source file')
@click.option('--training_file', help='Custom training file to use')
@click.option('--layer_count', default=2, help='The number of convolution layers')
def similitude(image_file, training_file, layer_count):
    print('blah')

if __name__ == '__main__':
    similitude()
