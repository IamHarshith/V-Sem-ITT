with open("hello.txt","r") as fo:
    with open("hi.txt","a") as fw:
        fo.seek(10)
        fw.write(fo.read(14))
        print fo.tell()
        print fo.name

