from pgmpy.models import BayesianNetwork;
from pgmpy.factors.discrete.CPD import TabularCPD;

graph = BayesianNetwork([('Burglary', 'Alarm'), ('Earthquake', 'Alarm'), ('Alarm', 'Neighbour Call')]);
print(graph.nodes());

daft_graph = graph.to_daft();
print(daft_graph);
daft_graph.savefig('graph.png');
