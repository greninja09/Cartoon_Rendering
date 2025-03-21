import cv2
import numpy as np

def cartoonize_image(image_path, out_path):
    # 이미지 로드
    img = cv2.imread(image_path)
    height, width = img.shape[:2]
    img = cv2.resize(img, (width, height))
    
    # 그레이스케일 변환
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 가우시안 블러 적용
    gray = cv2.medianBlur(gray, 5)
    
    # 엣지 검출 (Adaptive Thresholding)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                  cv2.THRESH_BINARY, 9, 9)
    
    # 색상 단순화 (Bilateral Filter)
    color = cv2.bilateralFilter(img, d=9, sigmaColor=200, sigmaSpace=200)
    
    # 엣지와 색상을 결합하여 만화 효과 적용
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    
    # 결과 저장
    cv2.imwrite(out_path, cartoon)

    # 결과 출력
    file_name = image_path.split('/')[-1]
    cv2.imshow(f"Cartoonized_{file_name}", cartoon)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 이미지 경로 지정 후 실행
for i in range(0, 14):
    cartoonize_image(f"./data/sample/sample{i}.jpg", f"./data/output/output{i}.jpg")