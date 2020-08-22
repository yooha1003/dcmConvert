from setuptools import setup, find_packages

setup(
    name='dcmConvert',
    version='0.1.0',
    url='https://github.com/yooha1003/dcmConvert',
    author='Uksu, Choi',
    author_email='qtwing@naver.com',
    description='Automatic DICOM converting script',
    packages=find_packages(),
    install_requires=['nibabel', 'glob', 'numpy', 'argparse', 'resource'],
)
