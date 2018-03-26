from apscheduler.schedulers.background import BackgroundScheduler
from apps.connect_mysql import connect
'''
这是一个定时的任务
需要在uwsgi中添加

enable-threads = true
;mule = apps/cronjob/__init__.py


目前在使用flask-APScheduler
这是是在同一个web进程中进行的定时任务，而本文件中的方式是另起一个后台线程进行。
'''
sched = BackgroundScheduler()
sched.add_job(connect, 'interval', seconds=5)

sched.start()

## 下面这句加在定时任务模块的末尾...判断是否运行在uwsgi模式下, 然后阻塞mule主线程(猜测).
try:
    import uwsgi
    while True:
        sig = uwsgi.signal_wait()
        print(sig)
except Exception as err:
    pass