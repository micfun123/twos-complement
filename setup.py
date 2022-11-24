from setuptools import setup, find_packages
 
VERSION = '0.0.0'
DESCRIPTION = "converts binary to twos complements binary. "

setup(
    name='twos_complement',
    version=VERSION,
    author='Michael Parker',
    author_email='michaelrbparker@protonmail.com',
    url='https://github.com/micfun123/twos-complement',
    description=DESCRIPTION,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages()
)

# python3 setup.py bdist_wheel
# twine upload dist/*
# sudo rm -rf ./build ./dist ./*egg-info