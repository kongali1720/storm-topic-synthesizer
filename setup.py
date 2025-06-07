from setuptools import setup, find_packages

setup(
    name='storm-topic-synthesizer',
    version='0.1.0',
    author='kongali1720',
    author_email='your-email@example.com',
    description='STORM: Synthesis of Topic Outlines through Retrieval Methods using GPT and LangChain',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/kongali1720/storm-topic-synthesizer',
    packages=find_packages(),
    install_requires=[
        'openai>=0.27.0',
        'langchain>=0.0.0',  # sesuaikan versi yang dipakai
        # tambahkan requirement lain jika ada
    ],
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'storm=storm.cli:main',  # misal ada main() di storm/cli.py
        ],
    },
)
