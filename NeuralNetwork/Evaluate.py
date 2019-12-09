import tensorflow as tf


def evaluate(model, class_names):
    # Replace this with the live api gathering
    test = []
    example = []
    for i in range(0, 900):
        example.append((i - 1000) * i + 1000000)
    test.append(example)

    predictions = model.predict(test)

    print(predictions)

    for i, logits in enumerate(predictions):
        class_idx = tf.argmax(logits).numpy()
        p = tf.nn.softmax(logits)[class_idx]
        name = class_names[class_idx]
        print("Example {} prediction: {} ({:4.1f}%)".format(i, name, 100 * p))

