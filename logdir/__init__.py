import arrow
import os


class LogDir:

    def __init__(self):
        import os
        app_name = 'abborders'
        osname = os.name
        if osname == 'nt':
            _log_folder = os.path.join(os.getenv('APPDATA'), 'log', app_name)
        else:
            _log_folder = os.path.join(os.getenv('HOME'), '.log', app_name)

        os.makedirs(_log_folder, exist_ok=True)

        self.log_folder = _log_folder
        return


class LogFile:

    def __init__(self, appname=''):
        if appname == '':
            self.appname = 'app'
        else:
            self.appname = appname

        self.filename = self.appname + '-' + self.get_time_stamp_string() + '.txt'
        log_dir = LogDir().log_folder
        self.full_path = os.path.join(log_dir, self.filename)
        return

    def get_time_stamp_string(self):
        now = arrow.now()
        fn = now.format('YYYYMMDD')
        return fn
