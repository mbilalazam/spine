# Parameters to Change for 2x2 Aggregation (Clustering) Task

For your task involving the 2x2 detector and optimizing the distance cut on edges during the aggregation (clustering) step of the reconstruction chain, you should focus on the following key parameters.

## 1. Graph Construction Parameters

These parameters control how edges are formed between nodes (track and shower fragments), essential for the aggregation step.

- **`graph.max_length`**
  - Controls the maximum distance between nodes (fragments) allowed for edge creation.
  - **Changeable**: Yes
  - **Existing value**: `[500, 0, 500, 500, 0, 0, 0, 25, 0, 25]`
  - **Example options**: Adjust based on physical detector geometry and desired distance cut.

- **`graph.dist_algorithm`**
  - Algorithm used for calculating distances between nodes. You can experiment with different algorithms to optimize aggregation.
  - **Changeable**: Yes
  - **Existing value**: `recursive`
  - **Example options**: `euclidean`, `manhattan`, etc.

## 2. Node and Edge Encoding Parameters

These control how nodes and edges are encoded, influencing how the model aggregates fragments.

### Node Encoder
- **`node_encoder.add_points`**
  - Determines whether to include point (coordinate) information in node encoding.
  - **Changeable**: Yes
  - **Existing value**: `true`
  - **Options**: `true` or `false`.

- **`node_encoder.add_local_dirs`**
  - Includes direction vectors in the node encoding to improve clustering based on direction alignment.
  - **Changeable**: Yes
  - **Existing value**: `true`
  - **Options**: `true` or `false`.

- **`node_encoder.dir_max_dist`**
  - Sets the maximum distance for direction vectors used in aggregation.
  - **Changeable**: Yes
  - **Existing value**: `5`
  - **Example options**: Adjust based on the detector's physical scale.

- **`node_encoder.add_local_dedxs`**
  - Adds local energy deposition values (dE/dx) to improve clustering, especially for distinguishing particle types.
  - **Changeable**: Yes
  - **Existing value**: `true`
  - **Options**: `true` or `false`.

- **`node_encoder.dedx_max_dist`**
  - Sets the maximum distance for dE/dx values in node aggregation.
  - **Changeable**: Yes
  - **Existing value**: `5`
  - **Example options**: Adjust based on energy deposition characteristics.

### Edge Encoder
- **`edge_encoder.use_numpy`**
  - Option to use NumPy for edge encoding. Can be toggled based on performance needs.
  - **Changeable**: Yes
  - **Existing value**: `true`
  - **Options**: `true` or `false`.

## 3. Clustering/Node Grouping Parameters

These parameters define how fragments (nodes) are grouped together.

- **`nodes.shapes`**
  - Defines the types of objects (shapes) being clustered. You might want to focus on `shower` and `track`.
  - **Changeable**: Yes
  - **Existing value**: `[shower, michel, delta]`
  - **Example options**: `[shower, track]`.

- **`nodes.min_size`**
  - Minimum size of clusters to consider. Adjust this to control how small fragments can be before being ignored in aggregation.
  - **Changeable**: Yes
  - **Existing value**: `-1`
  - **Example options**: Any integer (e.g., adjust to set a minimum threshold for fragment size).

- **`nodes.grouping_method`**
  - Method used to group fragments. You can experiment with different methods to see which one works best.
  - **Changeable**: Yes
  - **Existing value**: `score`
  - **Example options**: `distance`, `affinity`, etc.

## 4. Edge Prediction Parameters

These parameters define how the model predicts whether an edge should exist between two nodes (i.e., whether two fragments should be aggregated).

- **`edge_layer.mlp.depth`**
  - Number of layers in the MLP used for edge prediction.
  - **Changeable**: Yes
  - **Existing value**: `3`
  - **Example options**: Adjust based on the complexity of edge prediction.

- **`edge_layer.mlp.width`**
  - Width (number of neurons per layer) of the MLP for edge prediction.
  - **Changeable**: Yes
  - **Existing value**: `64`
  - **Example options**: Any integer (e.g., `32`, `128`).

- **`edge_layer.mlp.activation`**
  - Activation function used in the MLP. This affects how the network learns to aggregate fragments.
  - **Changeable**: Yes
  - **Existing value**: `lrelu` (Leaky ReLU)
  - **Example options**: `relu`, `tanh`, etc.

- **`edge_layer.mlp.normalization`**
  - Normalization layer used in the MLP to help control overfitting and improve convergence.
  - **Changeable**: Yes
  - **Existing value**: `batch_norm`
  - **Example options**: `layer_norm`, `instance_norm`.

## 5. Loss Function Parameters

- **`grappa_loss.node_loss.high_purity`**
  - Whether to only use high-purity clusters in the loss calculation.
  - **Changeable**: Yes
  - **Existing value**: `false`
  - **Options**: `true` or `false`.

- **`grappa_loss.edge_loss.target`**
  - Defines the target for edge prediction. Adjust this depending on whether you want to optimize based on groups or other targets.
  - **Changeable**: Yes
  - **Existing value**: `group`
  - **Example options**: `value`, `affinity`.

# Summary of Key Variables to Tune
- **`graph.max_length`**: Existing value `[500, 0, 500, 500, 0, 0, 0, 25, 0, 25]`. Optimize this for distance cut on edges.
- **`dist_algorithm`**: Existing value `recursive`. Choose an appropriate algorithm for distance calculation.
- **`node_encoder`**: Existing values like `add_points=true`, `dir_max_dist=5`, `add_local_dirs=true`. Adjust features like points, direction vectors, and dE/dx.
- **`edge_encoder`**: Existing value `use_numpy=true`. Tweak edge encoding for better aggregation.
- **`node_layer` and `edge_layer`**: Modify depth (`3`), width (`64`), activation (`lrelu`), and normalization (`batch_norm`) for edge and node prediction.
- **`nodes.shapes`, `min_size`, and `grouping_method`**: Set appropriate values for clustering track and shower fragments (e.g., shapes `[shower, track]`, `min_size=-1`, `grouping_method=score`).

These changes will help you optimize the clustering and aggregation of track and shower fragments in the 2x2 detector reconstruction chain.
