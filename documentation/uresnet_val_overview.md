## Overview of `uresnet_val.cfg` Configuration File

The `uresnet_val.cfg` file defines how the UResNet model will be validated using **SPINE**. It shares many similarities with the training configuration but is tailored for the validation process.

### 1. Base Configuration
This section defines general settings for the validation process:

- **`world_size: 1`**: Specifies the number of GPUs to use (1 GPU in this case).
- **`iterations: 100`**: The number of iterations for validation (~0.5 epochs).
- **`seed: 0`**: A random seed for reproducibility.
- **`unwrap: false`**: This setting should remain `false` during validation to avoid unnecessary operations.
- **`log_dir: logs/uresnet`**: Specifies the directory where logs will be saved.
- **`log_step: 1`**: Log validation information after every iteration.
- **`overwrite_log: true`**: If set to `true`, existing logs will be overwritten.

### 2. IO (Input/Output) Configuration
This section controls how the data is loaded for validation:

- **`loader` block**:
  - **`batch_size: 128`**: Specifies the size of each validation batch.
  - **`shuffle: false`**: Shuffling is turned off for validation to ensure deterministic evaluation.
  - **`num_workers: 4`**: Number of CPU cores used for data loading.
  - **`collate_fn: all`**: Specifies how data samples are combined into batches.
  
- **`dataset` block**:
  - **`name: larcv`**: Specifies the format of the dataset.
  - **`file_keys: /sdf/data/neutrino/generic/mpvmpr_2020_01_v04/test.root`**: Path to the validation dataset.
  - **`schema` block**:
    - **`data`**:
      - **`parser: sparse3d`**: Specifies how to parse the data (sparse3D format).
      - **`sparse_event: sparse3d_pcluster`**: Label for sparse 3D cluster data.
    - **`seg_label`**:
      - **`parser: sparse3d`**: Specifies how to parse segmentation labels.
      - **`sparse_event: sparse3d_pcluster_semantics`**: Label for sparse 3D segmentation labels.

### 3. Model Configuration
This section defines the model and how the validation will use it:

- **`name: uresnet`**: Specifies the UResNet model.
- **`weight_path: weights/uresnet/snapshot*.ckpt`**: Specifies the path to the saved model weights that will be used for validation.

- **`network_input` block**:
  - **`data: data`**: Defines the input data for the network.
  
- **`loss_input` block**:
  - **`seg_label: seg_label`**: Specifies the segmentation labels for validation.

### 4. Modules
This section describes the UResNet model architecture for validation:

- **`uresnet` block**:
  - **`num_input: 1`**: Number of input channels (1 for grayscale images).
  - **`num_classes: 5`**: Number of output classes.
  - **`filters: 32`**: Number of filters in the first convolutional layer.
  - **`depth: 5`**: The depth of the UResNet architecture (5 layers).
  - **`reps: 2`**: Each layer is repeated twice.
  - **`allow_bias: false`**: No bias term is used in the convolutional layers.
  - **`activation` block**:
    - **`name: lrelu`**: Leaky ReLU activation function.
    - **`negative_slope: 0.33`**: Slope for the Leaky ReLU function.
  - **`norm_layer` block**:
    - **`name: batch_norm`**: Applies batch normalization.
    - **`eps: 0.0001`**: Epsilon for numerical stability in batch normalization.
    - **`momentum: 0.01`**: Momentum for batch normalization.

- **`uresnet_loss` block**:
  - **`balance_loss: false`**: The loss function is not balanced across different classes.

### Purpose
The `uresnet_val.cfg` configuration file is specifically designed for validating the performance of a **UResNet model** on a test dataset. It loads previously saved model weights, runs the model for 100 iterations on the test data, and logs the validation results. This configuration ensures that the model's performance is evaluated in a controlled, deterministic environment.
