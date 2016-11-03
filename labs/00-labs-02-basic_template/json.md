# Template for JSON File

>**Note:** You may use [JSONLint](http://jsonlint.com/) to validate the format.

```json
{
  "labId": "varies-from-project-to-project",
  "title": "Title of the Lab",
  "slug": "Short description what will be covered in the lab",
  "time": 25,
  "byod": true,
  "files": [
    {"title": "name of the first markdown file"},
    {"title": "name of the second markdown file"},
    {"title": "name of the third markdown file"}
  ],
  "tags": [
    {"title": "Tag1"},
    {"title": "Tag2"},
    {"title": "Tag3"},
    {"title": "Tag4"}
  ],
  "related": [
     {
      "labId": "lab-id-of-the-related-lab",
      "title": "Title of the lab"
    },
     {
      "labId": "lab-id-of-the-related-lab",
      "title": "Title of the lab"
    },
     {
      "labId": "lab-id-of-the-related-lab",
      "title": "Title of the lab"
    }
  ],
  "authors": [
  	{"name": "Name Lastname", "email": "email@address.com"}
  ]
}
```