#Introduction
This project has for goal to provide a simple, fast, modulable tool to produce rule based machine learning in text processing task.


#Installation
setuptools install

#Usage
##Learning a new model

pyrbml learn --data <file of data> --labels <index of labels tabel in the data> --out <folder of modeling>

##Using a already existant model

pyrbml classify --text <text> --file <localisation of file>
