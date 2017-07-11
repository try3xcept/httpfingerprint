from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='httpfingerprint',
    version='0.1',
    description='No description at this moment',
    long_description=readme(),
    url='https://github.com/try3xcept/httpfingerprint',
    author='try3xcept',
    author_email='try3xcept@gmail.com',
    license='MIT',
    packages=['httpfingerprint'],
    install_requires=[
        'requests>=2.18.1,<3',
    ],
)
