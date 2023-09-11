from pathlib import Path
from setuptools import setup, find_packages


setup(
    name='gcs-shape',
    version='1.2.1',
    description='Generalized cylindrical shell library for Python.',
    long_description=Path('README.md').read_text(encoding='utf-8'),
    long_description_content_type='text/markdown',
    author='Kelsey L. Snapp et al.',
    maintainer='Samuel Silverman',
    maintainer_email='sssilver@bu.edu',
    url='https://github.com/bu-shapelab/gcs',
    download_url='https://pypi.python.org/pypi/gcs-shape',
    project_urls={
            'Bug Tracker': 'https://github.com/bu-shapelab/gcs/issues',
            'Documentation': 'https://gcs-shape.readthedocs.io/',
            'Source Code': 'https://github.com/bu-shapelab/gcs',
    },
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Multimedia :: Graphics :: 3D Modeling',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Typing :: Typed',
    ],
    python_requires='>=3.8',
    packages=find_packages(exclude=['tests*']),
    install_requires=[
        'bentley-ottmann==7.3.0',
        'mapbox-earcut>=1.0.0',
        'numpy>=1.21.5',
        'numpy-stl>=2.17.1',
        'pandas>=1.4.1',
        'scipy>=1.7.3',
    ],
    test_suite='pytest',
)
