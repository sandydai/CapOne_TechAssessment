# CapOne_TechAssessment
Submission for 2020 PEY Capital One Technical Assessment SWE

This code uses OOP and contains a class Language, holding attributes and methods pertaining the syntax of the language.
The LanguageList class has a mapping of languages to their syntax.
The main function counts and returns the required comment and line counts.

It is assumed that the majority of the files will be Java, python, C++ or Ruby scripts.
The LanguageList class provides the functionality to add more languages.

Exceptions are thrown when the file begins with "." or if the language is not recognized.

A boolean is stored indicating if a language as block comment syntax or not. E.g. python does not but often uses '''  ''' string literal. Future modifications can be made to better check what constitutes a block comment or not. The current assumption is that only using block syntax results in a block comment. 

Index.java is a test case file.
