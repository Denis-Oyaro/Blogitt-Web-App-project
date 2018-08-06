from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()
    
setup(
      name='blogitt', 
      version='1.0.0', 
      author='Denis Oyaro',
      author_email='oyaroden@gmail.com',
      description='A Blogging Web App',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/Denis-Oyaro/Blog-App-project',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
            'flask',
      ],
      classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)