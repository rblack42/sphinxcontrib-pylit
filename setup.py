'''
    Sphinxcontrib-pylit
    ~~~~~~~~~~~~~~~~~~~

    Sphinx extension to support Literate Programming.
'''
import io
from setuptools import setup, find_packages


import sphinxcontrib.pylit as lp


def readfile(filename):
    with io.open(filename, encoding="utf-8") as stream:
        return stream.read().split("\n")


readme = readfile("README.rst")

setup(
    name='sphinxcontrib-pylit',
    version=lp.version,
    url=lp.url,
    download_url=lp.pypi,
    license=lp.license,
    author=lp.author,
    author_email=lp.email,
    description=lp.summary,
    long_description="\n".join(readme),
    long_description_content_type='text/x-rst',
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['sphinx', 'sphinx-rtd-theme'],
    entry_points={
            'console_scripts': [
                    'pylitcli = sphinxcontrib.pylit.__main__:cli'
            ]
    },
    namespace_packages=['sphinxcontrib'],
)
