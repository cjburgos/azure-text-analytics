# Azure Text Analytics

Some Python scripts to leverage Azure's Cognitive Services to run sentiment and entity recognition analysis over a list of sample text/blurbs such as "tweets" or Google keywords search. The script connects to a deployed instance of Azure Cognitive Service utilizing user's credentials (i.e. API Keys), then refines and outputs results on an Excel file. 

Before running the application, you need to set up the environement:

1) Install Python 3 | 
   [Download Link](https://www.python.org/downloads/)

2) Install 'pipenv' by running the following command in Terminal
    ```
    pip install pipenv
    ```

3) Once 'pipenv' is installed, run the following command:
    ```
    pipenv install -r requirements.txt
    ```

4) Then run this other command:
    ```
    pipenv shell
    ```

Your terminal must show a similar pattern as: 
    ```
    (azure-text-analytics) bash-3.2$
    ```

The application is ready to go; Insert an updated file with the filename the same as the one included on the APP.YAML at CONFIG folder (input_filename). You can update these records, but make sure the input filename is the same. 

The application will take a couple minutes to run; Once is completed look for the file with name equals to the value of 'output_filename' on this application folder. 
