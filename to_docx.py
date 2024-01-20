from docx import Document
from htmldocx import HtmlToDocx

new_parser = HtmlToDocx()

input_path='Fanzhou_Liang.html'
output_path='Fanzhou_Liang.docx'

new_parser.parse_html_file(input_path, output_path)
