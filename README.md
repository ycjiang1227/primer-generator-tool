# PCR Primer Generator
### Video Demo: https://youtu.be/OLTiX6ELdjk
### Link to website: http://ycjiang1227.eu.pythonanywhere.com/
### Introduction
As a Biochemistry student, I was struck by inspiration while in a lab class where we were designing primers for PCR.

Testing each primer manually - especially calculating the Tm - was incredibly tedious. I realised that it was almost comically simple to write up a Python code that would reduce my work time dramatically. It was nothing more than a command-line application, but momentarily made my life that much easier.

When thinking of possible ideas for the CS50x final project, this old project came to mind. It had an uncomplicated backbones rooted in simple logic, and I could make it more user friendly by implementing it as a website via Flask.

### PCR

To understand the project, we need some basic knowledge on PCR.

Thanks to the COVID-19 pandemic, PCR has now become a household name. Standing for Polymerase Chain Reaction, PCR is a fairly simple biochemical reaction that amplifies DNA samples. To do that, we need primers: short DNA samples of 18-30 nucleotides (DNA bases) long that match up to your DNA sample. They're needed to kickstart the reaction, and then the biochemist will add in an enzyme that makes numerous copies of the DNA with the help of the primers. Two primers are needed for each PCR reaction, matching to the two strands of DNA.

Click here for a [video](https://www.youtube.com/watch?v=iQsu3Kz9NYo) detailing how PCR works exactly.

The trouble lies in that for every DNA sequence, there are many possible primers, and of course many possible primer pairs. We also have several criteria that primers should ideally meet, to make the PCR reaction run smoothly. These criteria are:
* a GC clamp
  * The primer ending with a G or C nucleotide (remember that DNA is made of A, G, C and T nucleotides)
* GC content between 40% and 60%
  * Too high and the PCR reaction is no longer specific, too low and the PCR reaction is no longer efficient
* A suitable Tm
  * Tm is the melting temperature, or the temperature at which 50% of DNA strands become denatured
  * Ideally between 55&#8451; and 65&#8451;
* Matching Tm
  * Both primers are added at the same time, so their Tms should be within about 5&#8451; of each other

### The Project
The first thing you see when clicking the link is a basic starting page with a form. Three field are required: the DNA sequence itself, and the minimum and maximum Tm of the reaction.

After submitting, lists of all possible forward and reverse primers betweeen 18 and 30 nucleotides long are generated. All possible pairs are then generated, and each pair is scored. The scoring system is found within the [/why page](http://ycjiang1227.eu.pythonanywhere.com/why) of the website.

Pairs with the highest scores are presented on the results page in a table.

### What's next?
The app currently only generates primers for the most basic PCR reactions. There are many variants of PCR out there that require more primer considerations - that would make the project more applicable to real life scenarios.

Data validation - checking the length of DNA, appropriate Tms. An alert for unusually low or high Tms could be implemented.

Support for FASTA format (common format for DNA sequences) or file uploads.

Downloading primer pairs in FASTA format into a text file.