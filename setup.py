"""Setup script for extension."""

from setuptools import setup

setup(
  name='grow-ext-html-beaufier',
  version='1.0.0',
  license='MIT',
  author='Luis Villalba',
  author_email='luismvillalba@gmail.com',
  include_package_data=False,
  packages=[
    'html_beautifier',
  ],
  install_requires=[
    'beautifulsoup4==4.4.0',
    'html5lib==0.999999999'
  ],
)
