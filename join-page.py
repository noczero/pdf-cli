from pikepdf import Pdf

def merge_pdfs(input_pdfs, output_pdf):
    # Create a new PDF for the output
    output = Pdf.new()

    # Iterate over each PDF file
    for pdf_path in input_pdfs:
        # Open the current PDF
        with Pdf.open(pdf_path) as pdf:
            # Append each page of the current PDF to the output PDF
            output.pages.extend(pdf.pages)

    # Save the combined PDF to the specified output file
    output.save(output_pdf)

# List of PDF files to be merged
directory = './docs/xx'

input_pdfs = ['0.pdf', '1.pdf', '2.pdf', '3.pdf', '4.pdf']

file_paths = [f"{directory}/{input_pdf}" for input_pdf in input_pdfs]

# Output file name
output_pdf = 'docs/xx/results.pdf'

# Merge the PDFs
merge_pdfs(file_paths, output_pdf)

print(f"Merged PDF saved as {output_pdf}")