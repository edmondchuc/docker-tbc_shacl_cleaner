import click
from rdflib import Graph, Namespace
from rdflib.namespace import RDF


@click.command()
@click.argument('shacl_file', type=click.Path(exists=True))
def run(shacl_file):
    g = Graph().parse(shacl_file, format='turtle')

    SH = Namespace('http://www.w3.org/ns/shacl#')

    for node_shape, _, _ in g.triples((None, RDF.type, SH.NodeShape)):
        g.add((node_shape, SH.targetClass, node_shape))

    g.serialize(shacl_file, format='turtle')


if __name__ == '__main__':
    run()