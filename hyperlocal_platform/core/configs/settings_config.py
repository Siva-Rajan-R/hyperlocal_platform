from pydantic import ValidationError
from ..settings import HyperLocalPlatformSettings
import sys
from ..constants import ENV_PREFIX
from ..settings import HyperLocalPlatformSettings
from ..utils.settings_initializer import init_settings


SETTINGS: HyperLocalPlatformSettings = init_settings(settings=HyperLocalPlatformSettings,service_name="hyperlocal-platform",env_prefix=ENV_PREFIX)
