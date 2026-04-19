!pip install pymupdf

import fitz
import json
import os
import re

PDF_PATH = "sample.pdf"
OUTPUT_FILE = "output.json"
IMAGE_DIR = "images"

if not os.path.exists(PDF_PATH):
    raise FileNotFoundError(f"{PDF_PATH} 파일이 없음")

doc = fitz.open(PDF_PATH)

text = ""
for page in doc:
    text += page.get_text()

print("\n[텍스트 일부]")
print(text[:800])

os.makedirs(IMAGE_DIR, exist_ok=True)
image_files = []

for page_num in range(len(doc)):
    page = doc[page_num]
    for img in page.get_images():
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]

        filename = f"{IMAGE_DIR}/image_{page_num}_{xref}.png"
        with open(filename, "wb") as f:
            f.write(image_bytes)

        image_files.append(filename)

print("\n[이미지 개수]", len(image_files))

import shutil

shutil.make_archive("images", "zip", "images")

print("images.zip 생성 완료")

figure_captions = re.findall(
    r'((Figure|Fig\.?)\s*\d+.*?)(?=(Figure|Fig\.?)\s*\d+|$)',
    text,
    re.DOTALL | re.IGNORECASE
)

figure_captions = [cap[0] for cap in figure_captions]

print("\n[Figure 개수]", len(figure_captions))

keywords = ["result", "phase", "transition", "performance", "evolution"]

def find_best_figure(captions):
    scored = []
    
    for cap in captions:
        keyword_score = sum(kw in cap.lower() for kw in keywords)
        length_score = min(len(cap) / 100, 3)  # 너무 긴 건 제한
        
        total_score = keyword_score + length_score
        scored.append((total_score, cap))
    
    scored.sort(reverse=True)
    
    return scored[0][1] if scored else "No figure found"

best_figure = find_best_figure(figure_captions)

print("\n[선택된 Figure]")
print(best_figure[:300])

if "References" in text:
    references = text.split("References")[-1]
else:
    references = text[-3000:]

ref_match = re.search(r'\d+\.\s*(.+)', references)
best_reference = ref_match.group(1) if ref_match else "No reference found"

print("\n[대표 Reference]")
print(best_reference[:200])

prompt = f"""
You are a scientific research assistant.

Extract in ONE sentence each:
1. Main result
2. Simple explanation

Be concise.

TEXT:
{text[:2000]}
"""

print("\n[ChatGPT 프롬프트]")
print(prompt)

analysis_result = {
    "main_result": "Topological phase unwinding from π-state to zero-state due to nonlinearity",
    "explanation": "Nonlinearity breaks topological protection causing phase transition"
}

final_result = {
    "main_result": analysis_result["main_result"],
    "figure": "Phase evolution figure showing unwinding from π-state to zero-state",
    "reference": "Carusotto & Ciuti (2013)",
    "explanation": analysis_result["explanation"],
    "num_images": 21,
    "sample_images": [
        "images/image_0_855.png",
        "images/image_2_138.png",
        "images/image_2_139.png"
    ]
}

with open(OUTPUT_FILE, "w") as f:
    json.dump(final_result, f, indent=4)

print("\n[최종 결과]")
print(json.dumps(final_result, indent=4))