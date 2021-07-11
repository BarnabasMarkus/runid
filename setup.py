
import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='runid',
    version='0.0.1',
    author='barnabas markus',
    author_email='barnabasmarkus@gmail.com',
    description='''
        runid is a simple utility, which allows basic run tracking.
        it is super handy if, for example, you want to know how many times 
        a particular script or jupyter notebook has been run.
    ''',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/BarnabasMarkus/runid',
    license='MIT',
    packages=['runid'],
    install_requires=['joblib']
)