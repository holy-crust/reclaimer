#!/usr/bin/env python
from os.path import dirname, join
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

curr_dir = dirname(__file__)

import reclaimer

try:
    try:
        long_desc = open(join(curr_dir, "readme.rst")).read()
    except Exception:
        long_desc = "Since PyPI refuses to let me upload due to my readme being Markdown, I wont be using a readme."
        #long_desc = open(join(curr_dir, "readme.md")).read()
except Exception:
    long_desc = 'Could not read long description from readme.'


setup(
    name='reclaimer',
    description='A libray of SupyrStruct structures and objects for \
games built with the Blam engine',
    long_description=long_desc,
    version='%s.%s.%s' % reclaimer.__version__,
    url='https://bitbucket.org/Moses_of_Egypt/reclaimer',
    author='Devin Bobadilla',
    author_email='MosesBobadilla@gmail.com',
    license='MIT',
    packages=[
        'reclaimer',
        'reclaimer.animation',
        'reclaimer.bitmaps',
        'reclaimer.h2',
        'reclaimer.h2.defs',
        'reclaimer.h2.defs.objs',
        'reclaimer.h3',
        'reclaimer.h3.defs',
        'reclaimer.h3.defs.objs',
        'reclaimer.halo_script',
        'reclaimer.hek',
        'reclaimer.hek.defs',
        'reclaimer.hek.defs.objs',
        'reclaimer.meta',
        'reclaimer.meta.gen3_resources',
        'reclaimer.meta.objs',
        'reclaimer.meta.wrappers',
        'reclaimer.model',
        'reclaimer.misc',
        'reclaimer.misc.defs',
        'reclaimer.misc.defs.objs',
        'reclaimer.os_hek',
        'reclaimer.os_hek.defs',
        'reclaimer.os_hek.defs.objs',
        'reclaimer.os_v3_hek',
        'reclaimer.os_v3_hek.defs',
        'reclaimer.os_v4_hek',
        'reclaimer.os_v4_hek.defs',
        'reclaimer.physics',
        'reclaimer.sounds',
        'reclaimer.shadowrun_prototype',
        'reclaimer.shadowrun_prototype.defs',
        'reclaimer.strings',
        'reclaimer.stubbs',
        'reclaimer.stubbs.defs',
        'reclaimer.stubbs.defs.objs',
        'reclaimer.util',
        ],
    package_data={
        '': ['*.txt', '*.md', '*.rst',
             '**/p8_palette_halo',   '**/p8_palette_halo_diff_map',
             '**/p8_palette_stubbs', '**/p8_palette_stubbs_diff_map'],
        },
    platforms=["POSIX", "Windows"],
    keywords="reclaimer, halo",
    # arbytmap can be removed from the dependencies if you cannot install
    # it for some reason, though it will prevent certain things from working.
    install_requires=['supyr_struct', 'binilla', 'arbytmap'],
    requires=['supyr_struct', 'binilla', 'arbytmap'],
    provides=['reclaimer'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        ],
    zip_safe=False,
    )
