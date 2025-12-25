from pydantic import ValidationError
from .settings import HyperLocalPlatformSettings
import sys
from .constants import ENV_PREFIX


def load_platform_settings() -> HyperLocalPlatformSettings:
    try:
        return HyperLocalPlatformSettings()
        
    except ValidationError as e:
        print("\n❌PLATFORM CONFIGURATION ERROR\n")

        missing = [
            err["loc"][0]
            for err in e.errors()
            if err["type"] == "missing"
        ]

        if missing:
            print("The following environment variables are REQUIRED for HYPERLOCAL-PLAFORM:\n")
            for field in missing:
                print(f"  - {ENV_PREFIX}{field}")

        print("\nFix your .env or environment variables and restart.\n")
        sys.exit(1)


SETTINGS: HyperLocalPlatformSettings = load_platform_settings()
