import os
from setuptools import setup, find_packages

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# Package dependencies
install_requires = [
    "django>=3.2",
]

setup(
    name='django_env_robots',
    version=__import__('django_env_robots').__version__,
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='Control robots.txt files from envrionment variables.',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/cursive-works/django-env-robots',
    author='Patrick Smith',
    author_email='pat.smith@cursive.works',
    keywords=['WAGTAIL', 'JSON', 'STREAMFIELD', 'JSONEditor', 'WAGTAIL CMS'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development',
    ],
    install_requires=install_requires,
)