import asyncio, time

def toBackground(target, *, loop=None, executor=None):
    if loop is None:
        loop = asyncio.get_event_loop()
    if callable(target):
        return loop.run_in_executor(executor, target)
    raise TypeError("target must be a callable, not {!r}".format(type(target)))

# Runs a callback after waitTime
def delayCallback(waitTime, cb):
    def delay():
        time.sleep(waitTime)
        cb()
    return delay
