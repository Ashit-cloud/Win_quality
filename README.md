conda create -n wineq python=3.7 -y
activate env
conda activate wine_quality

Created a req file and install the requirements.txt
pip install -r requirements.txt

Download the data from
https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5?usp=sharing

'''bash
git init

dvc init 
dvc add data_given_win/winequality.csv
git add .
git commit -m "first commit"
oneliner updates for readme


git add . && git commit -m "update Readme.md"
git remote add origin https://github.com/Ashit-cloud/Win_quality_dvc.git
git branch -M main
git push origin main
