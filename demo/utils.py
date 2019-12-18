import json
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt, mpld3
import pandas as pd


def classify_data_by_headers(headers, data):
    plt.figure(figsize=(15, 6))
    headers_json = json.loads(headers)
    data_json = json.loads(data)

    output_json = {}
    hid = headers_json.get('id')

    for elem in data_json:
        for key, value in elem.items():
            if headers_json.get(key) or key == hid:
                if output_json.get(key) is None:
                    output_json.update({key: [value]})
                else:
                    output_json.get(key).append(value)

    output_df = pd.read_json(json.dumps(output_json))

    if hid is not None:
        varieties = list(output_df.pop(hid))

    mergings = linkage(output_df.to_numpy(), method='complete')
    if hid is not None:
        dendrogram(mergings, labels=varieties)
    else:
        dendrogram(mergings)

    return mpld3.fig_to_html(plt.gcf())
