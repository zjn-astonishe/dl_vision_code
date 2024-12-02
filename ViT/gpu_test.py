import tensorflow as tf
# gpus = tf.config.experimental.list_physical_devices(device_type='GPU')
# cpus = tf.config.experimental.list_physical_devices(device_type='CPU')
# print(gpus, cpus)
# print(tf.sysconfig.get_build_info())

# 检查 TensorFlow 版本
print("TensorFlow version:", tf.__version__)

# 检查是否可用的 GPU
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    print("GPUs detected:")
    for gpu in gpus:
        print(gpu)
else:
    print("No GPU detected.")
