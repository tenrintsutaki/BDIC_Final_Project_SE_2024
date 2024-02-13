from paddleocr import PaddleOCR



ocr = PaddleOCR(lang = 'en')

def start_ocr():
    img_path = "img.png"
    result = ocr.ocr(img_path)
    output = ""
    for res in result:
        for r in res:
            output += r[1][0]
    return output
