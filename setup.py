from setuptools import setup, find_packages

NAME = 'kaviyesutil'
VERSION = '0.1.0'
DESCRIPTION = "A set of functions that's often used with Kaviyes related projects."
AUTHOR = 'Kaviyes (Karl Vince Reyes)'
AUTHOR_EMAIL = 'kaviyeslabs@proton.me'
URL = 'https://github.com/Kaviyes/kaviyesutil'
LICENSE = 'MIT'

with open('README.md', 'r', encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=LICENSE,
    package_data={
        '': ['LICENSE']
    },
    packages=find_packages(),
    keywords=['utility'],
    classifiers=[
        'Development Status :: 3 - Alpha',  
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.x',  
        'Operating System :: Microsoft :: Windows',
        'Operating System :: UNIX'
        'Operating System :: MacOS :: MacOS X'
    ],
    install_requires=[ ],
    python_requires='>=3.6',
)
