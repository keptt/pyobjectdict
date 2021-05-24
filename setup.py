from distutils.core import setup

setup(
  name = 'objectdict',
  packages = ['objectdict'],
  version = '0.1.1',
  license='MIT',
  description = 'Package provides js-like dictionary object with a more convenient support of dot syntax plus a few additional methods',
  author = 'Serhii Orkivskyi',
  author_email = '2blesteve@gmail.com',
  url = 'https://github.com/keptt/objectdict',
  download_url = 'https://github.com/keptt/objectdict/archive/refs/tags/0.1.0.tar.gz',
  keywords = ['dict', 'objectdict', 'dot syntax', 'object', 'js-like'],
  install_requires=[],
  python_requires='>=3.6',
  classifiers=[
    'Development Status :: 3 - Alpha',      # "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of the package
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
