# sascii

SASCII is a Python project that allows you to generate coloured ASCII text art using special characters. It provides a collection of ASCII art representations for uppercase letters and digits as well as support for spaces.

## Prerequisites
- Python 3.x installed on your machine

## Usage
1. Clone or download the SASCII project from the [GitHub repository](https://github.com/9xN/sascii).
2. Open a terminal or command prompt and navigate to the project directory.

### Generating ASCII Art
1. Run the `sascii.py` script using the following command:
   ```sh
   python3 sascii.py
   ```
2. You will be prompted to select which font you would like to use
3. You will then be prompted to enter text and or numbers for which you want to generate ASCII art (you can add spaces by using an underscore "_" charactor typing out spaces in your response will not work).
4. A list of all of the possible colour combinations will be printed out; type in the desired number and press enter.
5. You can now enter a prefix and suffic to add to each line in order to make it easier to implement into a pre-existing project 
(i.e 

`'Enter a prefix for each line: '` 

```
printf("
```
`'Enter a suffix for each line: '` 


```
");
```
).

6. The program will display the corresponding ASCII art representation for each character in the text with escape codes and your optional prefix && suffix.

## Contributing
If you would like to contribute to the SASCII project, you can fork the repository, make your changes, and submit a pull request. Contributions such as adding new ASCII art representations, improving the code, or enhancing the functionality are welcome.
