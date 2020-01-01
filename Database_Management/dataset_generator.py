import csv
import operator
import os
import csv_getter
from pydub import AudioSegment
from pydub.playback import play
from shutil import copy
import random

i = 1
i = str(i).zfill(2)
counter = 1
while counter <= 31:
    print(i)
    final = 'final' + str(random.randrange(0, 1000000000)) + '.csv'
    URL = 'https://s3-eu-west-1.amazonaws.com/public.bitmex.com/data/trade/201912' + i + '.csv.gz'
    csv_getter.prepare_source(URL)

    # deleting all unneeded columns
    with open('source.csv', 'rt') as inp, open('first_edit.csv', 'wt', newline='') as out:
        writer = csv.writer(out)
        reader = csv.reader(inp)
        for column in reader:
            writer.writerow((column[0], column[1], column[4]))
        inp.close()
        out.close()

    # deleting all rows not containing XBTUSD values
    with open('first_edit.csv', 'rt') as inp, open('second_edit.csv', 'wt', newline='') as out:
        writer = csv.writer(out)
        reader = csv.reader(inp)
        for row in reader:
            if row[1] == "XBTUSD":
                writer.writerow(row)
        inp.close()
        out.close()

    # deleting symbol column
    with open('second_edit.csv', 'rt') as inp, open('third_edit.csv', 'wt', newline='') as out:
        writer = csv.writer(out)
        reader = csv.reader(inp)
        for column in reader:
            writer.writerow((column[0], column[2]))
        inp.close()
        out.close()

    # sorting list by timestamp
    with open('third_edit.csv', 'rt') as inp, open('sorted.csv', 'wt', newline='') as out:
        writer = csv.writer(out)
        reader = csv.reader(inp)
        sortedlist = sorted(reader, key=operator.itemgetter(0))
        for row in sortedlist:
            writer.writerow(row)

    # finalizing list with one value per second
    with open('sorted.csv', 'rt') as inp, open(final, 'wt', newline='') as out:
        writer = csv.writer(out)
        reader = csv.reader(inp)
        current = 0
        for row in reader:
            var = row[0]
            sliced = var[17:19]
            if current != sliced:
                writer.writerow(row)
                current = sliced
        inp.close()
        out.close()

    # removing unneeded temporary files
    os.remove('first_edit.csv')
    os.remove('second_edit.csv')
    os.remove('third_edit.csv')
    os.remove('sorted.csv')
    copy(final, '/home/v1le/Documents/Finished_Dataset')
    os.remove(final)
    os.remove('source.csv')
    counter += 1
    i = str(counter)
    i = str(i).zfill(2)
song = AudioSegment.from_mp3('audio.mp3')
play(song)
