"""
Document Processor Module
Handles text extraction from various document formats (PDF, DOCX, Images)
"""

import PyPDF2
from docx import Document
from PIL import Image
import io


def extract_text_from_pdf(file):
    """Extract text from PDF file"""
    try:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        return text.strip()
    except Exception as e:
        return f"Error extracting PDF: {str(e)}"


def extract_text_from_docx(file):
    """Extract text from DOCX file"""
    try:
        doc = Document(file)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text.strip()
    except Exception as e:
        return f"Error extracting DOCX: {str(e)}"


def extract_text_from_image(file):
    """Placeholder for image OCR - to be implemented with pytesseract"""
    try:
        image = Image.open(file)
        # OCR functionality can be added later with pytesseract
        return "Image OCR not yet implemented. Please upload PDF or DOCX files for now."
    except Exception as e:
        return f"Error processing image: {str(e)}"


def process_document(uploaded_file):
    """
    Main function to process any uploaded document
    Returns extracted text or error message
    """
    file_type = uploaded_file.type.lower()
    
    if 'pdf' in file_type:
        return extract_text_from_pdf(uploaded_file)
    elif 'word' in file_type or 'document' in file_type or uploaded_file.name.endswith('.docx'):
        return extract_text_from_docx(uploaded_file)
    elif 'image' in file_type or uploaded_file.name.lower().endswith(('.png', '.jpg', '.jpeg')):
        return extract_text_from_image(uploaded_file)
    else:
        return f"Unsupported file type: {file_type}"


def get_file_info(uploaded_file):
    """Get basic information about uploaded file"""
    return {
        'name': uploaded_file.name,
        'size_kb': uploaded_file.size / 1024,
        'type': uploaded_file.type
    }
