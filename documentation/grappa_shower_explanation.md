# GRAPPA Shower Configuration Overview

This configuration file (`grappa_shower.cfg`) is used for training and optimizing the GRAPPA model for shower reconstruction. Below is a detailed explanation of each section and the available customizable options.

## 1. Base Configuration

- **`world_size`**: Specifies the number of distributed processes or GPUs to use.
  - Options: Any integer (default `1` for single-GPU setup).

- **`iterations`**: The total number of training iterations.
  - Options: Any integer (e.g., `25000`). Adjust based on dataset size or desired number of epochs.

- **`seed`**: Sets the random seed for reproducibility.
  - Options: Any integer.

- **`unwrap`**: Determines whether to unwrap models during distributed training.
  - Options: `true` or `false`.

- **`log_dir`**: Specifies the directory where log files will be saved.
  - Options: Any valid directory path (e.g., `logs`).

- **`log_step`**: The number of iterations between log outputs.
  - Options: Any integer (e.g., `1` for every iteration).

- **`overwrite_log`**: Whether to overwrite the existing log file.
  - Options: `true` or `false`.

### `train` Section:

- **`weight_prefix`**: Prefix for the file paths where model weights will be saved.
  - Options: Any valid directory path (e.g., `weights/grappa_shower/snapshot-`).

- **`save_step`**: The frequency (in iterations) at which to save model checkpoints.
  - Options: Any integer (e.g., `1000`).

- **`optimizer`**:
  - **`name`**: The type of optimizer to use for training.
    - Options: `Adam`, `SGD`, etc.
  - **`lr`**: Learning rate for the optimizer.
    - Options: Any floating-point number (e.g., `0.001`).

## 2. IO Configuration

This section defines how data is loaded and structured for input to the model.

- **`loader`**:
  - **`batch_size`**: The number of samples per batch.
    - Options: Any integer (e.g., `128`).
  
  - **`shuffle`**: Whether to shuffle the data at the start of each epoch.
    - Options: `true` or `false`.
  
  - **`num_workers`**: Number of workers for parallel data loading.
    - Options: Any integer (e.g., `8`).
  
  - **`collate_fn`**: Function to use for collating individual samples into a batch.
    - Options: Custom function or `all`.

  - **`sampler`**: Specifies how data is sampled for each batch.
    - Options: `random_sequence`, `sequential`, `distributed`, etc.

  - **`dataset`**:
    - **`name`**: The type of dataset being used.
      - Options: `larcv` (in this case, LArCV format).
    
    - **`file_keys`**: Path to the dataset files.
      - Options: Any valid file path (e.g., `/sdf/data/neutrino/...`).

    - **`schema`**:
      - **`data`**: Configuration for the input data.
        - **`parser`**: Method to parse the data.
          - Options: `cluster3d`, `sparse3d`, etc.
        
        - **`cluster_event`**: Specifies the cluster event in the input file.
          - Options: Name of the cluster event (e.g., `cluster3d_pcluster`).

        - **`particle_event`**: Specifies the particle event in the input file.
          - Options: Name of the particle event (e.g., `particle_corrected`).

        - **`sparse_semantics_event`**: Specifies the sparse semantics event.
          - Options: Name of the sparse semantics event (e.g., `sparse3d_pcluster_semantics`).

        - **`add_particle_info`**: Whether to include particle information.
          - Options: `true` or `false`.

        - **`clean_data`**: Whether to clean the data.
          - Options: `true` or `false`.

      - **`coord_label`**:
        - **`parser`**: Method to parse the particle coordinates.
          - Options: `particle_coords`.

        - **`particle_event`**: Specifies the particle event for the coordinate label.
          - Options: Same as above (`particle_corrected`).

        - **`cluster_event`**: Specifies the cluster event for the coordinate label.
          - Options: Same as above (`cluster3d_pcluster`).

## 3. Model Configuration

This section defines the architecture of the GRAPPA model and the inputs/outputs for training.

- **`name`**: The name of the model.
  - Options: `grappa`.

- **`weight_path`**: Specifies the path to pre-trained weights (or `null` for no pre-trained weights).
  - Options: Any valid file path or `null`.

### `network_input` Section:

- **`data`**: Specifies the input tensor for the model.
  - Options: Must match the data schema (e.g., `data`).

- **`coord_label`**: Specifies the coordinate label tensor.
  - Options: Must match the data schema (e.g., `coord_label`).

### `loss_input` Section:

- **`clust_label`**: Specifies the clustering label tensor.
  - Options: Must match the data schema (e.g., `data`).

### `modules` Section:

#### `grappa` Module:

- **`nodes`**:
  - **`source`**: Defines the source of the clusters.
    - Options: `cluster` or other sources depending on the use case.
  
  - **`shapes`**: Defines the shapes to detect.
    - Options: `shower`, `michel`, `delta`, etc.

  - **`min_size`**: Minimum size for clusters.
    - Options: Any integer (e.g., `-1` to allow all sizes).

  - **`make_groups`**: Whether to group clusters together.
    - Options: `true` or `false`.

  - **`grouping_method`**: Method for grouping clusters.
    - Options: `score`, or any custom grouping method.

- **`graph`**:
  - **`name`**: The type of graph to construct.
    - Options: `complete`, `knn`, etc.
    
  - **`max_length`**: Maximum distance allowed for edges in the graph.
    - Options: List of integers (e.g., `[500, 0, 500, ...]`).
    
  - **`dist_algorithm`**: The algorithm to compute distances.
    - Options: `recursive`, `euclidean`, etc.

- **`node_encoder`**:
  - **`name`**: Type of encoding for the nodes.
    - Options: `geo`, `mlp`, etc.

  - **`use_numpy`**: Whether to use NumPy for computations.
    - Options: `true` or `false`.

  - **`add_value`**: Whether to add the value of the clusters.
    - Options: `true` or `false`.

  - **`add_shape`**: Whether to add the shape of the clusters.
    - Options: `true` or `false`.

  - **`add_points`**: Whether to add the points (coordinates) of the clusters.
    - Options: `true` or `false`.

  - **`add_local_dirs`**: Whether to add local directions to the nodes.
    - Options: `true` or `false`.

  - **`dir_max_dist`**: Maximum distance for direction vectors.
    - Options: Any floating-point number (e.g., `5`).

  - **`add_local_dedxs`**: Whether to add local dE/dx values (energy deposition).
    - Options: `true` or `false`.

  - **`dedx_max_dist`**: Maximum distance for dE/dx values.
    - Options: Any floating-point number (e.g., `5`).

- **`edge_encoder`**:
  - **`name`**: Type of encoding for the edges.
    - Options: `geo`, `mlp`, etc.

  - **`use_numpy`**: Whether to use NumPy for edge computations.
    - Options: `true` or `false`.

- **`gnn_model`**:
  - **`name`**: The type of GNN (Graph Neural Network) model.
    - Options: `meta`, `gcn`, etc.
  
  - **`node_feats`**: Number of features for each node.
    - Options: Any integer (e.g., `33`).

  - **`edge_feats`**: Number of features for each edge.
    - Options: Any integer (e.g., `19`).

  - **`node_pred`**: Number of node prediction classes.
    - Options: Any integer (e.g., `2`).

  - **`edge_pred`**: Number of edge prediction classes.
    - Options: Any integer (e.g., `2`).

  - **`edge_layer`**: Configuration for the edge prediction layer.
    - **`name`**: Type of layer.
      - Options: `mlp`, etc.
    
    - **`mlp`**: Parameters for the MLP (multi-layer perceptron) edge layer.
      - **`depth`**: Number of layers in the MLP.
        - Options: Any integer (e.g., `3`).

      - **`width`**: Number of units in each layer.
        - Options: Any integer (e.g., `64`).

      - **`activation`**: Activation function for the MLP.
        - **`name`**: Type of activation function.
          - Options: `lrelu`, `relu`, etc.
        
        - **`negative_slope`**: The negative slope for `lrelu`.
          - Options: Any floating-point number (e.g., `0.1`).

      - **`normalization`**: Type of normalization layer.
        - Options: `batch_norm`, `layer_norm`, etc.

  - **`node_layer`**: Configuration for the node prediction layer.
    - Similar options as the `edge_layer` with additional parameters like `reduction` (e.g., `max`) and `attention`.

#### `grappa_loss` Module:

- **`node_loss`**:
  - **`name`**: Type of node loss function.
    - Options: `shower_primary`, `binary_crossentropy`, etc.
  
  - **`high_purity`**: Whether to only use high purity clusters.
    - Options: `true` or `false`.
  
  - **`use_group_pred`**: Whether to use predicted groups for loss calculation.
    - Options: `true` or `false`.

- **`edge_loss`**:
  - **`name`**: Type of edge loss function.
    - Options: `channel`, `binary_crossentropy`, etc.
  
  - **`target`**: Target for the edge loss (e.g., group or direct values).
    - Options: `group`, `value`, etc.
  
  - **`high_purity`**: Whether to only use high purity edges.
    - Options: `true` or `false`.

## Conclusion

The `grappa_shower.cfg` provides several customizable parameters related to data handling, model architecture, graph structure, and loss function choices. You can modify parameters based on dataset size, computational resources, and desired performance.
