import os
import onnx
import onnx_analyzer
import pandas as pd
import matplotlib.pyplot as plt

def analyze_single(model_path: str, calculate_macs=False) -> list:
    model = onnx.load(model_path)
    params = onnx_analyzer.count_param(model)
    ops, macs = onnx_analyzer.count_op(model)
    return[(model_path, params, ops, macs)]

def analyze(path: str, calculate_macs=False) -> list:
    results = []
    for files in os.listdir(path):
        if files.endswith('.onnx'):
            results += analyze_single(os.path.join(path, files), calculate_macs)
        else:
            continue
    return results

def report(results: list, out: str, visualize=False):
    if visualize:
        fig, axs = plt.subplots(len(results))
        fig.set_size_inches(8,6*len(results))
    for i, (model_path, params, ops, macs) in enumerate(results):
        print("Results for model: {}".format(model_path))
        print("params: {}".format(params))
        print("op statistics:")
        ops_df = pd.DataFrame({'op_type': ops.keys(), 'count': ops.values()})
        ops_df['percent'] = (ops_df['count'] / 
                    ops_df['count'].sum()) * 100
        print(ops_df)
        if visualize:
            ops_df.plot.bar(x='op_type', y='count', ax=axs[i])
            axs[i].set_title(model_path)

    if visualize:
        plt.subplots_adjust(left=0.1,
                            bottom=0.1, 
                            right=0.9, 
                            top=0.9, 
                            wspace=0.4, 
                            hspace=0.6)
        print("Saving visualizations to: {}".format(out))
        plt.savefig(out)
        
        