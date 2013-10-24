from setuptools import setup

setup(
    name='django-jquery-lightbox',
    version='2.6',
    url='https://github.com/mikebryant/django-jquery-lightbox',
    description='Django package for Lightbox: a small javascript library used to overlay images on top of the current page.',
    author='Lokesh Dhakar',
    maintainer='Mike Bryant',
    maintainer_email='mike@mikebryant.me.uk',
    license='Creative Commons Attribution 2.5 License',
    keywords=['django', 'jquery', 'lightbox', 'staticfiles', 'overlay', 'image'],
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    packages=['jquery_lightbox'],
    package_data={'jquery_lightbox': ['static/js/*.js', 'static/css/*.css', 'static/img/*']},
    install_requires=['django-jquery >= 1.9',],
)
