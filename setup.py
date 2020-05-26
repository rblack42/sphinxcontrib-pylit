'''
    Sphinxcontrib-pylit
    ~~~~~~~~~~~~~~~~~~~

    Sphinx extension to support Literate Programming.
'''
import io
from setuptools import setup, find_packages


from sphinxcontrib.pylit import meta


def readfile(filename):
    with io.open(filename, encoding="utf-8") as stream:
        return stream.read().split("\n")


readme = readfile("README.rst")

setup(
    name='sphinxcontrib-pylit',
    version=meta.version,
    url=meta.url,
    download_url=meta.pypi,
    license=meta.license,
    author=meta.author,
    author_email=meta.email,
    description=meta.summary,
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
    install_requires=['sphinx'],
    entry_points={
            'console_scripts': [
                    'pylitcli = sphinxcontrib.pylit.__main__:cli'
            ]
    },
    namespace_packages=['sphinxcontrib'],
)
