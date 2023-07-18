import pytesseract
from PIL import Image
from PIL import ImageGrab

class ScreenCaptureOCR:
    def __init__(self):
        self.center_x = 938
        self.center_y = 605
        self.width = 330
        self.height = 50
    
    def capture_and_ocr(self):
        # 计算截图区域的左上角和右下角坐标
        left = self.center_x - self.width // 2
        top = self.center_y - self.height // 2
        right = self.center_x + self.width // 2
        bottom = self.center_y + self.height // 2

        # 截取屏幕指定区域的截图
        im = ImageGrab.grab(bbox=(left, top, right, bottom))

        # 保存截图为PNG格式的图片文件
        im.save("screenshot.png")

        # 使用Tesseract OCR识别截图中的文本
        text = pytesseract.image_to_string(Image.open("screenshot.png"), lang="eng")

        return text

