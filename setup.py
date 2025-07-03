import setuptools

with open('README.md','r',encoding='utf-8') as ff:
    long_description = ff.read()

__version__='0.0.0'


REPO_NAME='RenalTumor'
AUTHOR_USER_NAME='kanishka-rani-2005'
SRC_REPO='KidneyDiseaseClassifier'
AUTHOR_EMAIL='kanishka22043@gmail.com'

setuptools.setup(
    name=REPO_NAME,
    version=__version__, 
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='This is a Kidney Disease Classification Project',
    long_description=long_description,
    long_description_content_type='text/markdown',
    project_urls={
        'Bug Tracker':f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issue"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where='src')
)
