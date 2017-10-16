# Pylogin

``` DISCLAIMER: This script was made for educational purposes only. ```
``` Don't use this for anything illegal, don't be an a hole ```

The purpose of this script is to extract confidential data from google chrome's sqlite3 db. The logins table contains the columns; origin_url, username_value and password_vale as seen visually in this image.

![alt text](https://i.gyazo.com/9dbd2e79a778383a5419a5781d08000f.png)

It then writes the output to a file called "Chromepass.txt" and calls the sendmail.py script

The sendmail script connects to an smpt server and uses the MIME modules(Multipart, Base and Text) to creates a complete new message structure with different objects from the file. The sendmail script was written in part by crossreferencing Python Documentation, Stack Overflow and general reseaching so the MIME module might not be entirely necessary

![alt text](https://i.gyazo.com/60fa5127d3950a543a4ea71cd8fcfc0a.png)
