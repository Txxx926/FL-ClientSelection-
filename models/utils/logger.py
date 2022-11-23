import logging
import os
class Logger():
    logger = None
    log_name = 'default'
    
    def get_logger(self):
        if Logger.logger != None:
            return Logger.logger
        log_file = '{}.log'.format(Logger.log_name)
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        logging.basicConfig(level = logging.INFO, 
                    filename=log_file,
                    filemode='w',
                    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        Logger.logger = logging.getLogger('FL-type')
        sh = logging.StreamHandler()
        sh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        Logger.logger.addHandler(sh)
        log_file_name = os.path.join(Logger.log_name.split('/')[-1]+".log")
        #fh = logging.FileHandler(log_file_name,encoding="UTF-8")
        #Logger.logger.addHandler(fh)
        Logger.logger.info('logger init finished ---- log file: {}'.format(log_file))
        print("log file-----",log_file)
        return Logger.logger
    
    def set_log_name(self, name):
        while name[-4:] == '.log':
            name = name[:-4]
        Logger.log_name = name
