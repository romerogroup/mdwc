import setuptools
from numpy.distutils.core import Extension
from numpy.distutils.core import setup

setup(
   name="mdwc",
   version="0.1",
   author="Arturo Hernandez",
   author_email="my@email.com",
   description="Example package to demonstrate wheel issue",
   packages=['mdwc', 'mdwc.software_tools', 'mdwc.MD_suite'],
   ext_modules=[Extension('mdwc.MD_suite.MD_suite',
                          ['mdwc/MD_suite/MD_suite.f90'])],
   scripts=['scripts/mdwc_']
)
