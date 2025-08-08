# Worker process to run queued jobs (RQ)
import redis
from rq import Worker, Queue
from settings import REDIS_URL

listen = ['resets']
conn = redis.from_url(REDIS_URL)

if __name__ == '__main__':
    queues = [Queue(name, connection=conn) for name in listen]
    worker = Worker(queues, connection=conn)
    worker.work()
