if __name__  == '__main__':
    base = '/opt/RpiTemp/tools'
    finName = '%s/heat_test.conf' %(base)
    foutName = '/etc/init/heat_test.conf'

    with open(finName, 'r') as fin:
        try:
            data = fin.read()
        except Exception, e:
            print e


    with open(foutName, 'w') as fout:
        try:
            fout.write(data)
        except Exception, e:
            print e
