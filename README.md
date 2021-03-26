# pdf2tiff
## Create individual TIFF files from PDF files

### Requirements
* [Homebrew](https://brew.sh/ "Homebrew")
* [Python 3](https://docs.brew.sh/Homebrew-and-Python)
* [pdf2image](https://pypi.org/project/pdf2image/)
* [Poppler](https://formulae.brew.sh/formula/poppler)

### Troubleshooting
1. ```shutil.Error: Destination path './TIFFs/image.tif' already exists``` : Duplicate image file present in the TIFF output directory. Remove image from output directory or remove PDF from source.
