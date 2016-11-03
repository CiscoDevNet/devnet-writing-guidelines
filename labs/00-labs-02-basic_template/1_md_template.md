# 1.md Template

## Creating Learing Labs with Markdown (Title of the Lab)

In this Lab, we will learn how to use markdown to create Learning Labs. (Brief summary of what will be covered in the lab)


## Objective ##

Completion Time: 45 minutes

* First Objective
* Second Objective


## Prerequisites

**Background**
* Bulleted list which should summarize required knowledge to pass this lab.

**Tool 1**
* Indicate the tool that is required for this lab and instructions on how to obtain it.

**Tool 2**
* Indicate the tool that is required for this lab and instructions on how to obtain it.


## Step 1. Learn Markdown Syntax

### Checking Your Python Version

In this sentence we will provide a detailed description what you will do/learn in this step. We will use different markdown syntax to make our text more interesting to read and learn.

> Note: This is a note.


1. First we will show you how to add pictures into the text.

![](./images/cisco_logo.jpg "If you hover over the picture you will see this text")

2. To **bold** a text we will use two asterisk in front and at the end of the text and to write in *italics*  we will use only one.

3. To write an `inline code` we will use back-ticks around it.

4. A block code should be enclosed between three back-ticks. To highlight syntax, provide language at the end of the first three back-ticks.
	```python
	text = "I am learning Markdown"
	print(text)
	```
5. To create hyperlink we will use square brackets to capture the front-end text and parenthesis for the actual URL. [I am a front-end text click on me.](https://www.cisco.com)


At the end, we will provide a summary what was discussed in this lab step, and will introduce what will be covered in the next step



## Code for Above Text
```md
# Creating Learing Labs with Markdown (Title of the Lab)

In this Lab, we will learn how to use markdown to create Learning Labs. (Brief summary of what will be covered in the lab)


## Objective ##

Completion Time: 45 minutes

* First Objective
* Second Objective


## Prerequisites

**Background**
* Bulleted list which should summarize required knowledge to pass this lab.

**Tool 1**
* Indicate the tool that is required for this lab and instructions on how to obtain it.

**Tool 2**
* Indicate the tool that is required for this lab and instructions on how to obtain it.


## Step 1. Learn Markdown Syntax

### Checking Your Python Version

In this sentence we will provide a detailed description what you will do/learn in this step. We will use different markdown syntax to make our text more interesting to read and learn.

> Note: This is a note.


1. First we will show you how to add pictures into the text.

![](./images/cisco_logo.jpg "If you hover over the picture you will see this text")

2. To **bold** a text we will use two asterisk in front and at the end of the text and to write in *italics*  we will use only one.

3. To write an `inline code` we will use back-ticks around it.

4. A block code should be enclosed between three back-ticks. To highlight syntax, provide language at the end of the first three back-ticks.
	```python
	text = "I am Learning Markdown"
	print(text)
	```
5. To create hyperlink we will use square brackets to capture the front-end text and parenthesis for the actual URL.
	[I am a front-end text.](https://www.cisco.com)


At the end, we will provide a summary what was discussed in this lab step, and will introduce what will be covered in the next step
```

### Explanation

* `#` - Indicates a header and the size. Number of pound signs(`#`) affects the size of the text
* `*` - At the begging of a sentence, asterisk creates unordered (bulleted) list.
* `1.` - Number and a dot at the begging of a sentence creates numbered list.
* `**bold**` - Text enclosed in between two asterisks is bolded.
* `*italic` - Text enclosed in between one asterisk appears as italics.
* `![](PATH_TO_THE_IMAGE_FILE)` - Images are added using this markdown code.
* `[Click Here](https://www.cisco.com)` - Code for Hyperlink.
* `>` - At the begging of a sentence, greater sign creates a blockquote.
* `Inline Code` - Text surrounded with back-ticks creates inline code.
