<!-- Generated from data/*.yaml. Do not edit directly. -->

# Datasets

| Resource | Released | Tasks | Status | Description |
| --- | --- | --- | --- | --- |
| [jpeglle/epstein-files-ocr-complete](https://huggingface.co/datasets/jpeglle/epstein-files-ocr-complete) | 2026-08-08 | text-recognition | candidate | 
	
		
	
	
		Epstein Files — Complete OCR Dataset
	


This is a comprehensive, structured publication of the Epstein Files OCR dataset, significantly expanding upon the earlier Datasets 1-8 release.


	
		
	
	
		Dataset Summary
	

This dataset contains page-level OCR output compiled from an extensive release of documents related to Jeffrey Epstein / the Epstein case.
Each row in this dataset represents one scanned PDF document from the original release using a proprietary automated OCR pipeline… See the full description on the dataset page: https://huggingface.co/datasets/jpeglle/epstein-files-ocr-complete. |
| [alphabot2/07-08-2026_OCR_Bimanual](https://huggingface.co/datasets/alphabot2/07-08-2026_OCR_Bimanual) | 2026-08-07 | text-recognition | candidate | This dataset was created using LeRobot.







	
		
	
	
		Dataset Structure
	

meta/info.json:
{
    "codebase_version": "v3.0",
    "robot_type": "aibot2",
    "total_episodes": 37,
    "total_frames": 17770,
    "total_tasks": 1,
    "chunks_size": 1000,
    "data_files_size_in_mb": 100,
    "video_files_size_in_mb": 200,
    "fps": 10,
    "splits": {
        "train": "0:37"
    },
    "data_path": "data/chunk-{chunk_index:03d}/file-{file_index:03d}.parquet",
    "video_path":… See the full description on the dataset page: https://huggingface.co/datasets/alphabot2/07-08-2026_OCR_Bimanual. |
| [boffire/adlis-pdfs-ocr-kab](https://huggingface.co/datasets/boffire/adlis-pdfs-ocr-kab) | 2026-08-06 | text-recognition | candidate | — |
| [PersianML/persian-ocr-benchmark](https://huggingface.co/datasets/PersianML/persian-ocr-benchmark) | 2026-08-05 | text-recognition | candidate | 
	
		
	
	
		Persian OCR Evaluation Dataset
	

This benchmark contains paired Persian document images and UTF-8 transcription
targets for OCR evaluation. Each JSONL row references one image under
bench_data/images/ and contains its transcription in the text field.

	
		
	
	
		Schema
	


image: image path relative to the repository
id: stable image identifier
page: page number, currently 1
type: evaluation item type, currently transcription
text: reference transcription
language: fa
checked:… See the full description on the dataset page: https://huggingface.co/datasets/PersianML/persian-ocr-benchmark. |
| [jswhitworth/ocr-demo-documents](https://huggingface.co/datasets/jswhitworth/ocr-demo-documents) | 2026-08-05 | text-recognition | candidate | 
	
		
	
	
		OCR Demo Documents — state court opinions
	

Public state appellate opinions parsed with
baidu/Unlimited-OCR, served on
vLLM. Each document is published as the original PDF, the raw model output,
the converted HTML, and the PDF's own text layer.

	
		
	
	
		Layout
	


	
		
Path
Contents


		
pdf/
Source PDFs, exactly as downloaded from the court


pages/
Page images fed to the model (PNG, 300 dpi)


raw/
Unmodified model output, including <|det|> layout markers


html/
Converted… See the full description on the dataset page: https://huggingface.co/datasets/jswhitworth/ocr-demo-documents. |
| [bhumika-tewari-282006/assistive-ocr-benchmark-results](https://huggingface.co/datasets/bhumika-tewari-282006/assistive-ocr-benchmark-results) | 2026-08-05 | text-recognition | candidate | 
	
		
	
	
		Assistive OCR — Benchmark Results
	

Real, reproducible benchmark results for the assistive OCR wearable module (offline, multilingual — English, Bengali+English, Hindi+English). This repository is self-contained: it holds the results, the ground-truth manifest, and the 98 real images they were computed from, so it can be run and demoed directly with no other dataset needed. (The same images are also published at Arko007/assistive-ocr-data-acquisition, folder… See the full description on the dataset page: https://huggingface.co/datasets/bhumika-tewari-282006/assistive-ocr-benchmark-results. |
| [SeeWye/Nondeterministic_Finite_Automata_OCR_vtest](https://huggingface.co/datasets/SeeWye/Nondeterministic_Finite_Automata_OCR_vtest) | 2026-08-04 | text-recognition | candidate | — |
| [p4ulbr4dl3y/passport-ocr-vlm](https://huggingface.co/datasets/p4ulbr4dl3y/passport-ocr-vlm) | 2026-08-04 | text-recognition | candidate | — |
| [christinamaria/cord-v2-ocr](https://huggingface.co/datasets/christinamaria/cord-v2-ocr) | 2026-08-04 | text-recognition | candidate | 
	
		
	
	
		CORD-v2 text-only — receipt OCR text → structured JSON
	

A text-only derivative of CORD-v2 (Consolidated Receipt Dataset; Park et al., 2019), the standard benchmark for document information extraction used by Donut and similar models. The original dataset pairs 1,000 receipt photos with a rich ground-truth schema (~30 field types across 4 groups, including menu line items). This version drops the images and pairs the OCR text of each receipt with its target parse, so text-only… See the full description on the dataset page: https://huggingface.co/datasets/christinamaria/cord-v2-ocr. |
| [arolstar52/ocr-synthetic-multilingual-v1-tokenized-zh-hans](https://huggingface.co/datasets/arolstar52/ocr-synthetic-multilingual-v1-tokenized-zh-hans) | 2026-08-04 | text-recognition | candidate | — |
| [Zeldeo/ocr-handwritten-receipt](https://huggingface.co/datasets/Zeldeo/ocr-handwritten-receipt) | 2026-08-03 | handwriting-recognition, text-recognition | candidate | — |
| [Zeldeo/ocr-handwritten-labeled](https://huggingface.co/datasets/Zeldeo/ocr-handwritten-labeled) | 2026-08-03 | handwriting-recognition, text-recognition | candidate | — |
| [swastikgahukar007/odia-ocr-benchmark](https://huggingface.co/datasets/swastikgahukar007/odia-ocr-benchmark) | 2026-08-03 | handwriting-recognition, text-recognition | candidate | 
	
		
	
	
		Odia OCR Benchmark Dataset
	


	
		
	
	
		Description
	

A curated benchmark dataset for evaluating OCR models on Odia (Oriya) text recognition.
Contains handwritten, printed, scene text, newspaper, books, and digital categories,
including both short samples and long-text examples for OCR evaluation.

	
		
	
	
		Dataset Structure
	


id: Unique identifier for each sample
image: The input image (PIL Image)
ground_truth: The correct Odia text transcription
category: Type of text… See the full description on the dataset page: https://huggingface.co/datasets/swastikgahukar007/odia-ocr-benchmark. |
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
