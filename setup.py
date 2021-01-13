from setuptools import setup, find_packages

setup(name='coloredtext',
      version='1.0',
      url = 'https://github.com/meet86/colored-helloworld',
      author = 'Meet Vasani',
      author_email = 'meet.vasani86@gmail.com',
      license= 'MIT',
      install_requires = ['colorama'],
      packages=find_packages(where='coloredtext'),
      zip_safe = False
)