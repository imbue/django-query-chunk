import setuptools

name = 'django-query-chunk'
requirements = ['six', 'django>=2.0']

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name=name,
    version='0.0.1',
    author='imbue',
    author_email='liamboer@outlook.com',
    description='Part QuerySets into small chunks.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/imbue/django-query-chunk',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)