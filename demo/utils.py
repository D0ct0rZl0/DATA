import json
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
import pandas as pd


def classify_data_by_headers(headers, data):
    headers_json = json.loads(headers)
    data_json = json.loads(data)

    output_json = {}
    id = headers_json['id']

    for elem in data_json:
        for key, value in elem.items():
            if headers_json.get(key) or key == id:
                if output_json.get(key) is None:
                    output_json.update({key: [value]})
                else:
                    output_json.get(key).append(value)

    output_df = pd.read_json(json.dumps(output_json))

    varieties = list(output_df.pop(id))
    samples = output_df.values

    print(samples)
    print(varieties)

    mergings = linkage(samples, method='complete')
    if id is not None:
        dendrogram(mergings, labels=varieties)
    else:
        dendrogram(mergings)

    plt.show()
