

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

