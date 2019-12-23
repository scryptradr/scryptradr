import tensorflow as tf


def setupNetwork(neurons_in_input_layer, hidden_layer, neurons_in_output_layer, attributes, compiler):

    # Add input layer
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Dense(
        name='Input_Layer',
        units=neurons_in_input_layer,
        input_dim=neurons_in_input_layer,
        kernel_initializer=attributes[0][1],
        bias_initializer=attributes[0][2],
        activation=attributes[0][0])
    )

    # Add hidden layers

    current = hidden_layer[0]
    operation = hidden_layer[1]
    if isinstance(hidden_layer[1], str):
        difference_per_layer = hidden_layer[2]
        max_hidden_layers = hidden_layer[3]
    else:
        max_hidden_layers = len(hidden_layer)
    counter = 1
    while current > 0 and max_hidden_layers > 0:
        print("Hidden " + str(counter) + " is " + str(current))
        model.add(tf.keras.layers.Dense(
            name='Hidden_Layer' + str(counter),
            units=current,
            input_dim=current,
            kernel_initializer=attributes[1][1],
            bias_initializer=attributes[1][2],
            activation=attributes[1][0])
        )
        if operation == 'add':
            current += difference_per_layer
        elif operation == 'sub':
            current -= difference_per_layer
        elif operation == 'mul':
            current *= difference_per_layer
        elif counter < len(hidden_layer):
            current = hidden_layer[counter]
        max_hidden_layers -= 1
        counter += 1

    # Add output layer
    model.add(tf.keras.layers.Dense(
        name='Output_Layer',
        units=neurons_in_output_layer,
        input_dim=neurons_in_output_layer,
        kernel_initializer=attributes[2][1],
        bias_initializer=attributes[2][2],
        activation=attributes[2][0])
    )

    # Compile model
    model.compile(optimizer=compiler[0], loss=compiler[1])
    return model