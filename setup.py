# setup.py

from setuptools import setup, find_packages

setup(
    name='my_stats_toolkit',
    version='0.1.0',
    author='Lucas', # 請換成您的名字
    author_email='Lucassullivan0219@gmail.com', # 請換成您的 Email
    description='一個用於練習高階開發者架構的通用統計工具包',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)