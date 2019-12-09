import csv
import os
import tensorflow as tf


def trainNetwork(model, neurons_in_input_layer, epochs_per_file, overlap):
    column_values = 0
    column_desired = 1
    delimiter = ';'

    fileCount = 0
    for _ in os.listdir(os.fsencode('Checkpoints')):
        fileCount += 1

    for file in os.listdir(os.fsencode('Data')):
        filename = "Data\\" + os.fsdecode(file)
        data = []
        desired = []
        d = []
        if filename.endswith('.CSV'):
            with open(filename) as csv_file:
                content = csv.reader(csv_file, delimiter=delimiter)

                for row in content:
                    d.append(row[column_values])
                    if row[column_desired] != '':
                        des = int(row[column_desired])
                        if des == 0:
                            desired.append([1, 0, 0])
                        elif des == 1:
                            desired.append([0, 1, 0])
                        else:
                            desired.append([0, 0, 1])

                counter = 0
                while counter <= (len(d) - 1):
                    tmp = []
                    for i in range(0, neurons_in_input_layer):
                        tmp.append(float(d[counter + i]))
                    data.append(tmp)
                    counter += neurons_in_input_layer - overlap

                (tf.keras.models.Sequential()(model)).fit(data, desired, epochs=epochs_per_file)

                fileCount += 1
                model.save('Checkpoints\\Save-' + str(fileCount) + '.h5')

    return model
