## Overview of `uresnet.cfg` Configuration File

The `uresnet.cfg` configuration file defines how the UResNet model will be trained using **SPINE** for a semantic segmentation task. Below is a breakdown of the key components.

### 1. Base Configuration
This section defines general settings for the training process:

- **`world_size: 1`**: Specifies the number of GPUs to use (1 GPU in this case).
- **`iterations: 25000`**: The number of training iterations (~25 epochs).
- **`seed: 0`**: A random seed for reproducibility.
- **`unwrap: false`**: Do not break down input/output images within the batch (this is not necessary for training).
- **`log_dir: logs/uresnet`**: The directory where training logs will be saved.
- **`log_step: 1`**: Log training information after every iteration.
- **`overwrite_log: true`**: Overwrite existing logs if they already exist.

Within the `train` block:
- **`weight_prefix: weights/uresnet/snapshot`**: Specifies where to save model weights.
- **`save_step: 1000`**: Save the model weights every 1,000 iterations.
- **`optimizer` block**:
  - **`name: Adam`**: Use the Adam optimizer for training.
  - **`lr: 0.001`**: Learning rate for the optimizer.

### 2. IO (Input/Output) Configuration
This section controls how the data will be loaded for training:

- **`loader` block**:
  - **`batch_size: 128`**: The size of each training batch.
  - **`shuffle: false`**: Data shuffling is disabled (randomization is done via a sampler).
  - **`num_workers: 4`**: Number of CPU cores used for data loading.
  - **`collate_fn: all`**: Specifies how to combine data samples into batches.
  - **`sampler: random_sequence`**: Load data using a random sequence.
  
- **`dataset` block**:
  - **`name: larcv`**: Specifies the dataset format.
  - **`file_keys: /sdf/data/neutrino/generic/mpvmpr_2020_01_v04/train.root`**: Path to the training dataset.
  - **`schema` block**:
    - **`data`**:
      - **`parser: sparse3d`**: Specifies that the data format is sparse3D.
      - **`sparse_event: sparse3d_pcluster`**: Label for sparse 3D cluster data.
    - **`seg_label`**:
      - **`parser: sparse3d`**: Specifies the format for segmentation labels.
      - **`sparse_event: sparse3d_pcluster_semantics`**: Label for sparse 3D segmentation.

### 3. Model Configuration
This section defines the UResNet model:

- **`name: uresnet`**: Specifies the UResNet model to be used.
- **`weight_path: null`**: No pretrained weights are used for this model.
  
- **`network_input` block**:
  - **`data: data`**: Specifies the input data for the network (defined in the `IO` block).
  
- **`loss_input` block**:
  - **`seg_label: seg_label`**: Specifies the segmentation labels used in the loss function.

### 4. Modules
This section describes the architecture of the UResNet model and its loss function:

- **`uresnet` block**:
  - **`num_input: 1`**: Number of input channels (1 for grayscale images).
  - **`num_classes: 5`**: The number of output classes.
  - **`filters: 32`**: Number of filters in the first convolutional layer.
  - **`depth: 5`**: The depth of the UResNet architecture (5 layers).
  - **`reps: 2`**: Each layer is repeated twice.
  - **`allow_bias: false`**: No bias term is used in the convolutional layers.
  - **`activation` block**:
    - **`name: lrelu`**: Leaky ReLU activation function.
    - **`negative_slope: 0.33`**: Slope for the Leaky ReLU function.
  - **`norm_layer` block**:
    - **`name: batch_norm`**: Use batch normalization.
    - **`eps: 0.0001`**: Epsilon value to prevent division by zero.
    - **`momentum: 0.01`**: Momentum for the moving average in batch normalization.
  
- **`uresnet_loss` block**:
  - **`balance_loss: false`**: The loss function is not balanced across different classes.

### Purpose
The `uresnet.cfg` file defines the training process for a **UResNet model**, which is used for **3D sparse image segmentation**. The model is configured to run for 25,000 iterations, with model checkpoints saved every 1,000 iterations. It also logs the training progress after each iteration and uses the Adam optimizer to adjust the model weights.
