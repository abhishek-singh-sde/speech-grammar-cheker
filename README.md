# speech-grammar-cheker
A simple script to record narration/speech, convert it to text and analyze the text online via a website to display the grammatical errors made while speaking.

Make sure you have all the packages/library modules required. If not, open CMD and use pip install <name> to install the same... Should get downloaded in seconds... 

The default microphone should've the access.i.e adjust privacy settings to allow recording using python if required. 

If r.recognize_google(audio) isn't working, use r.recognize_sphinx(audio) 

Add the path of your chromedriver.exe file in webdriver.Chrome(options=options, executable_path=(r"<insert path here>")
