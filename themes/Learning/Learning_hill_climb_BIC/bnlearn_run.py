import bnlearn as bn
from pgmpy.readwrite import BIFWriter
import pandas as pd
import os
import sys


current_dir = os.path.dirname(os.path.abspath(__file__))

# Load the BN to compare properly time of learning
true_model = bn.import_DAG(f"{current_dir}/data/alarm.bif", verbose=False)

# Load the data
df = pd.read_csv(f"{current_dir}/data/sample_{sys.argv[1]}_alarm.csv")

# learning the structure
model_learned = bn.structure_learning.fit(
    df, methodtype="hc", scoretype="bic", verbose=False
)

# learning the parameters
model_learned = bn.parameter_learning.fit(
    model_learned, df, methodtype="bayes", verbose=False
)

# Save the model
BIFWriter(model_learned["model"]).write_bif(
    f"{current_dir}/data/bnlearn_learned_{sys.argv[1]}_alarm.bif"
)
