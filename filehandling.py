"""with open('test2.txt', 'w') as f:
    f.write('spotlight die unfassbare')

with open('test2.txt', 'r+') as f:
    f_contents=f.read()
    print(f_contents)



  for line in f:
        print(line, end='')



    f_content = f.readline()
    print(f_content, end='')

    f_content = f.readline()
    print(f_content, end='')

    f_content = f.readline()
    print(f_content, end='')"""


with open('foto.jpg', 'rb') as rf:
    with open('foto_copy.jpg', 'wb') as wf:
        chunksize = 1
        rf_chunk=rf.read(chunksize)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk=rf.read(chunksize)
