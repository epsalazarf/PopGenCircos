# Circos Recipes

*By Pavel Salazar-Fernandez (epsalazarf@gmail.com)*

*Human Population and Evolutionary Genomics Lab | LANGEBIO*

[Project still in development]
## About
This document explains the basics about Circos, a program for creating circular infographics.

The first section explains the installation and basic usage of Circos. Most of the information is obtained from the Circos website (<http://circos.ca/>), which provides downloads and useful documentation for learning and fine-tuning the Circos package. 

The second section, **Recipes**, provides instructions and scripts for generating specific graphs. It is strongly encouraged that users contribute with more recipes to this folder.  

## What is Circos?
*Source: [Circos website](http://circos.ca/)*
Circos is a software package for visualizing data and information in a circular layout — ideal for exploring relationships between objects or positions. Originally designed for visualizing genomic data, it can create figures from data in any field. 

Circos is flexible and can be automated. You have fine control each element in the figure to tailor its focus points and detail to your audience. It is controlled by plain-text configuration files, which makes it easily incorporated into data acquisition, analysis and reporting pipelines (a data pipeline is a multi-step process in which data is analyzed by multiple and typically independent tools, each passing their output as the input to the next step). 

### Installing Circos
**Requirements**:
- Unix system (preferred, but can be installed on a Windows computer)
- Perl 5.8.x or newer

**Download**:
<http://circos.ca/software/download/>

**Installation guide**:
<http://circos.ca/software/installation/>

### Learning Circos
The Circos website has great tutorials for learning Circos. If you haven't used Circos before, the Quick Start tutorial is a nice introduction to the package and necessary for modifying these recipes. 

**Circos/Quick Start:**
<http://circos.ca/documentation/tutorials/quick_start/>

## Recipes
For more recipes, check the Circos website:
<http://circos.ca/documentation/tutorials/recipes/>

### Genomic SNP Density Map
This recipe generates an histogram within an ideogram representing the autosome. Bars quantify the number of SNP found within a range (default: 1Mbp), and gray section shows regions with no SNPs.


**Requirements**:
- BIM or MAP file from a PLINK dataset
- Python 3+ or better (Download at http://www.python.org/)
- `SNPCounter.py` (provided)
- `chr.hetero.highlights.txt`: list of heterochromatic regions in chromosomes.

Function:
Counts the number of SNPs per Mb from a BIM file and output a CSV

Usage:
- Copy the script file to desired location.
- Run the following command:

`python SNPCounter.py [file.bim]`

"""