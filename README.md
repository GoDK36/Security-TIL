# Security-TIL: PE 파일 분석 및 악성코드 탐지 실습

## 프로젝트 소개

이 프로젝트는 PE(Portable Executable) 파일 구조 분석, 악성코드 탐지 모델 실습, 그리고 탐지 우회 기법 실험을 목적으로 합니다. 머신러닝 기반 탐지기의 한계와 우회 방법을 실습하며, 보안 연구 및 악성코드 분석에 대한 이해를 높이는 데 중점을 둡니다.

## 주요 기능

- PE 파일의 다양한 헤더 및 섹션 정보 추출
- 엔트로피, 섹션 구조 등 통계적 특징 기반 악성코드 탐지
- RandomForestClassifier를 활용한 악성코드 분류
- 엔트로피, 헤더, 섹션 이름 등 조작을 통한 탐지 우회 실험
- 정상 파일이 없는 환경에서의 대안적 실험 방법 제공

## 폴더 구조 예시

```
Security-TIL/
├── date_til/
│   ├── adverserial.ipynb
│   ├── 0517-TIL.md
│   └── ...
├── dangerous-ai-main/
│   └── 3장/
│       └── data/
│           ├── malware.exe
│           ├── normal.exe
│           ├── extract.py
│           ├── rf_model.joblib
│           └── ...
└── README.md
```

## 사용법

1. **필수 라이브러리 설치**
   ```bash
   pip install pefile pandas scikit-learn joblib
   ```
2. **실습 노트북 실행**
   - `date_til/adverserial.ipynb`에서 실험 코드 실행
   - PE 파일 특징 추출, 엔트로피 조작, 악성코드 탐지 실험 등 단계별 실습
3. **모델 파일**
   - `rf_model.joblib` 등 사전 학습된 모델 파일 필요
4. **정상 파일이 없는 경우**
   - 통계적 평균값 또는 윈도우 기본 파일을 기준으로 실험 가능

## 실험 환경
- WSL2 기반 Ubuntu
- Python 3.11
- 주요 라이브러리: pefile, pandas, scikit-learn, joblib 등

## 참고 사항
- 본 프로젝트는 보안 연구 및 교육 목적입니다.
- 실제 악성코드 파일을 다루므로, 안전한 환경(가상머신, 샌드박스 등)에서 실습하세요.
- 엔트로피, 헤더, 섹션 조작 등은 실제 보안 환경에서 탐지 우회에 사용될 수 있으나, 악용을 금지합니다.

## License
MIT License 