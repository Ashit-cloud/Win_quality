conda create -n wineq python=3.7 -y

activate env

conda activate wine_quality

Created a req file and install the requirements.txt

pip install -r requirements.txt

Download the data from

https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5?usp=sharing

git init



dvc init 

dvc add data_given_win/winequality.csv

git add . && git commit -m "first commit"

oneliner updates for readme



git remote add origin https://github.com/Ashit-cloud/Win_quality_dvc.git

git branch -M main

git push origin main 

or

git push -f origin main


tox command -

tox

for rebuilding -

tox -r 

pytest command

pytest -v

setup commands -

pip install -e . 

build your own package commands-

python setup.py sdist bdist_wheel
