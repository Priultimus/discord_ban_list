from setuptools import setup

with open('discord_ban_list/version.py') as fp:
    _loc, _glob = {}, {}
    exec(fp.read(), _loc, _glob)
    version = {**_loc, **_glob}['VERSION']

with open('requirements.txt') as fp:
    requirements = fp.read().splitlines()

with open('README.md') as fp:
    readme = fp.read()

if not version:
    raise RuntimeError('Version is not set in discord_ban_list/version.py')

setup(
    name='discord_ban_list',
    author='romangraef',
    url='https://github.com/romangraef/discord_ban_list',
    version=str(version),
    install_requires=requirements,
    long_description=readme,
    setup_requires=['pytest-runner', 'pytest-pylint'],
    tests_require=['pytest', 'pylint'],
    license='MIT',
    packages=['discord_ban_list'],
    description='Asyncio Python Wrapper for the discord.id ban list.',
    classifiers=[
        'Topic :: Discord',
        'Operating System :: OS Independent',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
