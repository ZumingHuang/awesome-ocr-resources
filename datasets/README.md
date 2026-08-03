<!-- Generated from data/*.yaml. Do not edit directly. -->

# Datasets

| Resource | Released | Tasks | Status | Description |
| --- | --- | --- | --- | --- |
| [SeeWye/Nondeterministic_Finite_Automata_OCR_v2](https://huggingface.co/datasets/SeeWye/Nondeterministic_Finite_Automata_OCR_v2) | 2026-08-02 | text-recognition | candidate | — |
| [BDRC/tibetan-ocr-diagnostic-benchmark](https://huggingface.co/datasets/BDRC/tibetan-ocr-diagnostic-benchmark) | 2026-08-02 | text-recognition | candidate | 
	
		
	
	
		Tibetan OCR Diagnostic Benchmark (OFAT)
	

A small, controlled diagnostic OCR benchmark of 300 synthetic Tibetan pecha-page images with exact, noise-free ground truth.
It is a scientific instrument for measuring how OCR character error rate (CER) responds to individual difficulty factors one at a time (OFAT) — not a coverage-maximizing training set.
Code & regeneration: https://github.com/buda-base/synthetic-ocr-benchmark-tools (diagnostic_benchmark/)

	
		
	
	
		What's inside… See the full description on the dataset page: https://huggingface.co/datasets/BDRC/tibetan-ocr-diagnostic-benchmark. |
| [mossbee/hippocamp_ocr](https://huggingface.co/datasets/mossbee/hippocamp_ocr) | 2026-08-01 | text-recognition | candidate | — |
| [mimimimi2002/license-detection-paligemma-ocr](https://huggingface.co/datasets/mimimimi2002/license-detection-paligemma-ocr) | 2026-08-01 | text-recognition | candidate | — |
| [vaishnavi0901/student-answer-ocr-v2](https://huggingface.co/datasets/vaishnavi0901/student-answer-ocr-v2) | 2026-07-31 | text-recognition | candidate | — |
| [vaishnavi0901/student-answer-ocr-notebook](https://huggingface.co/datasets/vaishnavi0901/student-answer-ocr-notebook) | 2026-07-31 | text-recognition | candidate | — |
| [vaishnavi0901/student-answer-ocr](https://huggingface.co/datasets/vaishnavi0901/student-answer-ocr) | 2026-07-30 | text-recognition | candidate | — |
| [mustaphaelkady/arabic-ocr-books](https://huggingface.co/datasets/mustaphaelkady/arabic-ocr-books) | 2026-07-30 | document-parsing, text-recognition | candidate | 
	
		
	
	
		Scanned Book Page Images
	

This dataset contains page images rendered from 9 PDF file(s).

	
		
	
	
		Dataset structure
	


One image per PDF page.
One subfolder per source PDF.
data/metadata.jsonl contains technical provenance for each page.


	
		
	
	
		Image settings
	


DPI: 300
Maximum width: 1600
Grayscale: True
Contrast factor: 1.4
JPEG quality: 95
White-margin cropping: True


	
		
	
	
		Intended use
	

OCR, document understanding, knowledge extraction, fine-tuning,
and… See the full description on the dataset page: https://huggingface.co/datasets/mustaphaelkady/arabic-ocr-books. |
| [egolqa/ocrv2](https://huggingface.co/datasets/egolqa/ocrv2) | 2026-07-30 | text-recognition | candidate | 
	
		
	
	
		OCR
	

The primary artifact is ocr.jsonl

	
		
	
	
		ocr.jsonl
	

Each line is one OCRFragment, a visible text region in one keyframe.
Common fields:

fragment_id: stable OCR observation identifier
video_id: source video identifier
time_span: [timestamp_ms, timestamp_ms] in source video time
text: recognized visible text
bbox: normalized text region with x_min, y_min, x_max, and y_max

There is no placeholder for frames without text and no fabricated confidence score. Join OCR with… See the full description on the dataset page: https://huggingface.co/datasets/egolqa/ocrv2. |
| [egolqa/ocr](https://huggingface.co/datasets/egolqa/ocr) | 2026-07-30 | text-recognition | candidate | 
	
		
	
	
		OCR
	

The primary artifact is ocr.jsonl còn artifact_metadata.jsonl records the input, model, prompt version, subset, and Git lineage

	
		
	
	
		ocr.jsonl
	

Each line is one OCRFragment, a visible text region in one keyframe.
Common fields:

fragment_id: OCR observation identifier
video_id: source video identifier
time_span: [timestamp_ms, timestamp_ms] in source video time
text: recognized visible text
bbox: normalized text region with x_min, y_min, x_max, and y_max

There is… See the full description on the dataset page: https://huggingface.co/datasets/egolqa/ocr. |
| [davanstrien/pr4598-header-ocr-test](https://huggingface.co/datasets/davanstrien/pr4598-header-ocr-test) | 2026-07-29 | text-recognition | candidate | 
	
		
	
	
		Document OCR using Unlimited-OCR
	

This dataset contains OCR results for davanstrien/bhl-impact-groundtruth
produced by baidu/Unlimited-OCR with vLLM.

	
		
	
	
		Processing Details
	


Source Dataset: davanstrien/bhl-impact-groundtruth
Model: baidu/Unlimited-OCR
Number of Samples: 10
Processing Time: 2.6 min
Processing Date: 2026-07-29 10:44 UTC
Output Column: markdown
Split: train


	
		
	
	
		Output
	

The column holds the model's raw layout-grounded markdown: text spans tagged… See the full description on the dataset page: https://huggingface.co/datasets/davanstrien/pr4598-header-ocr-test. |
| [Arko007/assistive-ocr-data-acquisition](https://huggingface.co/datasets/Arko007/assistive-ocr-data-acquisition) | 2026-07-29 | text-recognition | candidate | 
	
		
	
	
		Assistive OCR Benchmark Data
	

Multilingual OCR benchmark for visually impaired assistance — Indian medicine labels, packaged goods, and signage in Bengali, Hindi, and English.

	
		
	
	
		Dataset Summary
	


	
		
Property
Value


		
Total images
7,004 rows in manifest


Image sources
images/hf_medicines/, images/openfoodfacts/, images/synthetic/


Domains
medicine_packaging (6,588), packaged_goods (386), signage (30)


Languages
bn+en (5,337), hi+en (868), en (799)


Splits
dev… See the full description on the dataset page: https://huggingface.co/datasets/Arko007/assistive-ocr-data-acquisition. |
| [Wukong-OCR](https://wukong-dataset.github.io/wukong-dataset/) | unknown | text-recognition | needs-review | — |
| [TextVQA](https://textvqa.org/dataset/) | unknown | document-vqa | needs-review | — |
| [TextOCR](https://textvqa.org/textocr/dataset/) | unknown | text-recognition | needs-review | — |
| [SynthText](https://github.com/ankush-me/SynthText) | unknown | text-recognition | needs-review | — |
| [SynthDoG-ZH](https://github.com/clovaai/donut/tree/master/synthdog) | unknown | text-recognition | needs-review | — |
| [SynthDoG-EN](https://github.com/clovaai/donut/tree/master/synthdog) | unknown | text-recognition | needs-review | — |
| [ST-VQA](https://rrc.cvc.uab.es/?ch=11) | unknown | document-vqa | needs-review | — |
| [SROIE](https://rrc.cvc.uab.es/?ch=13) | unknown | text-recognition, key-information-extraction | needs-review | — |
| [ReCTs](https://rrc.cvc.uab.es/?ch=12) | unknown | text-recognition | needs-review | — |
| [RCTW-17](https://rctw.vlrlab.net/) | unknown | text-recognition | needs-review | — |
| [POIE](https://drive.google.com/file/d/1eEMNiVeLlD-b08XW_GfAGfPmmII-GDYs/view) | unknown | key-information-extraction | needs-review | — |
| [ParsynthOCR](https://huggingface.co/datasets/hezarai/parsynth-ocr-200k) | unknown | text-recognition | needs-review | — |
| [OCRVQA](https://ocr-vqa.github.io/) | unknown | document-vqa | needs-review | — |
| [NAF](https://github.com/herobd/NAF_dataset) | unknown | key-information-extraction | needs-review | — |
| [MTWI](https://www.modelscope.cn/datasets/iic/MTWI/) | unknown | text-recognition | needs-review | — |
| [LSVT](https://rrc.cvc.uab.es/?ch=16) | unknown | text-recognition | needs-review | — |
| [LaionCOCO-OCR](https://laion.ai/blog/laion-coco/) | unknown | text-recognition | needs-review | — |
| [InfoVQA](https://www.docvqa.org/datasets/infographicvqa) | unknown | document-vqa | needs-review | — |
| [IAM](https://fki.tic.heia-fr.ch/databases/iam-handwriting-database) | unknown | text-recognition | needs-review | — |
| [HME100K](https://ai.100tal.com/dataset) | unknown | formula-recognition | needs-review | — |
| [EST-VQA](https://github.com/xinke-wang/EST-VQA/blob/main/README.md) | unknown | document-vqa | needs-review | — |
| [EATEN](https://github.com/beacandler/EATEN) | unknown | key-information-extraction | needs-review | — |
| [CTW](https://ctwdataset.github.io/) | unknown | text-recognition | needs-review | — |
| [COCO-Text](https://vision.cornell.edu/se3/coco-text-2/) | unknown | text-recognition | needs-review | — |
| [Chinese-OCR](https://huggingface.co/datasets/longmaodata/Chinese-OCR) | unknown | text-recognition | needs-review | — |
| [CASIA](https://dataloaderx.github.io/datasetsome/casia/CASIA%E6%89%8B%E5%86%99%E6%B1%89%E5%AD%97%E7%AE%80%E4%BB%8B.html) | unknown | text-recognition | needs-review | — |
| [ArT](https://rrc.cvc.uab.es/?ch=14) | unknown | text-recognition | needs-review | — |
