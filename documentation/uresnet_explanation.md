# UResNet Configuration Overview

This configuration file (`uresnet.cfg`) defines various parameters for training and optimizing the UResNet model. Below is a detailed explanation of each section and the customizable options available.

## 1. Base Configuration

This section includes general settings for the model training process.

- **`world_size`**: Controls the number of parallel processes or distributed workers (for multi-GPU or multi-node setups).
  - Options: Any integer (typically `1` for a single GPU setup).

- **`iterations`**: Specifies the number of iterations for training.
  - Options: Any integer (e.g., `25000`). The iteration count depends on the dataset and convergence requirements.

- **`seed`**: Sets the random seed for reproducibility.
  - Options: Any integer.

- **`unwrap`**: Flag to indicate whether to unwrap models during distributed training. If set to true, it unwraps the model and removes any wrapping done by libraries like `torch.nn.DataParallel`.
  - Options: `true` or `false`.

- **`log_dir`**: Specifies the directory where logs will be stored.
  - Options: Any valid directory path.

- **`log_step`**: Determines how often (in terms of iterations) logs should be written.
  - Options: Any integer (e.g., `1` means logging every iteration).

- **`overwrite_log`**: If set to true, overwrites the log file on each run.
  - Options: `true` or `false`.

### `train` Section:

- **`weight_prefix`**: Specifies the path where model weights will be saved.
  - Options: Any valid file path.
  
- **`save_step`**: The frequency (in terms of iterations) at which to save model checkpoints.
  - Options: Any integer.
  
- **`optimizer`**:
  - **`name`**: Specifies the type of optimizer.
    - Options: `Adam`, `SGD`, `RMSprop`, etc.
    
  - **`lr`**: The learning rate for the optimizer.
    - Options: Any floating-point number (e.g., `0.001`).

## 2. IO Configuration

This section defines how data is loaded and processed.

- **`loader`**:
  - **`batch_size`**: The number of samples per batch.
    - Options: Any integer (e.g., `128`).
    
  - **`shuffle`**: If true, shuffles the data at the beginning of each epoch.
    - Options: `true` or `false`.
    
  - **`num_workers`**: Number of workers to use for data loading in parallel.
    - Options: Any integer (e.g., `4`).
    
  - **`collate_fn`**: Specifies the collation function used to merge samples into a batch.
    - Options: Custom function or `all`.
    
  - **`sampler`**: Specifies how data is sampled.
    - Options: `random_sequence`, `sequential`, `distributed`, etc.
    
  - **`dataset`**:
    - **`name`**: The dataset type.
      - Options: `larcv` (in this case, it uses LArCV data format).
      
    - **`file_keys`**: Specifies the dataset file(s).
      - Options: File paths to the dataset.
      
    - **`schema`**: Defines how the dataset is parsed.
      - **`data`**:
        - **`parser`**: Defines how the input data is parsed.
          - Options: `sparse3d`, `dense3d`, etc.
          
        - **`sparse_event`**: Specifies the event key in the input file for sparse data.
        
      - **`seg_label`**:
        - **`parser`**: Defines how the segmentation labels are parsed.
        - **`sparse_event`**: Specifies the event key in the input file for segmentation labels.

## 3. Model Configuration

This section controls the architecture and behavior of the model.

- **`name`**: The name of the model being used.
  - Options: `uresnet`.

- **`weight_path`**: Specifies the path to pre-trained weights. If set to `null`, no pre-trained weights are loaded.
  - Options: File path to pre-trained weights or `null`.

### `network_input` Section:

- **`data`**: Defines the input data tensor to be used in the network.
  - Options: Should match the schema defined in the `io` section (e.g., `data`).

### `loss_input` Section:

- **`seg_label`**: Specifies the tensor to be used as the segmentation label.
  - Options: Should match the schema (e.g., `seg_label`).

### `modules` Section:

#### `uresnet` Module:

- **`num_input`**: Number of input channels (features) in the data.
  - Options: Any integer (e.g., `1`).
  
- **`num_classes`**: Number of segmentation classes.
  - Options: Any integer (e.g., `5`).
  
- **`filters`**: Number of filters for the first convolution layer, determines the model's capacity.
  - Options: Any integer (e.g., `32`).
  
- **`depth`**: The depth of the UResNet network (number of downsampling and upsampling stages).
  - Options: Any integer (e.g., `5`).
  
- **`reps`**: Number of repeated layers at each resolution level.
  - Options: Any integer (e.g., `2`).
  
- **`allow_bias`**: Whether to use bias terms in convolution layers.
  - Options: `true` or `false`.
  
- **`activation`**:
  - **`name`**: Type of activation function.
    - Options: `relu`, `lrelu`, `sigmoid`, `tanh`, etc.
    
  - **`negative_slope`**: If using `lrelu` (leaky ReLU), this controls the slope for negative values.
    - Options: Any floating-point number (e.g., `0.33`).
    
- **`norm_layer`**:
  - **`name`**: Type of normalization layer.
    - Options: `batch_norm`, `instance_norm`, `group_norm`, etc.
    
  - **`eps`**: Epsilon value to prevent division by zero in normalization.
    - Options: Any floating-point number (e.g., `0.0001`).
    
  - **`momentum`**: Momentum factor for batch normalization.
    - Options: Any floating-point number (e.g., `0.01`).

#### `uresnet_loss` Module:

- **`balance_loss`**: Whether to balance the loss to account for class imbalance.
  - Options: `true` or `false`.

## Parameters You Can Change

### Optimizer and Training Configuration:
- Adjust `learning rate (lr)`, `optimizer name`, and `save_step`.

### Batch Size and Data Loading:
- Change `batch_size`, `shuffle`, `num_workers`, `sampler`.

### Model Architecture:
- Modify `filters`, `depth`, `reps`, and activation function (e.g., `lrelu` with different slopes).
- Change normalization settings (`batch_norm` with different `eps` and `momentum` values).

### Loss Handling:
- Enable or disable `balance_loss`.

## Conclusion
Many parameters in this configuration file are customizable. Changing the values should align with your computational resources and your dataset.
