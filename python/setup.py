from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='polyreg',
      version='0.1',
      description='Polynomial Regression using pySpark',
      long_description=readme(),
      classifiers=[
        'License :: OSI Approved :: MIT License'
      ],
      keywords='pyspark polynomial cdsw',
      url='http://github.mtv.cloudera.com/mlop/polyreg/',
      author='Brad Barker',
      author_email='barker@cloudera.com',
      license='MIT',
      packages=['polyreg'],
      install_requires=[
          'pyspark',
          'scikit-learn',
          'numpy',
          'pandas'
      ],
      test_suite='nose.collector',
      include_package_data=True,
      zip_safe=False)
