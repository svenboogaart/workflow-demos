# your_script.py
import os

# Define your outputs
output_1 = "This is the first output"
output_2 = "This is the second output"
output_3 = "This is the third output"

# Set the outputs to the GITHUB_OUTPUT file
with open(os.getenv('GITHUB_OUTPUT'), 'a') as f:
    f.write(f"output_1={output_1}\n")
    f.write(f"output_2={output_2}\n")
    f.write(f"output_3={output_3}\n")

print("Outputs written to GITHUB_OUTPUT")