import pandas as pd

expression = pd.read_csv('data/expression.tsv', sep='\t')

tumor_columns = ["tumor_1", "tumor_2"]
normal_columns = ["normal_1", "normal_2"]

expression["tumor_mean"] = expression[tumor_columns].mean(axis=1)
expression["normal_mean"] = expression[normal_columns].mean(axis=1)
expression["fold_change"] = expression["tumor_mean"] / expression["normal_mean"]
filtered_expression = expression[expression["fold_change"] > 2]
sorted_expression = filtered_expression.sort_values(by="fold_change", ascending=False)
sorted_expression.to_csv('results/upregulated_genes.tsv', sep='\t', index=False)