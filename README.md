# ourcityindata
Github Repository, to have a information 

## Setting up the virtual environment
To make sure we use the same packages, you should create a virtual environment. Open a terminal, go to the root directory of this repository (OURCITYINDATA) and run

```
python -m venv venv
```

Activate the virtual environment in the terminal with (for Windows)
```
venv/Scripts/Activate.ps1
```
For other operating systems, you can find the commands [here](https://docs.python.org/3/library/venv.html).

Then you can install the required packages with:
```
pip install -r requirements.txt
```

Now you should be able to run the code in this repository.

## Running the streamlit app
First make sure that you have activated the virtual environment and have installed all the required packages (see above).

Then in the rootfolder (ourcityindata), run the following command:
```
streamlit run src/Interactive_bike_parking.py
```

This should open a browser window with the map of the analysis, and a selection box that lets you visualise different types of data.