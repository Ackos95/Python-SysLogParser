from setuptools import setup, find_packages

setup(
    name='SysLogParser',
    version='0.0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='syslog formatted file parser written in python',
    long_description=open('README.md').read(),
    install_requires=[],
    url='https://github.com/Ackos95/Python-SysLogParser',
    author='Acko Spasic',
    author_email='spasic.acko.95@gmail.com'
)
