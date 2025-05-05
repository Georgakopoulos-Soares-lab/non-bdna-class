import sys
from pathlib import Path
from SigProfilerAssignment import Analyzer as Analyze

samples = sys.argv[1]
output = "sig_ID"
Path(output).mkdir(exist_ok=True)

if not Path(samples).is_dir():
    raise ValueError(f"Non-existant directory '{samples}'.")

print(f"INPUT <<---- {samples}.")
print(f"out-sourcing resultings ---->> {output}.")

Analyze.cosmic_fit(
                   samples, 
                   output,
				   input_type="vcf",
				   context_type="ID",
				   collapse_to_SBS96=False,
				   cosmic_version=3.4,
				   exome=False,
				   genome_build="GRCh37",
				   signature_database=None,
				   exclude_signature_subgroups=None,
				   export_probabilities=True,
				   export_probabilities_per_mutation=True,
				   make_plots=True,
				   sample_reconstruction_plots=False,
				   verbose=True
                   )
