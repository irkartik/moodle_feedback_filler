# moodle_feedback_filler (<a href = "https://youtu.be/ZVkv3yzOseQ">Demo</a>)
We hate filling feedback forms, don't we? Relax, this script fills the moodle feedback form for you!

This script automates your task for filling the MSIT moodle feedback form

Any contributions from you guys are welcome. Just fork this repository, make changes in the code and create a pull request, I will merge the changes if it seems interesting. :)

Do star the repo if you think it worth it.

# Requirements (on your system)
1. Chrome/Chromium Browser (https://www.google.com/chrome/browser)
2. Chrome WebDriver (https://chromedriver.storage.googleapis.com/index.html?path=2.33/)
3. Python3 (https://www.python.org/downloads/)
4. Virtualenv (<code>$ pip3 install virtualenv</code>)
5. Selenium (<code>$ pip3 install selenium</code>)

# Steps to run in your local machine
1. Firstly, clone the repository using the git shell <br>
<code>$ git clone https://github.com/rajujha373/moodle_feedback_filler.git</code> 
2. Goto the base directory of the project <br>
<code>$ cd moodle_feedback_filler</code>  
3. Create a virtual environment and activate it.<br> 
<code> $ virtualenv venv </code><br>
<code> $ source venv/bin/activate </code>
4. Install the requirements for the project<br> 
<code> $ pip install -r requirements.txt </code>
6. Download the ChromeWebdriver and extract into the directory.
7. In the file "feedback.py" replace <br>
      "{GLOBAL PATH OF CHROMEDRIVER}" with the absolute path of the downloaded Chrome Webdriver<br>
      "{YOUR USERNAME HERE}": with your moodle username<br>
      "{YOUR PASSWORD HERE}" with your moodle password<br>
      "{YOUR LABCODE HERE}": with your lab code (lab_codes_A : IF YOU BELONG TO GROUP A, lab_codes_B : IF YOU BELONG TO GROUP B, lab_codes_C : IF YOU BELONG TO GROUP C)<br>
5. Run the script<br>
<code> $ python3 feedback.py</code>
6. Voila!

# to be noted

This script gives rating of 4 to each checkboxes (in the scale of 5, larger being better). 

