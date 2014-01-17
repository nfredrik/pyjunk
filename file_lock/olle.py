import lockfile

# http://pythonhosted.org/lockfile/lockfile.html#examples

print dir(lockfile)

lock = lockfile.FileLock("other")
while not lock.i_am_locking():
    try:
        lock.acquire(timeout=60)    # wait up to 60 seconds
    except LockTimeout:
        lock.break_lock()
        lock.acquire()
print "I locked", lock.path
lock.release()

