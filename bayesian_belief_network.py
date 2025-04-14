from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Define the structure of the Bayesian Network
model = BayesianModel([('Income', 'BuysCar'), ('Age', 'BuysCar')])

# Define the CPDs (Conditional Probability Distributions)
cpd_income = TabularCPD(variable='Income', variable_card=2, values=[[0.6], [0.4]])  # 0: Low, 1: High
cpd_age = TabularCPD(variable='Age', variable_card=2, values=[[0.5], [0.5]])        # 0: Young, 1: Old

# P(BuysCar | Income, Age)
cpd_buyscar = TabularCPD(
    variable='BuysCar', variable_card=2,
    values=[
        [0.9, 0.7, 0.6, 0.2],  # P(BuysCar=0)
        [0.1, 0.3, 0.4, 0.8]   # P(BuysCar=1)
    ],
    evidence=['Income', 'Age'],
    evidence_card=[2, 2]
)

# Add CPDs to the model
model.add_cpds(cpd_income, cpd_age, cpd_buyscar)

# Verify the model
assert model.check_model()

# Inference
inference = VariableElimination(model)

# Predict probability of BuysCar given Income=1 (High), Age=0 (Young)
query_result = inference.query(variables=['BuysCar'], evidence={'Income': 1, 'Age': 0})
print(query_result)