from setuptools import setup, find_packages

setup(
    name='pdftools',
    version='1.0.8',
    description='PDFTools, a basic library for PDF softwares',
    author='Scihacker',
    author_email='sjtuzlp@gmail.com',
    url='https://github.com/PDFSoftware/PDFTools',
    packages=find_packages(),
    install_requires=[
        "pytest",
        "PyMuPDF",
        "svgwrite",
        "pyautogui",
        "keyboard",
        "pydrive",
        "pdfplumber",
        "pywin32",
        "google-auth",
        "google-auth-oauthlib",
        "google-auth-httplib2",
        "google-api-python-client"
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
