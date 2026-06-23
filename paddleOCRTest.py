from paddleocr import PaddleOCR
import os

# ========== 模型路径配置 ==========
BASE_MODEL_DIR = r"C:\\Users\\Administrator\\Desktop\\sh\\models"
PADDLEOCR_MODEL_DIR = os.path.join(BASE_MODEL_DIR, "paddleocr")

# PaddleOCR 各子模型路径（分别指定）
DET_MODEL_DIR = os.path.join(PADDLEOCR_MODEL_DIR, "ch_PP-OCRv4_det_infer")      # 检测模型
REC_MODEL_DIR = os.path.join(PADDLEOCR_MODEL_DIR, "ch_PP-OCRv4_rec_infer")      # 识别模型
CLS_MODEL_DIR = os.path.join(PADDLEOCR_MODEL_DIR, "ch_ppocr_mobile_v2.0_cls_infer")  # 分类模型

# ========== 初始化 OCR（使用自定义模型路径）==========
ocr = PaddleOCR(
    det_model_dir=DET_MODEL_DIR,      # 检测模型路径
    rec_model_dir=REC_MODEL_DIR,      # 识别模型路径
    cls_model_dir=CLS_MODEL_DIR,      # 分类模型路径
    use_angle_cls=True,               # 启用方向分类
    lang='ch',                        # 中文模型
    use_gpu=False,                    # CPU 运行
    show_log=True                     # 显示日志（方便调试）
)

# ========== 测试图片路径 ==========
img_path = r'C:\\Users\\Administrator\\Desktop\\sh\\pic\\OCR.png'

# 执行 OCR
result = ocr.ocr(img_path, cls=True)

print("=" * 50)
print("PaddleOCR 识别结果：")
print("=" * 50)

# 解析结果
if result and result[0]:
    for line in result[0]:
        box = line[0]        # 文字框坐标
        text = line[1][0]    # 识别文字
        score = line[1][1]   # 置信度
        print(f"文字: {text:<20} 置信度: {score:.4f}")
else:
    print("未识别到文字")

print("=" * 50)
print("PaddleOCR 验证完成！")