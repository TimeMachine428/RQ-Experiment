import time

from redis import Redis
from rq import Queue
from stuff import count_words_at_url

q = Queue(connection=Redis(host='redis'))

start_millis = int(round(time.time() * 1000))

for i in range(10000):
    result = q.enqueue(count_words_at_url, 'http://nvie.com')

end_millis = int(round(time.time() * 1000))

print("10000 tasks complete in: %d (ms)" % (end_millis - start_millis))
