'''
https://raw.githubusercontent.com/laserson/rock-health-python/master/get_some_ngrams.py

# make sure to change the HFDS directories in the script
hadoop fs -mkdir -p /user/laserson/rock-health-python/ngrams
'''


import sys
import random
import subprocess
import os

GB = 1024 * 1024 * 1024


def downloadData():
    ngram_urls = []

    # generate list of URLs
    base_url = 'http://storage.googleapis.com/books/ngrams/books/googlebooks-eng-all-%igram-20090715-%i.csv.zip'
    sizes = [(2, 100), (3, 200), (4, 400), (5, 800)]
    for size in sizes:
        n = size[0]
        num_files = size[1]
        for i in xrange(num_files):
            ngram_urls.append(base_url % (n, i))


    # download data
    stream_cmd = 'curl -O "%s"'
    random.shuffle(ngram_urls)
    finished = False
    total_size = 0

    while not finished:
        url = ngram_urls.pop()
        filename = url.split('/')[-1]
        sys.stdout.write("%s\n" % filename)
        sys.stdout.flush()
        subprocess.Popen(stream_cmd % url, shell=True).wait()
        total_size += os.path.getsize(filename)
        if total_size > 2 * GB:
            break
    return ngram_urls



def loadDataHDFS():
    file_count = 3
    for ngram in os.listdir('.'):
        if ngram.endswith('.csv.zip'):
            stream_cmd = 'funzip %s | hadoop fs -put - /user/laserson/rock-health-python/ngrams/%s'
            filename = '.'.join(ngram.split('.')[:-1])
            sys.stdout.write("%s\n" % filename)
            sys.stdout.flush()
            cmd = stream_cmd % (ngram, filename)
            subprocess.Popen(cmd, shell=True).wait()
            file_count -= 1
            if file_count == 0:
                break

#downloadData()
loadDataHDFS()

