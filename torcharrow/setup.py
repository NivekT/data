from setuptools import setup

setup(
    name='torcharrow',
    version='0.2.0',    
    description='Panda inspired, Arrow compatble Dataframes for PyTorch',
    url='https://github.com/...',
    author='Facebook',
    author_email='...@fb.com',
    license='BSD 2-clause',
    packages=['torcharrow'],
    install_requires=['arrow',
                      'numpy',
                      'pandas'   ,
                      'typing'

                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3.5',
    ],
)