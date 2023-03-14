#This is a tool depends on pdf2docx pdf to docx 
#Install the pdf2docx; pip install pdf2docx
#引入Conver类
import os
from pdf2docx import Converter
import time
#输入pdf文件路径和待生成的docx文件保存路径，使用相对路径
pdf_file = input('请输入源文件路径:')
docx_file = input('请输入保存路径:')

#开始转换
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()
#防止闪退
time.sleep(10)
