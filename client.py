import rpyc

if __name__ == '__main__':
    conn = rpyc.connect('localhost', 9981)
    result = conn.root.my_selling_point('600183.SH')
    print(result)




