import mmap

filename = 'myfile.txt'

# create a file with dummy data
with open(filename, "wb") as f:
    f.write(b"Hello Python!456" * 10)
    f.close() # read data from mmap'ed file

with open(filename, 'r') as f: 
    try:    
        m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)  
        try:        # access file via a memory mapped area        [...]
            pass  
        finally:
            m.close()
    finally:
        f.close() 