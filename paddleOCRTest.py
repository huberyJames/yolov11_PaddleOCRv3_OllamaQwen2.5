from paddleocr import PaddleOCR
import os

BASE_MODEL_DIR = r"C:\\Users\\Administrator\\Desktop\\sh\\models"
PADDLEOCR_MODEL_DIR = os.path.join(BASE_MODEL_DIR, "paddleocr")

DET_MODEL_DIR = os.path.join(PADDLEOCR_MODEL_DIR, "ch_PP-OCRv4_det_infer")
REC_MODEL_DIR = os.path.join(PADDLEOCR_MODEL_DIR, "ch_PP-OCRv4_rec_infer")
CLS_MODEL_DIR = os.path.join(PADDLEOCR_MODEL_DIR, "ch_ppocr_mobile_v2.0_cls_infer")

ocr = PaddleOCR(
    det_model_dir=DET_MODEL_DIR,
    rec_model_dir=REC_MODEL_DIR,
    cls_model_dir=CLS_MODEL_DIR,
    use_angle_cls=True,
    lang='ch',
    use_gpu=False,
    show_log=True,
    # ===== 关键优化：针对数字+特殊字符 =====
    det_limit_side_len=1920,        # 提高分辨率
    det_db_thresh=0.15,             # 大幅降低检测阈值（关键！）
    det_db_box_thresh=0.25,         # 降低框选阈值
    det_db_unclip_ratio=2.2,        # 增大扩展比例，防止边缘截断
    det_db_score_mode="slow",       # 更精确的评分
    use_dilation=True,              # 膨胀填充
    drop_score=0.2,                 # 降低过滤阈值，保留低置信度结果
)

img_path = r'C:\\Users\\Administrator\\Desktop\\sh\\pic\\OCR2.png'
result = ocr.ocr(img_path, cls=True)

print("=" * 60)
print("PaddleOCR 识别结果：")
print("=" * 60)

if result and result[0]:
    for i, line in enumerate(result[0], 1):
        text = line[1][0]
        score = line[1][1]
        print(f"[{i}] 文字: {text:<30} 置信度: {score:.4f}")
else:
    print("未识别到文字")

print("=" * 60)
print(f"共识别到 {len(result[0]) if result and result[0] else 0} 行文字")
print("PaddleOCR 验证完成！")
