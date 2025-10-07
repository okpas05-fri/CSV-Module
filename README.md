 CSV Module 
 Overview
The csv module is a built-in Python module for reading and writing tabular data in CSV (Comma Separated Values) format. It provides classes for reading and writing CSV files, as well as functions for working with CSV data.

 Features
- Reading CSV files: The csv.reader class allows you to read CSV files and iterate over the rows.
- Writing CSV files: The csv.writer class allows you to write data to a CSV file.
- Customizable formatting: You can customize the formatting of the CSV data, such as the delimiter, quote character, and escape character.
- Support for various CSV dialects: The csv module supports various CSV dialects, including Excel, Unix, and more.

 Example Usage
Reading a CSV file:
Writing a CSV file:
Classes and Functions
- csv.reader(csvfile, dialect='excel', **fmtparams): Returns a reader object that iterates over the rows of the CSV file.
- csv.writer(csvfile, dialect='excel', **fmtparams): Returns a writer object that writes data to the CSV file.
- csv.register_dialect(name[, dialect[, **fmtparams]]): Registers a new CSV dialect.
- csv.unregister_dialect(name): Unregisters a CSV dialect.

 Tips and Best Practices
- Always use the with statement to open CSV files to ensure they are properly closed.
- Use the newline='' parameter when opening CSV files in write mode to avoid issues with newline characters.
- Use the csv.QUOTE_NONE constant to specify that no quoting should be used in the CSV file.

