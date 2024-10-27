import tensorflow as tf

# Check if a GPU device is available
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
