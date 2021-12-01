import tensorflow

weights = tensorflow.constant_initializer([
    [1, 1],
    [1, 0]])
linear_layer = tensorflow.keras.layers.Dense(
    2,
    use_bias=False,
    kernel_initializer=weights,
    input_shape=(2,))
f = tensorflow.ones((1, 2))

print("Fibonacci Numbers:")
while True:
    print(f.numpy()[0][0])
    f = linear_layer(f)
