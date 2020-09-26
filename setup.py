import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='banes-ramomar',
    version='1.0.0',
    author='Eduardo Garza',
    author_email='hola@ramomar.dev',
    description='Scrape Banorte transaction emails.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ramomar/banes',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.7',
    install_requires=[
        'beautifulsoup4'
    ]
)
