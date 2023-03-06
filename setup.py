from setuptools import setup, find_packages

setup(
    name='cls',
    packages=find_packages(),
    version='1.0.0',
    description='Continuous line structure library for Python.',
    author='Samuel Silverman',
    license='',
    author_email='sssilver@bu.edu',
    url='https://github.com/samsilverman/cls',
    keywords=[],
    python_requires='>=3.6',
    classifiers=[],
    install_requires=[
        'bentley-ottmann==7.3.0',
        'mapbox-earcut==1.0.0',
        'matplotlib>=3.5.1',
        'numpy>=1.21.5',
        'numpy-stl>=2.17.1',
        'pandas>=1.4.1',
        'plotly>=5.13.0',
        'scipy>=1.7.3',
    ],
    tests_require=[
        'pytest',
    ],
)
