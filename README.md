# devnet-guidelines
Instructions and guidelines for DevNet lab creation and beyond

These instructional labs and templates should only be published to and accessed from the Staged environment.  They should not be published to production.


# Python Script

`script` folder contains a python script which sets up the directory structure for the user and copies necessary template files.

### How to use it

In terminal, run the script with `python3 start_here_for_LL.py`. The script will create necessary folders and will prompt to enter additional information. Obtained information will be used to populate some values in JSON file.

```
How would you like to name the root directory? 00-lab-01
What is the title of the lab? Learn How To Write a LL
Provide a short description for the lab. This lab is designed to teach content developers how to properly write LL
Approximately how long will it take to complete the lab? 35
Name the tag associated with this lab. LL
What is the name of the author of this lab? John Doe
What is author's email address? jd@abc.com

JSON file has been created, but it might need additional modification after the content is written.

The folder structure has been successfully created.
\---labs
    +---00-lab-01
    |   |   00-lab-01.json
    |   |   1.md
    |   |   2.md
    |   |   byod.html
    |   |
    |   \---assets
    |       \---images

```


# Recommended Tools

Check the [wiki](https://github.com/CiscoDevNet/devnet-guidelines/wiki/Tools-to-Write-Learning-Labs) section for recommend tools.
