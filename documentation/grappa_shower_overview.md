## Overview of `grappa_shower.cfg` Configuration File

The `grappa_shower.cfg` file defines the training configuration for a **GRAPPA**-based model using **SPINE**. This file configures how the model will process 3D cluster and particle data for training.

### 1. Base Configuration
This section defines general training settings:

- **`world_size: 1`**: Specifies the number of GPUs to use (in this case, 1 GPU).
- **`iterations: 25000`**: The total number of training iterations (~25 epochs).
- **`seed: 0`**: Random seed for reproducibility.
- **`unwrap: false`**: Disables breaking down input/output images in the batch (saves time during training).
- **`log_dir: logs`**: Directory where training logs will be stored.
- **`log_step: 1`**: Logging frequency, logs will be written every iteration.
- **`overwrite_log: true`**: Allows overwriting existing logs.
  
- **`train` block**:
  - **`weight_prefix: weights/grappa_shower/snapshot-`**: Path where model weights will be saved.
  - **`save_step: 1000`**: Specifies how frequently to save model weights (every epoch in this case).
  - **`optimizer` block**:
    - **`name: Adam`**: Specifies the use of the Adam optimizer.
    - **`lr: 0.001`**: The learning rate for the optimizer.

### 2. IO (Input/Output) Configuration
This section defines how data is loaded during training:

- **`loader` block**:
  - **`batch_size: 128`**: The batch size for training.
  - **`shuffle: false`**: Data shuffling is disabled (randomization is handled by a custom sampler).
  - **`num_workers: 8`**: Number of CPU cores used for data loading.
  - **`collate_fn: all`**: Specifies how to combine individual data samples into batches.
  - **`sampler: random_sequence`**: Uses a random sequence sampler for loading data.

- **`dataset` block**:
  - **`name: larcv`**: Specifies the format of the dataset.
  - **`file_keys: /sdf/data/neutrino/generic/mpvmpr_2020_01_v04/train.root`**: Path to the training dataset.
  
  - **`schema` block**:
    - **`data` block**:
      - **`parser: cluster3d`**: Specifies how to parse the 3D cluster data.
      - **`cluster_event: cluster3d_pcluster`**: Event label for 3D cluster data.
      - **`particle_event: particle_corrected`**: Event label for corrected particle data.
      - **`sparse_semantics_event: sparse3d_pcluster_semantics`**: Event label for semantic sparse 3D cluster data.
      - **`add_particle_info: true`**: Enables adding additional particle information.
      - **`clean_data: true`**: Specifies whether to clean the data before processing.
      
    - **`coord_label` block**:
      - **`parser: particle_coords`**: Parser for particle coordinates.
      - **`particle_event: particle_corrected`**: Event label for corrected particle data.
      - **`cluster_event: cluster3d_pcluster`**: Event label for the 3D cluster data.

### 3. Model Configuration
This section defines the **GRAPPA** model and its components:

- **`name: grappa`**: Specifies the GRAPPA model.
- **`weight_path: null`**: No pretrained weights are used for the training.

- **`network_input` block**:
  - **`data: data`**: Defines the input data for the network.
  - **`coord_label: coord_label`**: Specifies the coordinate labels as input.
  
- **`loss_input` block**:
  - **`clust_label: data`**: Specifies the cluster label to be used for calculating loss.

### 4. Modules
This section defines the specific components of the GRAPPA model and its architecture:

- **`grappa` block**:
  - **`nodes` block**:
    - **`source: cluster`**: Specifies that the source is the cluster data.
    - **`shapes: [shower, michel, delta]`**: Specifies the types of shapes to identify: shower, Michel electron, and delta.
    - **`min_size: -1`**: Minimum size filter for the clusters (set to -1, no filtering).
    - **`make_groups: false`**: Groups are not created automatically.
    - **`grouping_method: score`**: Clusters are grouped based on a scoring mechanism.
    
  - **`graph` block**:
    - **`name: complete`**: Defines a complete graph for connecting the nodes.
    - **`max_length`**: Maximum distance between nodes for creating edges.

  - **`node_encoder` block**:
    - **`name: geo`**: Specifies the geometry-based node encoder.
    - Various options like `add_value`, `add_shape`, `add_points`, etc. allow adding different geometric features to the node representation.

  - **`edge_encoder` block**:
    - **`name: geo`**: Specifies a geometry-based edge encoder.

  - **`gnn_model` block**:
    - **`name: meta`**: Specifies the use of a meta-learning GNN model.
    - **`node_feats: 33`**: Number of features for each node.
    - **`edge_feats: 19`**: Number of features for each edge.
    - **`node_pred: 2`**: Number of output predictions for each node.
    - **`edge_pred: 2`**: Number of output predictions for each edge.
    - **`edge_layer` block**:
      - Specifies a multilayer perceptron (MLP) with 3 layers for predicting edges.
    - **`node_layer` block**:
      - Specifies an MLP for predicting node states with options for normalization, aggregation, and activation functions.

- **`grappa_loss` block**:
  - **`node_loss` block**:
    - **`name: shower_primary`**: Specifies that the primary loss is for shower segmentation.
  - **`edge_loss` block**:
    - **`name: channel`**: Specifies the edge loss based on the "channel" connection between nodes.

### Purpose
The `grappa_shower.cfg` file sets up the GRAPPA model for 3D cluster-based training, primarily focusing on recognizing shapes like showers, Michel electrons, and delta rays. The file controls the training process, specifying how the dataset is loaded, how the model is configured, and how the training is performed. It trains the model for 25,000 iterations and saves checkpoints every 1,000 iterations while utilizing various geometric features for both node and edge encoding.
