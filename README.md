# PDF CLI

PDF CLI is a command-line tool for manipulating PDF documents. It allows you to merge multiple PDF files into one and split a PDF into multiple files based on specified page ranges.

## Features

- **Merge PDFs**: Combine multiple PDF files into a single document.
- **Split PDFs**: Divide a PDF into several smaller PDFs based on page ranges.

## Installation

To use PDF CLI, ensure you have Python 3.12 or higher installed. You can install the required dependencies using `pip`:

```bash
pip install pikepdf
```

Alternatively, you can use a tool like Poetry to manage dependencies as specified in the `pyproject.toml` file:

```bash
poetry install
```

## Usage

To create a `docs` directory and include processed PDF documents, you can follow these steps:

1. **Create the `docs` Directory:**

   Open your terminal and navigate to the root directory of your project. Then, execute the following command to create the `docs` directory:

   ```bash
   mkdir docs
   ```

2. **Update Your Scripts:**

   Ensure that the paths in your scripts (`join-page.py` and `split-page.py`) correctly point to the `docs` directory for both input and output PDF files. For example, the `output_pdf` in `join-page.py` should be:

   ```python
   output_pdf = 'docs/results.pdf'
   ```

   Similarly, in `split-page.py`, make sure the `filename` variable points to a PDF within the `docs` directory:

   ```python
   filename = "./docs/xxx.pdf"
   ```

3. **Place Processed PDF Documents:**

   After running your scripts, the output PDF files will be saved in the `docs` directory. This keeps your project organized and makes it easier to locate processed documents.

By following these steps, you ensure that all processed PDF files are stored in the `docs` directory, maintaining a clean and organized project structure. If you want to include sample PDFs or any initial files, you can manually place them in the `docs` directory as well.
### Merging PDFs

The `join-page.py` script merges multiple PDF files. You can specify the input PDF files and the output file path within the script:

```python
# List of PDF files to be merged
input_pdfs = ['0.pdf', '1.pdf', '2.pdf', '3.pdf', '4.pdf']

# Output file name
output_pdf = 'docs/xx/results.pdf'
```

Run the script using Python:

```bash
python join-page.py
```

### Splitting PDFs

The `split-page.py` script splits a PDF into multiple files. You can configure the page ranges for each split within the script:

```python
# a dictionary mapping PDF file to original PDF's page range
file2pages = {
    0: [0, 1], # Pages 0 to 1
    1: [2, 3], # Pages 2 to 3
}

# the target PDF document to split
filename = "./docs/xxx.pdf"
```

Run the script using Python:

```bash
python split-page.py
```


## TODO
- Add `main.py` to handle argument CLI

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements/Credits
- Utilizes the [pikepdf](https://pikepdf.readthedocs.io/) library for PDF manipulation.
