
Grappa is a graph neural network that works as follows:

# Problem Overview

### Inputs:
The input is a set of nodes and edges. For our purposes, the nodes are shower clusters and the edges are "connections" between nodes, representing if nodes belong together. 

### Outputs:
Given this, the task of GrapPA is to determine an **Adjacency Matrix**. Connected nodes indicate that they are part of the same particle shower. Additionally, GrapPA identifies primary shower and track fragments, i.e, the fragments that originated the shower/track.


# GrapPA specifics:

## Graph Construction:

The graph of GrapPA can be determined any number of ways:
1) A complete, fully connected graph
2) Spatial Minimum Spanning Tree
3) 5 Nearest Neighbors

But GrapPA performs best with a complete graph:

![[Pasted image 20250114122246.png]]

## Message Passing:

### Edge Update:

Edges are updated with a 3 layer network, where each layer is preceded by a bath normalization layer, and followed by a LeakyRELU layer with a negative slope of 0.1. The input is a combination of the connected node features and the edge feature. The first linear layer will transform the number of features from $F^s_e + 2F^s_v$ to $F_e^{s+1} = 64$. 

### Node Update:

Authors tested 5 functions to update node feature and generate messages:

1) MetaLayer: A message $m_{ji}$ is computed with a three layer MLP using features from the source node and the connecting edge of the same design as the edge updater mlp. The produced messages are then averaged, then combines with the sink node features. This input is then fed into the same MLP design and produces $F_v^{s+1} = 64$ features.
2) NNConv: $${\vec x}_i^{s+1} = \hat \Theta \vec x_i^s + \sum_{j \in N(i)} x_j^s\cdot h(e_{j,i}^{s+1})$$ where $\hat \Theta$ is a $F_v^{s+1} \times F_v^s$ matrix of weights and $h$ is a MLP that maps $F_e^{s+1}$ to a $F_v^{s+1} \times F_v^s$ matrix. Its the design of the aforementioned MLP where the first layer brings the number of features to $F_v^{s+1} \times F_v^s$.
3) EdgeConv: $$x_i^{s+1}=\sum_{j\in N(i)} h(x_i^s ||x_j^s-x_i^s)$$ Where $||$ is a concatenation operator and $h$ is an MLP that turns $2F_v^s$ features to $F_v^{s+1} = 64$ features, and is identical to the aforementioned design.

The study finds that these three perform roughly the same.

# Theory of GNNs

It may be useful to understand GNNs in general in order to be able to contribute, so this section will include basically notes of what I understand about GNN theory.

## Construction

The input to all GNNs is a graph that is depended on your problem and organization of the data.

## Feature Updates

The important part about GNNs is that over successive timesteps, we update the encoded features of edges and nodes. This is called message passing. It is called this because an the features of the node and edges will be updated according to the features of their neighbors by sharing these features. In a sense, as you perform message passing steps, a node and edge understand more of the graph, as the messages they received from neighbors have been influenced by nodes that are not their neighbors. This happens in 3 steps

#### Updating edge features

For an edge, $e_i^s$ at time $s$, $$e_{ij}^{s+1} = \psi\left(x_i^s, x_{j}^s, e_i^s\right)$$
where $x_i, x_j$ are the features of the nodes that the edge connects.


#### Creating the message
For a node, $x_i^s$ at time s, the message is: $$m_{ij}^{s+1} = \phi\left(x_j^s, e_{ij}^{s+1}\right)$$
where $x_j \in N(V_i)$

#### Updating the Node Features
For a node, $x_i^s$: $$x_i^{s+1} = \chi(x_s^i, \square_{n_j\in N(i)} m_{ij})$$
where $\square {n_j\in N(i)}$ is an aggregation function for the messages to the incoming node, like a sum mean or max.

$\psi, \phi, \chi$ are functions, normally a type of deep neural network. 

## Problem and Loss

Now each aspects of the graph has a set of node features and edge features that have been influenced by their neighbors. We can use these features as an input to a final neural network to solve our chose problem. The architecture of the final network depends on the problem.
