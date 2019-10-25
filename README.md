This project is an example of how to build a cli that parses logs.

The object which is called `blob` is called that way just because I could not find any better name, basically this object holds the needed logs, their name, and their additional info :)

The project is structured the next way:

- cli - holds the files for the cli interface of the tool
- rest - holds the files for the rest interface of the tool
- core - holds the core files of the tool, all the domain logic and service are in this folder.
  - emitters - holds the files that handle emitting the results of the parsers
  - model - holds the files that define the core concepts for the tool, as `blob` and different levels of `severity`
  - parsers - holds the files that handle parsing of the logs
  - readers - holds the files that handle reading the logs from different places, be it a file, or database
  - services - holds the files that handle the different use cases for the tool. it connects between the readers, parsers and emitters and constructs the basic work flow.


-------------------
example of using the tool:

```python cli --file C:\path\example.log --severity WARNING --no-duplicates```

This line will parse the file located at C:\path\example.log and will output the warning lines it finds without any duplications.

-------------------
This repository aims to showcase certain ideas, including how to organize a project and manage responsibilities, and it is not yet finished.
Intentionally there is a really low amount of usage of classes and interfaces, to make the showcase of those principles as easy as possible.

To further improve the repository:
- add interfaces for parsers, emitters and readers, meaning that the functions will be replaced with classes that fulfill there interfaces
- make the severity as a value object
- change the core code to work with the blob and severity objects.



