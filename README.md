# pdf2tiff
## Create individual TIFF files from PDF files

### Requirements
* [Homebrew](https://brew.sh/ "Homebrew")
* [Python 3](https://docs.brew.sh/Homebrew-and-Python)
* [pdf2image](https://pypi.org/project/pdf2image/)
* [Poppler](https://formulae.brew.sh/formula/poppler)

------------

### Troubleshooting
###```raise Error("Destination path '%s' already exists" % real_dst)</br> shutil.Error: Destination path './TIFFs/file-name.tif' already existsshutil.Error: Destination path './TIFFs/image.tif' already exists``` : 
* Reason: Duplicate image file present in the TIFF output directory.
* Solutions:
	1. Remove duplicates from output directory and rerun script....OR
	2. Remove PDF from source and rerun script.
