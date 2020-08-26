import logging


logging.basicConfig(
                    filename='/Users/surenderpal/Projects/Ads-Manager/Log/file.log',
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%A %B %d/%m/%Y %H:%M:%S ' 
                                        )

logging.critical('This is critical message')
logging.error('This is error message')
logging.warning('This is warning message')
logging.info('This is info message')
logging.debug('This is debug message')
