import os
from setuptools import setup

def readme():
    fp = os.path.join(os.path.dirname(__file__), 'README.md')
    with open(fp, encoding='utf-8', mode='r') as f:
        return f.read()


setup(
    name='Minimal Server',
    version='1.0.1',
    packages=['minimal_server'],
    description=('Serve a python object through a simple socket; '
                 'supports multiple connections.'),
    long_description=readme(),
    long_description_content_type='text/markdown',
    author='Luca Soldaini',
    author_email='luca@soldaini.net',
    license='MIT License',
    url='https://github.com/soldni/MinimalServer',
    classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 3',
            'Topic :: System :: Networking',

        ]
      )
