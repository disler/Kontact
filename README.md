# Kontact
A simple CRUD application demonstrating a relatively clean and intuitive design for building apps using vuejs and python.

# Quick View
Check out http://disler.pythonanywhere.com/#/ for a view of the site

# Improvements

## Major
* Database in currently in memory. It should be converted to an external Database (PostgreSql)
* All kontacts are loaded every time the root url '/' is hit. To scale - pagination should be added and the records should be cached
* All kontact object information is fetched on the root url '/'. This is greedy and only required information should be rendered.
* Ability to upload profile picture

## Minor
* Save button should be deactivated when no changes have been made
* Filtering should animate
* Ability to select backdrop color
* Clean up .gitignore (.vscode/, etc)
