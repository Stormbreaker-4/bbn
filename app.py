from pgmpy.models import BayesianNetwork;
from pgmpy.factors.discrete.CPD import TabularCPD;

graph = BayesianNetwork([('Burglary', 'Alarm'), ('Earthquake', 'Alarm'), ('Alarm', 'Neighbour Call')]);
print(graph.nodes());

b_cpd = TabularCPD('Burglary', 2, [[0.005], [0.995]], state_names={'Burglary': ['True', 'False']});
e_cpd = TabularCPD('Earthquake', 2, [[0.002], [0.998]], state_names={'Earthquake': ['True', 'False']});
a_cpd = TabularCPD('Alarm', 2, [[0.99, 0.97, 0.8, 0.001], [0.01, 0.03, 0.2, .999]], evidence=['Burglary', 'Earthquake'], evidence_card=[2, 2], state_names={'Alarm': ['True', 'False'], 'Burglary': ['True', 'False'], 'Earthquake': ['True', 'False']});
n_cpd = TabularCPD('Neighbour Call', 2, [[0.98, 0.005], [0.02, 0.995]], evidence=['Alarm'], evidence_card=[2], state_names={'Neighbour Call': ['True', 'False'], 'Alarm': ['True', 'False']});

graph.add_cpds(b_cpd, e_cpd, a_cpd, n_cpd);
