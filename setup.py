from setuptools import setup, find_packages

setup(
	name="pyautest",
	version="0.0.1",
	description="golden file test utility",
	url="https://github.com/higumachan/pyautest",
	package_dir={'': 'src'},
	packages=find_packages(),
	entry_points={"pytest11": ["name_of_plugin = pyautest.pytest_integration.plugin"]},
	classifiers=["Framework :: Pytest"],
)
