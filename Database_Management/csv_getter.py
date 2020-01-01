import urllib.request
import io
import gzip


def prepare_source(URL):
    print(URL)
    response = urllib.request.urlopen(URL)
    compressed_file = io.BytesIO(response.read())
    decompressed_file = gzip.GzipFile(fileobj=compressed_file)
    with open('/home/v1le/PycharmProjects/scryptradr/Database_Management/source.csv', 'wb') as outfile:
        outfile.write(decompressed_file.read())
