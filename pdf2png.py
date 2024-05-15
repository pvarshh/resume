from pdf2image import convert_from_path

def convert_pdf(pdf_path, save_dif, res = 800):
    pages = convert_from_path(pdf_path,res)

    name_with_extension = pdf_path.rsplit('/')[-1]
    name = name_with_extension.rsplit('.')[0]

    for idx, page in enumerate(pages):
        page.save(f'{save_dif}/{name}.png','PNG')

convert_pdf('/Users/parney2004/Desktop/resume/resume.pdf',
            '/Users/parney2004/Desktop/resume/')
