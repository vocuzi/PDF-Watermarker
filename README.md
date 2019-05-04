[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

# Automated Batch PDF watermarker
This program takes the pdfs in input folder and then watermark them with provided logo and website address and puts them in output folder.
This program watermark PDFs with Image and Text. 

## How to use: 
1) Clone the repository and make sure you have `PyPDF2` and `reportlab` installed. If not, install with 
```
pip install PyPDF2 reportlab`. 
```
2) Place your logo in `./bin` directory with name "logo.png". 
3) Put the PDFs that you wish to watermark in `./input` folder. If folder doesn't already exists, create it manually before running the script. 
4) Run the program with following command in the program directory:  
```
$ python watermarker.py 
```
4) BOOM👯, Watermaked PDFs are ready in `./output` directory. 



- Edited by <a href="https://github.com/vocuzi" target="_blank">@vocuzi</a>
- Forked from <a href="https://github.com/sNeeds/PDF-Watermarker" target="_blank">sNeeds/PDF-Watermarker</a>
