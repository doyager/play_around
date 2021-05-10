

#to create virtual env and when you list on the current dir , you will see a folder with the name-of-env
python3 -m venv <name-of-env>
Eg : python3 -m venv venv
  
  
#to activate [i..e. start using that virtual env]

source venv/bin/activate


#To capture list of request libraries / requirements of the virtual env with all specific versions

pip freeze > requirements.txt

#install the dependenciesn , -t is option to specify the location and . is for current dir
pip install -r requirements.txt -t .


#deactivate virtual env
deactivate

#
