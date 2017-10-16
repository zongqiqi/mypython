from gevent import monkey
monkey.patch_all()#由于切换是在IO操作时自动完成，所以gevent需要修改Python自带的一些标准库，这一过程在启动时通过monkey patch完成
import gevent
import requests

def f(url):
    print('GET: %s' % url)
    resp = requests.get(url)
    data=resp.content
    print('%d bytes received from %s.' % (len(data), url))

gevent.joinall([#添加协程任务，并启动运行
        gevent.spawn(f, 'https://www.python.org/'),#spawn用来形成协程
        gevent.spawn(f, 'https://www.yahoo.com/'),
        gevent.spawn(f, 'https://github.com/'),
])