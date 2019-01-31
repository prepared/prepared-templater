import os
from distutils.command.build import build

from django.core import management
from setuptools import setup, find_packages


try:
    with open(os.path.join(os.path.dirname(__file__), 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()
except:
    long_description = ''


class CustomBuild(build):
    def run(self):
        management.call_command('compilemessages', verbosity=1)
        build.run(self)


cmdclass = {
    'build': CustomBuild
}


setup(
    name='prepared_templater',
    version='1.0.0',
    description='Allows to use a pretix event as a template for further events',
    long_description=long_description,
    url='github.com/bockstaller/prepared_templater',
    author='Lukas Bockstaller',
    author_email='lukas.bockstaller@posteo.de',
    license='Apache Software License',

    install_requires=[],
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    cmdclass=cmdclass,
    entry_points="""
[pretix.plugin]
prepared_templater=prepared_templater:PretixPluginMeta
""",
)
