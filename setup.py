from setuptools import setup,find_packages

setup(
    name="hyperlocal-platform",
    version="2.0.1",
    description="This contains the 'Hyperlocal Marketplace' common services,utils,repos and so on...",
    author="Siva-Rajan-R",
    author_email="siva967763@gmail.com",
    url="https://github.com/Siva-Rajan-R/hyperlocal_platform.git",
    packages=find_packages(),
    install_requires=[
        "pyjwt",
        "cryptography",
        "argon2-cffi",
        "orjson",
        "icecream",
        "pytz",
        "pydantic",
        "redis",
        "sqlalchemy"
    ],
    include_package_data=True
)