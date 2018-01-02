"""One-line summary of your script.

Multi-line description of your script (make sure you include the copyright and
license notice).

Script Dependencies:
    requests

Depencency Installation:
    $ pip install requests

Copyright (c) 2017, Cisco Systems, Inc. All rights reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


# Standard library imports
import json

# Third-party imports
import requests

# Local application/library-specific imports


# Define the API server root as a CONSTANT
URL = 'http://server:8081/api/v0/host'

# Define a variable to store the response to the request
response = requests.get(URL)

# Verify that the request was successful
response.raise_for_status()

# Parse the JSON data
json_data = response.json()

# Print the JSON data using a "pretty print" format
print(json.dumps(json_data, indent=4))
