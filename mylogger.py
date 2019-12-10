import logging


class RequestFormatter(logging.Formatter):

    def format(self, record):
        from flask import has_request_context, request

        if has_request_context():
            record.url = request.url
            record.remote_addr = request.remote_addr
        else:
            record.url = None
            record.remote_addr = None

        return super().format(record)


class MyLogger:

    def __init__(self, filename=''):
        if filename != '':
            self.filename = filename
        else:
            self.filename = 'logfile.txt'

        self.logfilename = self.get_log_file_name()

        log_formatter = RequestFormatter(
            '[%(asctime)s] %(remote_addr)s %(levelname)s %(module)s: %(message)s'
        )
        self.logger = logging.getLogger()
        file_handler = logging.FileHandler(self.logfilename)
        file_handler.setFormatter(log_formatter)
        file_handler.setLevel(logging.DEBUG)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(log_formatter)

        self.logger.addHandler(file_handler)
#         self.logger.addHandler(stream_handler)
        print('Logfile: %s' % self.logfilename)


    def get_log_file_name(self):
        import os
        if os.name == 'nt':
            home_path = os.path.abspath(os.getenv('APPDATA'))
            log_dir = os.path.join(home_path, 'log')
        else:
            home_path = os.path.abspath(os.getenv('HOME'))
            log_dir = os.path.join(home_path, '.log')

        os.makedirs(log_dir, exist_ok=True)
        result = os.path.join(log_dir, self.filename)
        return result
