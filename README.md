# Workflow of genomic data visualization using PyGenomeTrack

This notebook contains a procedure to prepare the sequencing data for visualization of the region plots. 
The workflow describes the tools to convert the files into the formats: BED6, BED12, BAM, and BIGWIG. Additionally, we formed the helper functions to create .ini files from scratch.

The [PyGenomeTrack](https://github.com/deeptools/pyGenomeTracks) aims to produce high-quality genome browser tracks.

The main steps:
* Installation of requirements.
* Prepare your GFF3 files.
* Convert GFF3 into BED6.
* Convert GFF3 into BED12.
* Sort your BED6/BED12 file
* Make BigWig file from BAM/SAM format.
* Prepare the .INI files - from scrach or by edition of the example file.
* PyGenomeTracks - make tracks file.
* PyGenomeTracks - make region plot

__HINT:__ Exclamation mark (!) at the beginning of line allows to use bash commands from jupyter notebook.

# Requirements:
* Python 2.7 or Python 3.x
* PyGenomeTrack
* samtools
* bedtools
* sortbed
* gff3togenepred
* genepredtobed
* numpy >= 1.8.0
* scipy >= 0.17.0
* py2bit >= 0.1.0
* pyBigWig >= 0.2.1
* pysam >= 0.8
* matplotlib >= 1.4.0
* deeptools

# Types of formats
* [GFF3](https://www.ensembl.org/info/website/upload/gff3.html) - General Feature Format Version 3
* [BED6/BED12](https://genome.ucsc.edu/FAQ/FAQformat.html#format1) - Browser Extensible Data
* The [BIGWIG](https://genome.ucsc.edu/goldenPath/help/bigWig.html) format is useful for dense, continuous data that will be displayed in the Genome Browser as a graph.
* The __INI__ file format is an informal standard for configuration files.
* [SAM](https://samtools.github.io/hts-specs/SAMv1.pdf) - Sequence Alignment Map
* [BAM](https://genome.ucsc.edu/goldenPath/help/bam.html) is the compressed binary version of the Sequence Alignment/Map (SAM) format, a compact and index-able representation of nucleotide sequence alignment.
* [genePred](http://genome.ucsc.edu/FAQ/FAQformat#format9) is a table format commonly used for gene prediction tracks in the Genome Browser.
