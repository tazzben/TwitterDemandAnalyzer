try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

long_desc = """
	A analysis tool (to be used on the data created by the collector) for economists using the fact that twitter presents a demand curve for information
"""


setup(name="TwitterDemandAnalyzer",
      version=1.1,
      description="A analysis tool (to be used on the data created by the collector) for economists using the fact that twitter presents a demand curve for information",
      author="Ben Smith",
      author_email="tazz_ben@ad.wsu.edu",
      url="https://github.com/tazzben/TwitterDemandAnalyzer",
      license="Public Domain",
      packages=[],
	  scripts=['TwitterDemandAnalyzer'],
	  package_dir={},
      long_description=long_desc,
      classifiers=[
          'Topic :: Scientific/Engineering',
          'Environment :: Console',
          'Development Status :: 5 - Production/Stable',
          'Operating System :: POSIX',
          'Intended Audience :: Science/Research'
      ]
     )