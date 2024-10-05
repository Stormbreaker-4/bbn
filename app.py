from pgmpy.models import BayesianNetwork;
from pgmpy.factors.discrete.CPD import TabularCPD;
from pgmpy.inference import VariableElimination;
import matplotlib.pyplot as plt;
import networkx as nx;

alarm = 'Alarm';
burglary = 'Burglary';
earthquake = 'Earthquake';
neighbour_call = 'Neighbour Call';

graph = BayesianNetwork([(burglary, alarm), (earthquake, alarm), (alarm, neighbour_call)]);

b_cpd = TabularCPD(burglary, 2, [[0.005], [0.995]], state_names={burglary: ['True', 'False']});
e_cpd = TabularCPD(earthquake, 2, [[0.002], [0.998]], state_names={earthquake: ['True', 'False']});
a_cpd = TabularCPD(alarm, 2, [[0.99, 0.97, 0.27, 0.001], [0.01, 0.03, 0.73, .999]], evidence=[burglary, earthquake], evidence_card=[2, 2], state_names={alarm: ['True', 'False'], burglary: ['True', 'False'], earthquake: ['True', 'False']});
n_cpd = TabularCPD(neighbour_call, 2, [[0.98, 0.005], [0.02, 0.995]], evidence=[alarm], evidence_card=[2], state_names={neighbour_call: ['True', 'False'], alarm: ['True', 'False']});

graph.add_cpds(b_cpd, e_cpd, a_cpd, n_cpd);

# Check if the model is valid
assert graph.check_model()

# Create inference object
infer = VariableElimination(graph)

# Plotting the Bayesian Network graph
def plot_bayesian_network(graph):
    plt.figure(figsize=(8, 6))
    G = nx.DiGraph(graph.edges())
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold')
    plt.title('Bayesian Network Structure', size=15)
    plt.show()

# Function to visualize results for decision making
def plot_inference_result(inference_result, title="Inference Result"):
    probs = inference_result.values;
    labels = inference_result.state_names[inference_result.variables[0]];
    colour_mapping = {
        'True': 'lightgreen',
        'False': 'salmon'
    }
    colours = [colour_mapping.get(label) for label in labels]
    plt.figure(figsize=(6, 4))
    plt.bar(labels, probs, color=colours, alpha=1)
    plt.ylabel('Probability')
    plt.title(title)
    plt.show()

# Visualize Bayesian Network Structure
plot_bayesian_network(graph)

# Query 1: Probability that the alarm is ringing given burglary but no earthquake
prob_alarm = infer.query(variables=[alarm], evidence={burglary: 'True', earthquake: 'False'})
print("P(Alarm | Burglary, ¬Earthquake):")
print(prob_alarm)
plot_inference_result(prob_alarm, title="P(Alarm | Burglary, ¬Earthquake)")

# Query 2: Probability that a burglary has occured given a call from the neighbour due to the alarm and an earthquake
prob_burglar = infer.query(variables=[burglary], evidence={alarm: 'True', neighbour_call: 'True', earthquake: 'True'})
print("P(Burglary | Alarm, Neighbour Call, Earthquake):")
print(prob_burglar)
plot_inference_result(prob_burglar, title="P(Burglary | Alarm, Neighbour Call, Earthquake)")

# Query 3: Probability that the a burglary has occured given a call from the neighbour and an earthquake took place
prob_burglar = infer.query(variables=[burglary], evidence={neighbour_call: 'True', earthquake: 'True'})
print("P(Burglary | Neighbour Call, Earthquake):")
print(prob_burglar)
plot_inference_result(prob_burglar, title="P(Burglary | Neighbour Call, Earthquake)")
