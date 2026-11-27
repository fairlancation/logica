#se debe importar el archivo metro.xlsx
import pandas as pd
import numpy as np
import networkx as nx
df = pd.read_excel('metro.xlsx')
df.head()

METRO = nx.from_pandas_edgelist(df,source='Origen',target='Destino',edge_attr='Longitud de interestación')

djk_path= nx.dijkstra_path(METRO, source='Culhuacán', target='Norte 45', weight='Longitud de interestación')

djk_path

nx.dijkstra_path_length(METRO, 'Ferrería', 'Insurgentes Sur', 'Longitud de interestación')
