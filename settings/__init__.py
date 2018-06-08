# -*- coding: utf-8 -*-

import logging
import os

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
)

logger = logging.getLogger(__name__)
logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3.connectionpool").setLevel(logging.WARNING)
logging.getLogger("jieba").setLevel(logging.WARNING)
logging.getLogger("wxpy.api.bot").setLevel(logging.WARNING)
logging.getLogger("wxpy.api.chats.chat").setLevel(logging.WARNING)

def load_config():
    # mode = os.environ.get('MODE')
    mode = 'PRODUCTION'
    try:
        if mode == 'PRODUCTION':
            from .production import ProductionConfig
            return ProductionConfig
        elif mode == 'TESTING':
            from .testing import TestingConfig
            return TestingConfig
        else:
            from .development import DevelopmentConfig
            return DevelopmentConfig
    except ImportError as e:
        logger.warn('Configuration Import Error: {error}.'.format(error=str(e)))
