from setuptools import setup

exec(open('merge_pdf/version.py').read())

setup(
    name='merge_pdf',
    version=__version__,
    description='Merge PDFs offline for free',
    author='Kyllian Asselin de Beauville',
    author_email='kyllianasselindebeauville@gmail.com',
    url='https://github.com/kyllianasselindebeauville/merge-pdf',
    packages=['merge_pdf'],
    license='MIT',
    install_requires=[
        'PyPDF2>=2.11.0',
    ],
    entry_points={
        'console_scripts': [
            'merge-pdf = merge_pdf.__main__:main',
        ],
    },
    python_requires='>=3.7',
)
