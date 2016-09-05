VERSION = (3, 0, 1)
__version__ = '.'.join(map(str, VERSION if VERSION[-1] else VERSION[:2]))


from django.apps import AppConfig

from .simple import *   # flake8: noqa
from .query import *   # flake8: noqa
from .invalidation import *   # flake8: noqa
from .templatetags.cacheops import *   # flake8: noqa
from .transaction import install_cacheops_transaction_support


class CacheopsConfig(AppConfig):
    name = 'cacheops'

    def ready(self):
        install_cacheops()
        install_cacheops_transaction_support()

default_app_config = 'cacheops.CacheopsConfig'
