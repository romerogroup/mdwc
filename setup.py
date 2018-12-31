import setuptools
from numpy.distutils.core import Extension
from numpy.distutils.core import setup

setup(
   name="mdwc",
   version="0.1",
   author="Arturo Hernandez",
   author_email="my@email.com",
   description="Example package to demonstrate wheel issue",
   packages=['mdwc', 'mdwc.software_tools', 'mdwc.MD_suit'],
   ext_modules=[Extension('mdwc.MD_suit.MD_suit',
                          ['mdwc/MD_suit/MD_suit.f90'])],
   scripts=['scripts/mdwc_']
)
