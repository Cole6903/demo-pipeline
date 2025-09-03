from setuptools import setup, find_packages

setup(name="census-income",
      version ="0.0.3",
      author="cole",
      author_email="falafelinnit@gmail.com",
      packages=find_packages(),
      install_requires=["pandas","numpy","flask"]
)