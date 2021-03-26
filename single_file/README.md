# pdf2tiff
## Create individual TIFF files from a single PDF file

### Requirements
* [Homebrew](https://brew.sh/ "Homebrew")
* [Python 3](https://docs.brew.sh/Homebrew-and-Python)
* [pdf2image](https://pypi.org/project/pdf2image/)
* [Poppler](https://formulae.brew.sh/formula/poppler)

### Troubleshooting
1. ```shutil.Error: Destination path './TIFFs/image.tif' already exists``` : 
* Reason: Duplicate image file present in the TIFF output directory.
* Solutions:
	1. Remove duplicates from output directory and rerun script....OR
	2. Remove PDF from source and rerun script.
