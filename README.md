# biological_community_detection

#### The aim of this project is to evvaluate community detection algorithms on synthetic and cortical networks.

#### The algorithms will be evaluated with:
1. The normalised mutual information: 
2. The modularity:

##### These scores are with respect to the ground truth communities. 

## Baseline reasults

#### Below show the variatoon if Normalised mutual information and Modularity for the synthetic LFR graph with varying number of nodes andmixing perameter between 0-1.

| Normalised mutual information      | Modularity     |
| -------------- | -------------- |
| ![image info](figures/n250NMI.png)   | ![image info](figures/n250Q.png)   |
| ![image info](figures/n500NMI.png)| ![image info](figures/n500Q.png) |
| ![image info](figures/n1000NMI.png)| ![image info](figures/n1000Q.png) |

## Reasults of community detection cortical netowrks.
#### Below is an evaluation of the detected communities overlap with the node metadata treated as communities. 

| Cell role     | Neurotransmitter     |
| -------------- | -------------- |
| ![image info](figures/cortex_community_roles_overlap.png)   | ![image info](figures/cortex_community_neurotransmitters_overlap.png)   |