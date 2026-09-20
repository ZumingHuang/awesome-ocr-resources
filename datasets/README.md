<!-- Generated from data/*.yaml. Do not edit directly. -->

# Datasets

| Resource | Released | Tasks | Status | Description |
| --- | --- | --- | --- | --- |
| [Leon-klein/test-document-ocr](https://huggingface.co/datasets/Leon-klein/test-document-ocr) | 2026-09-20 | text-recognition | candidate | 
	
		
	
	
		Document OCR Audio Video Data Notes
	


	
		
	
	
		Dataset summary
	

This repository contains a preparation pipeline and a small metadata sample for Document OCR work with Audio Video inputs. It does not claim to be a complete benchmark release; the loader documents how source data is normalized and validated.

	
		
	
	
		Included material
	


prepare.py — loading, cleaning, and split preparation code.
dataset_infos.json — schema and split metadata.
metadata_sample.jsonl — small… See the full description on the dataset page: https://huggingface.co/datasets/Leon-klein/test-document-ocr. |
| [V4ldeLund/Faroese-Handwritten-OCR](https://huggingface.co/datasets/V4ldeLund/Faroese-Handwritten-OCR) | 2026-09-19 | handwriting-recognition, text-recognition | candidate | 
	
		
	
	
		Faroese Handwritten OCR
	

Public draft, version 0.1: an alignment pilot with 16 line-image/text pairs from one
historical Faroese manuscript page. No rows are verified benchmark ground truth.
The page is image 3 of D IV – Ániasar táttur, held by Landsbókasavnið
(National Library of the Faroe Islands) and digitized on HandRit. The manuscript
is associated with the scribe Jóhan Hendrik Schrøter (1842–1911). Proposed
reference text is aligned from Eivind Weyhe's scholarly edition of… See the full description on the dataset page: https://huggingface.co/datasets/V4ldeLund/Faroese-Handwritten-OCR. |
| [raogaurav/document-ocr-samples](https://huggingface.co/datasets/raogaurav/document-ocr-samples) | 2026-09-19 | text-recognition | candidate | 
	
		
	
	
		Document OCR Image Text Data Notes
	


	
		
	
	
		Dataset summary
	

A documented Document OCR data-preparation workflow for Image Text records. The bundled rows demonstrate the schema and validation path rather than pretending to be a full training corpus.

	
		
	
	
		Included material
	


dataset.py — loading, cleaning, and split preparation code.
dataset_infos.json — schema and split metadata.
metadata_sample.jsonl — small, human-readable records for checking the schema.… See the full description on the dataset page: https://huggingface.co/datasets/raogaurav/document-ocr-samples. |
| [Xrenya/rvl_ocr](https://huggingface.co/datasets/Xrenya/rvl_ocr) | 2026-09-18 | text-recognition | candidate | — |
| [Siddharthcmehta/intern-document-ocr10](https://huggingface.co/datasets/Siddharthcmehta/intern-document-ocr10) | 2026-09-18 | text-recognition | candidate | 
	
		
	
	
		Document OCR Image Depth Data Notes
	


	
		
	
	
		Dataset summary
	

This data card accompanies a lightweight Document OCR loader for Image Depth metadata. It is meant for pipeline inspection, source adaptation, and reproducible split preparation.

	
		
	
	
		Included material
	


load_data.py — loading, cleaning, and split preparation code.
dataset_infos.json — schema and split metadata.
metadata_sample.jsonl — small, human-readable records for checking the schema.
README.md —… See the full description on the dataset page: https://huggingface.co/datasets/Siddharthcmehta/intern-document-ocr10. |
| [jankowskijulia/document-ocr-video-text-clean](https://huggingface.co/datasets/jankowskijulia/document-ocr-video-text-clean) | 2026-09-18 | text-recognition | candidate | 
	
		
	
	
		Document OCR Video Text Data Notes
	


	
		
	
	
		Dataset summary
	

This data card accompanies a lightweight Document OCR loader for Video Text metadata. It is meant for pipeline inspection, source adaptation, and reproducible split preparation.

	
		
	
	
		Included material
	


loader.py — loading, cleaning, and split preparation code.
dataset_infos.json — schema and split metadata.
metadata_sample.jsonl — small, human-readable records for checking the schema.
README.md — data… See the full description on the dataset page: https://huggingface.co/datasets/jankowskijulia/document-ocr-video-text-clean. |
| [jaeminparkland/document-ocr-corpus](https://huggingface.co/datasets/jaeminparkland/document-ocr-corpus) | 2026-09-18 | text-recognition | candidate | 
	
		
	
	
		Document OCR Text Tabular Data Notes
	


	
		
	
	
		Dataset summary
	

Preparation notes and schema examples for Document OCR tasks using Text Tabular data. Full source material is intentionally not bundled, so provenance and licensing remain explicit.

	
		
	
	
		Included material
	


prepare.py — loading, cleaning, and split preparation code.
dataset_infos.json — schema and split metadata.
metadata_sample.jsonl — small, human-readable records for checking the schema.
README.md —… See the full description on the dataset page: https://huggingface.co/datasets/jaeminparkland/document-ocr-corpus. |
| [iamkushagratomar/devanagari-ocr-synthetic-80k](https://huggingface.co/datasets/iamkushagratomar/devanagari-ocr-synthetic-80k) | 2026-09-18 | text-recognition | candidate | 
	
		
	
	
		Devanagari OCR Synthetic 80K
	

80,000 synthetically rendered Devanagari (Hindi) text-line images paired with
their ground-truth transcription, intended for training / fine-tuning OCR and
text-recognition models (e.g. TrOCR, Donut, CRNN-CTC).
Each image is a single line of Hindi text rendered with a randomly chosen
font and font size.

	
		
	
	
		Dataset Structure
	


	
		
column
type
description


		
image
Image
rendered text-line image (RGB PNG, 900x64 px)


text
string… See the full description on the dataset page: https://huggingface.co/datasets/iamkushagratomar/devanagari-ocr-synthetic-80k. |
| [saeid1999/fa-en-ar-handwritten-ocr-v1](https://huggingface.co/datasets/saeid1999/fa-en-ar-handwritten-ocr-v1) | 2026-09-17 | handwriting-recognition, text-recognition | candidate | 
	
		
	
	
		Multi-script Synthetic Handwritten OCR — fa / ar / en
	

A large, clean, augmentation-rich synthetic handwriting dataset for
training and benchmarking OCR / HTR models on Persian (fa), Arabic
(ar) and English (en). Every line image ships with an exact Unicode
transcription plus rich provenance metadata (writer style, font, ink, script
direction, digit system). Page-level PAGE-XML and COCO ground truth support
layout-aware training and evaluation out of the box.

1,000 rendered… See the full description on the dataset page: https://huggingface.co/datasets/saeid1999/fa-en-ar-handwritten-ocr-v1. |
| [OdiaGenAIOCR/odia-ocr-chatml](https://huggingface.co/datasets/OdiaGenAIOCR/odia-ocr-chatml) | 2026-09-17 | text-recognition | candidate | — |
| [justtaeyoungoh/document-ocr-collection](https://huggingface.co/datasets/justtaeyoungoh/document-ocr-collection) | 2026-09-16 | text-recognition | candidate | 
	
		
	
	
		Document OCR Pointcloud Text Data Notes
	


	
		
	
	
		Dataset summary
	

This repository contains a preparation pipeline and a small metadata sample for Document OCR work with Pointcloud Text inputs. It does not claim to be a complete benchmark release; the loader documents how source data is normalized and validated.

	
		
	
	
		Included material
	


clean.py — loading, cleaning, and split preparation code.
dataset_infos.json — schema and split metadata.
metadata_sample.jsonl —… See the full description on the dataset page: https://huggingface.co/datasets/justtaeyoungoh/document-ocr-collection. |
| [fwgpiyawudk/Thai_Insurance_Docs_OCR](https://huggingface.co/datasets/fwgpiyawudk/Thai_Insurance_Docs_OCR) | 2026-09-16 | text-recognition | candidate | — |
| [fwgpiyawudk/Thai_e-Government_Procurement_OCR](https://huggingface.co/datasets/fwgpiyawudk/Thai_e-Government_Procurement_OCR) | 2026-09-16 | text-recognition | candidate | — |
| [uv-scripts/ocr-demo](https://huggingface.co/datasets/uv-scripts/ocr-demo) | 2026-09-15 | text-recognition | candidate | 
	
		
	
	
		OCR demo: Food for Space Flight
	

Seven scanned pages from NASA's Food for Space Flight booklet, with headings,
columns, photographs, food lists and tables. This small dataset is an input for
trying OCR recipes and inspecting their results.
The images are PDF pages 3-9 (printed pages 2-8) of the original booklet.
The selection omits the reproduction disclaimer and dark cover. The complete
original PDF and a matching seven-page extract are in the
OCR demo Bucket.

	
		
	
	
		Use as… See the full description on the dataset page: https://huggingface.co/datasets/uv-scripts/ocr-demo. |
| [TPELEE83/document-ocr-image-audio](https://huggingface.co/datasets/TPELEE83/document-ocr-image-audio) | 2026-09-15 | text-recognition | candidate | 
	
		
	
	
		Document OCR Image Audio Data Notes
	


	
		
	
	
		Dataset summary
	

This data card accompanies a lightweight Document OCR loader for Image Audio metadata. It is meant for pipeline inspection, source adaptation, and reproducible split preparation.

	
		
	
	
		Included material
	


preprocess.py — loading, cleaning, and split preparation code.
dataset_infos.json — schema and split metadata.
metadata_sample.jsonl — small, human-readable records for checking the schema.
README.md —… See the full description on the dataset page: https://huggingface.co/datasets/TPELEE83/document-ocr-image-audio. |
| [Sigurdur/icelandic-ocr-benchmark](https://huggingface.co/datasets/Sigurdur/icelandic-ocr-benchmark) | 2026-09-15 | text-recognition | candidate | 
	
		
	
	
		Dataset Card for Icelandic OCR Benchmark
	


	
		
	
	
		Dataset Details
	


	
		
	
	
		Dataset Description
	

Icelandic OCR Benchmark is a ground-truth dataset for evaluating OCR accuracy on
Icelandic-language documents. It consists of manually transcribed page images with
matching layout annotations (text regions, line polygons, baselines) in both ALTO
and PAGE XML.

Curated by: Sigurdur Haukur Birgisson
Language(s): Icelandic (is)
License: CC BY-SA 4.0


	
		
	
	
		Dataset… See the full description on the dataset page: https://huggingface.co/datasets/Sigurdur/icelandic-ocr-benchmark. |
| [nicholasnelson/document-ocr-audio-video-v2-2023](https://huggingface.co/datasets/nicholasnelson/document-ocr-audio-video-v2-2023) | 2026-09-15 | text-recognition | candidate | 
	
		
	
	
		Document OCR Audio Video Data Notes
	


	
		
	
	
		Dataset summary
	

This data card accompanies a lightweight Document OCR loader for Audio Video metadata. It is meant for pipeline inspection, source adaptation, and reproducible split preparation.

	
		
	
	
		Included material
	


prepare.py — loading, cleaning, and split preparation code.
dataset_infos.json — schema and split metadata.
metadata_sample.jsonl — small, human-readable records for checking the schema.
README.md — data… See the full description on the dataset page: https://huggingface.co/datasets/nicholasnelson/document-ocr-audio-video-v2-2023. |
| [meharuhanzz/OCR-Bench1000-Telugu](https://huggingface.co/datasets/meharuhanzz/OCR-Bench1000-Telugu) | 2026-09-15 | text-recognition | candidate | 
	
		
	
	
		OCR-Bench1000-Telugu
	

1000 synthetic printed-text line images with ground-truth transcriptions,
sampled from a larger locally-held Telugu OCR training corpus.
This is a benchmark/sample release, not the full training set.

	
		
	
	
		Data fields
	


	
		
Field
Description


		
file_name
relative path to the image (images/...)


text
ground-truth transcription


category
telugu_only / english_only / mixed / numeric_and_symbols


length_bucket
short / medium / long, by character… See the full description on the dataset page: https://huggingface.co/datasets/meharuhanzz/OCR-Bench1000-Telugu. |
| [meharuhanzz/OCR-Bench1000-Tamil](https://huggingface.co/datasets/meharuhanzz/OCR-Bench1000-Tamil) | 2026-09-15 | text-recognition | candidate | 
	
		
	
	
		OCR-Bench1000-Tamil
	

1000 synthetic printed-text line images with ground-truth transcriptions,
sampled from a larger locally-held Tamil OCR training corpus.
This is a benchmark/sample release, not the full training set.

	
		
	
	
		Data fields
	


	
		
Field
Description


		
file_name
relative path to the image (images/...)


text
ground-truth transcription


category
tamil_only / english_only / mixed / numeric_and_symbols


length_bucket
short / medium / long, by character count… See the full description on the dataset page: https://huggingface.co/datasets/meharuhanzz/OCR-Bench1000-Tamil. |
| [meharuhanzz/OCR-Bench1000-Sanskrit](https://huggingface.co/datasets/meharuhanzz/OCR-Bench1000-Sanskrit) | 2026-09-15 | text-recognition | candidate | 
	
		
	
	
		OCR-Bench1000-Sanskrit
	

1000 synthetic printed-text line images with ground-truth transcriptions,
sampled from a larger locally-held Sanskrit OCR training corpus.
This is a benchmark/sample release, not the full training set.

	
		
	
	
		Data fields
	


	
		
Field
Description


		
file_name
relative path to the image (images/...)


text
ground-truth transcription


category
sanskrit_only / english_only / mixed / numeric_and_symbols


length_bucket
short / medium / long, by… See the full description on the dataset page: https://huggingface.co/datasets/meharuhanzz/OCR-Bench1000-Sanskrit. |
| [meharuhanzz/OCR-Bench1000-Punjabi](https://huggingface.co/datasets/meharuhanzz/OCR-Bench1000-Punjabi) | 2026-09-15 | text-recognition | candidate | 
	
		
	
	
		OCR-Bench1000-Punjabi
	

1000 synthetic printed-text line images with ground-truth transcriptions,
sampled from a larger locally-held Punjabi OCR training corpus.
This is a benchmark/sample release, not the full training set.

	
		
	
	
		Data fields
	


	
		
Field
Description


		
file_name
relative path to the image (images/...)


text
ground-truth transcription


category
punjabi_only / english_only / mixed / numeric_and_symbols


length_bucket
short / medium / long, by character… See the full description on the dataset page: https://huggingface.co/datasets/meharuhanzz/OCR-Bench1000-Punjabi. |
| [meharuhanzz/OCR-Bench1000-Marathi](https://huggingface.co/datasets/meharuhanzz/OCR-Bench1000-Marathi) | 2026-09-15 | text-recognition | candidate | 
	
		
	
	
		OCR-Bench1000-Marathi
	

1000 synthetic printed-text line images with ground-truth transcriptions,
sampled from a larger locally-held Marathi OCR training corpus.
This is a benchmark/sample release, not the full training set.

	
		
	
	
		Data fields
	


	
		
Field
Description


		
file_name
relative path to the image (images/...)


text
ground-truth transcription


category
marathi_only / english_only / mixed / numeric_and_symbols


length_bucket
short / medium / long, by character… See the full description on the dataset page: https://huggingface.co/datasets/meharuhanzz/OCR-Bench1000-Marathi. |
| [meharuhanzz/OCR-Bench1000-Malayalam](https://huggingface.co/datasets/meharuhanzz/OCR-Bench1000-Malayalam) | 2026-09-15 | text-recognition | candidate | 
	
		
	
	
		OCR-Bench1000-Malayalam
	

1000 synthetic printed-text line images with ground-truth transcriptions,
sampled from a larger locally-held Malayalam OCR training corpus.
This is a benchmark/sample release, not the full training set.

	
		
	
	
		Data fields
	


	
		
Field
Description


		
file_name
relative path to the image (images/...)


text
ground-truth transcription


category
malayalam_only / english_only / mixed / numeric_and_symbols


length_bucket
short / medium / long, by… See the full description on the dataset page: https://huggingface.co/datasets/meharuhanzz/OCR-Bench1000-Malayalam. |
| [meharuhanzz/OCR-Bench1000-Kannada](https://huggingface.co/datasets/meharuhanzz/OCR-Bench1000-Kannada) | 2026-09-15 | text-recognition | candidate | 
	
		
	
	
		OCR-Bench1000-Kannada
	

1000 synthetic printed-text line images with ground-truth transcriptions,
sampled from a larger locally-held Kannada OCR training corpus.
This is a benchmark/sample release, not the full training set.

	
		
	
	
		Data fields
	


	
		
Field
Description


		
file_name
relative path to the image (images/...)


text
ground-truth transcription


category
kannada_only / english_only / mixed / numeric_and_symbols


length_bucket
short / medium / long, by character… See the full description on the dataset page: https://huggingface.co/datasets/meharuhanzz/OCR-Bench1000-Kannada. |
| [meharuhanzz/OCR-Bench1000-Hindi](https://huggingface.co/datasets/meharuhanzz/OCR-Bench1000-Hindi) | 2026-09-15 | text-recognition | candidate | 
	
		
	
	
		OCR-Bench1000-Hindi
	

1000 synthetic printed-text line images with ground-truth transcriptions,
sampled from a larger locally-held Hindi OCR training corpus.
This is a benchmark/sample release, not the full training set.

	
		
	
	
		Data fields
	


	
		
Field
Description


		
file_name
relative path to the image (images/...)


text
ground-truth transcription


category
hindi_only / english_only / mixed / numeric_and_symbols


length_bucket
short / medium / long, by character count… See the full description on the dataset page: https://huggingface.co/datasets/meharuhanzz/OCR-Bench1000-Hindi. |
| [meharuhanzz/OCR-Bench1000-Gujarati](https://huggingface.co/datasets/meharuhanzz/OCR-Bench1000-Gujarati) | 2026-09-15 | text-recognition | candidate | 
	
		
	
	
		OCR-Bench1000-Gujarati
	

1000 synthetic printed-text line images with ground-truth transcriptions,
sampled from a larger locally-held Gujarati OCR training corpus.
This is a benchmark/sample release, not the full training set.

	
		
	
	
		Data fields
	


	
		
Field
Description


		
file_name
relative path to the image (images/...)


text
ground-truth transcription


category
gujarati_only / english_only / mixed / numeric_and_symbols


length_bucket
short / medium / long, by… See the full description on the dataset page: https://huggingface.co/datasets/meharuhanzz/OCR-Bench1000-Gujarati. |
| [meharuhanzz/OCR-Bench1000-Bengali](https://huggingface.co/datasets/meharuhanzz/OCR-Bench1000-Bengali) | 2026-09-15 | text-recognition | candidate | 
	
		
	
	
		OCR-Bench1000-Bengali
	

1000 synthetic printed-text line images with ground-truth transcriptions,
sampled from a larger locally-held Bengali OCR training corpus.
This is a benchmark/sample release, not the full training set.

	
		
	
	
		Data fields
	


	
		
Field
Description


		
file_name
relative path to the image (images/...)


text
ground-truth transcription


category
bengali_only / english_only / mixed / numeric_and_symbols


length_bucket
short / medium / long, by character… See the full description on the dataset page: https://huggingface.co/datasets/meharuhanzz/OCR-Bench1000-Bengali. |
| [koharugwatanabe/document-ocr-audio-text-curated6-2024](https://huggingface.co/datasets/koharugwatanabe/document-ocr-audio-text-curated6-2024) | 2026-09-15 | text-recognition | candidate | 
	
		
	
	
		Document OCR Audio Text Data Notes
	


	
		
	
	
		Dataset summary
	

A documented Document OCR data-preparation workflow for Audio Text records. The bundled rows demonstrate the schema and validation path rather than pretending to be a full training corpus.

	
		
	
	
		Included material
	


prepare.py — loading, cleaning, and split preparation code.
dataset_infos.json — schema and split metadata.
metadata_sample.jsonl — small, human-readable records for checking the schema.… See the full description on the dataset page: https://huggingface.co/datasets/koharugwatanabe/document-ocr-audio-text-curated6-2024. |
| [icfoss/malayalam-ocr-words](https://huggingface.co/datasets/icfoss/malayalam-ocr-words) | 2026-09-15 | text-recognition | candidate | 
	
		
	
	
		Malayalam OCR Words
	

A word-level Malayalam OCR dataset: cropped word images paired with their
transcribed text label, split into train/validation/test sets.

	
		
	
	
		Dataset structure
	

train.csv / val.csv / test.csv   # tab-separated: <relative image path>\t<Malayalam word>
train/ val/ test/                # image files referenced by the corresponding CSV

Each CSV row maps one image file (path relative to its split folder) to its
ground-truth Malayalam word transcription.… See the full description on the dataset page: https://huggingface.co/datasets/icfoss/malayalam-ocr-words. |
| [gaelferre/personal-document-ocr](https://huggingface.co/datasets/gaelferre/personal-document-ocr) | 2026-09-15 | text-recognition | candidate | 
	
		
	
	
		Document OCR Audio Video Data Notes
	


	
		
	
	
		Dataset summary
	

This data card accompanies a lightweight Document OCR loader for Audio Video metadata. It is meant for pipeline inspection, source adaptation, and reproducible split preparation.

	
		
	
	
		Included material
	


dataset.py — loading, cleaning, and split preparation code.
dataset_infos.json — schema and split metadata.
metadata_sample.jsonl — small, human-readable records for checking the schema.
README.md — data… See the full description on the dataset page: https://huggingface.co/datasets/gaelferre/personal-document-ocr. |
| [DestinyJdj/learn-document-ocr](https://huggingface.co/datasets/DestinyJdj/learn-document-ocr) | 2026-09-15 | text-recognition | candidate | 
	
		
	
	
		Document OCR Image Audio Data Notes
	


	
		
	
	
		Dataset summary
	

A documented Document OCR data-preparation workflow for Image Audio records. The bundled rows demonstrate the schema and validation path rather than pretending to be a full training corpus.

	
		
	
	
		Included material
	


build_dataset.py — loading, cleaning, and split preparation code.
dataset_infos.json — schema and split metadata.
metadata_sample.jsonl — small, human-readable records for checking the schema.… See the full description on the dataset page: https://huggingface.co/datasets/DestinyJdj/learn-document-ocr. |
| [davanstrien/ocr-demo-results](https://huggingface.co/datasets/davanstrien/ocr-demo-results) | 2026-09-15 | text-recognition | candidate | 
	
		
	
	
		Document OCR using GLM-OCR
	

This dataset contains OCR results from images in uv-scripts/ocr-demo using GLM-OCR, a compact 0.9B OCR model achieving SOTA performance.

	
		
	
	
		Processing Details
	


Source Dataset: uv-scripts/ocr-demo
Model: zai-org/GLM-OCR
Task: text recognition
Number of Samples: 7
Processing Time: 2.4 min
Processing Date: 2026-09-15 16:30 UTC


	
		
	
	
		Configuration
	


Image Column: image
Output Column: markdown
Dataset Split: train
Batch Size: 16
Max… See the full description on the dataset page: https://huggingface.co/datasets/davanstrien/ocr-demo-results. |
| [danielcybq/document-ocr-samples](https://huggingface.co/datasets/danielcybq/document-ocr-samples) | 2026-09-15 | text-recognition | candidate | 
	
		
	
	
		Document OCR Pointcloud Text Data Notes
	


	
		
	
	
		Dataset summary
	

This repository contains a preparation pipeline and a small metadata sample for Document OCR work with Pointcloud Text inputs. It does not claim to be a complete benchmark release; the loader documents how source data is normalized and validated.

	
		
	
	
		Included material
	


preprocess.py — loading, cleaning, and split preparation code.
dataset_infos.json — schema and split metadata.… See the full description on the dataset page: https://huggingface.co/datasets/danielcybq/document-ocr-samples. |
| [sophiesmith/document-ocr-sensor-fusion](https://huggingface.co/datasets/sophiesmith/document-ocr-sensor-fusion) | 2026-09-14 | text-recognition | candidate | 
	
		
	
	
		Document OCR Sensor Fusion Data Notes
	


	
		
	
	
		Dataset summary
	

This repository contains a preparation pipeline and a small metadata sample for Document OCR work with Sensor Fusion inputs. It does not claim to be a complete benchmark release; the loader documents how source data is normalized and validated.

	
		
	
	
		Included material
	


prepare.py — loading, cleaning, and split preparation code.
dataset_infos.json — schema and split metadata.
metadata_sample.jsonl —… See the full description on the dataset page: https://huggingface.co/datasets/sophiesmith/document-ocr-sensor-fusion. |
| [PiotrSty/impact-psnc-polish-ocr](https://huggingface.co/datasets/PiotrSty/impact-psnc-polish-ocr) | 2026-09-14 | text-recognition | candidate | 
	
		
	
	
		IMPACT-PSNC Polish OCR Diverse Subset
	

Compact, provenance-preserving subset of the Polish IMPACT ground truth released by the Poznan Supercomputing and Networking Center (PSNC). It is intended for OCR experiments on diverse historical Polish printed material.
This subset contains:

89 full-page images from 30 source collections;
599 text-region crops derived from PAGE XML polygons;
the 89 corresponding original PAGE XML files;
page and region transcriptions;
document-level train… See the full description on the dataset page: https://huggingface.co/datasets/PiotrSty/impact-psnc-polish-ocr. |
| [Arthursouza03/document-ocr-samples](https://huggingface.co/datasets/Arthursouza03/document-ocr-samples) | 2026-09-14 | text-recognition | candidate | 
	
		
	
	
		Document OCR Sensor Fusion Data Notes
	


	
		
	
	
		Dataset summary
	

Preparation notes and schema examples for Document OCR tasks using Sensor Fusion data. Full source material is intentionally not bundled, so provenance and licensing remain explicit.

	
		
	
	
		Included material
	


prepare.py — loading, cleaning, and split preparation code.
dataset_infos.json — schema and split metadata.
metadata_sample.jsonl — small, human-readable records for checking the schema.
README.md… See the full description on the dataset page: https://huggingface.co/datasets/Arthursouza03/document-ocr-samples. |
| [andersonoao/document-ocr-dataset42-2024](https://huggingface.co/datasets/andersonoao/document-ocr-dataset42-2024) | 2026-09-14 | text-recognition | candidate | 
	
		
	
	
		Document OCR Audio Video Data Notes
	


	
		
	
	
		Dataset summary
	

This repository contains a preparation pipeline and a small metadata sample for Document OCR work with Audio Video inputs. It does not claim to be a complete benchmark release; the loader documents how source data is normalized and validated.

	
		
	
	
		Included material
	


clean.py — loading, cleaning, and split preparation code.
dataset_infos.json — schema and split metadata.
metadata_sample.jsonl — small… See the full description on the dataset page: https://huggingface.co/datasets/andersonoao/document-ocr-dataset42-2024. |
| [aidendparker/document-ocr-audio-video-clean](https://huggingface.co/datasets/aidendparker/document-ocr-audio-video-clean) | 2026-09-14 | text-recognition | candidate | 
	
		
	
	
		Document OCR Audio Video Data Notes
	


	
		
	
	
		Dataset summary
	

This repository contains a preparation pipeline and a small metadata sample for Document OCR work with Audio Video inputs. It does not claim to be a complete benchmark release; the loader documents how source data is normalized and validated.

	
		
	
	
		Included material
	


build_dataset.py — loading, cleaning, and split preparation code.
dataset_infos.json — schema and split metadata.
metadata_sample.jsonl —… See the full description on the dataset page: https://huggingface.co/datasets/aidendparker/document-ocr-audio-video-clean. |
| [yusukeyama0705/research-document-ocr](https://huggingface.co/datasets/yusukeyama0705/research-document-ocr) | 2026-09-13 | text-recognition | candidate | 
	
		
	
	
		Document OCR Image Audio Data Notes
	


	
		
	
	
		Dataset summary
	

This data card accompanies a lightweight Document OCR loader for Image Audio metadata. It is meant for pipeline inspection, source adaptation, and reproducible split preparation.

	
		
	
	
		Included material
	


build_dataset.py — loading, cleaning, and split preparation code.
dataset_infos.json — schema and split metadata.
metadata_sample.jsonl — small, human-readable records for checking the schema.
README.md… See the full description on the dataset page: https://huggingface.co/datasets/yusukeyama0705/research-document-ocr. |
| [SeeWye/NFA_OCR_qwen_grpo_formatv2](https://huggingface.co/datasets/SeeWye/NFA_OCR_qwen_grpo_formatv2) | 2026-09-13 | text-recognition | candidate | — |
| [SeeWye/NFA_OCR_qwen_grpo_format1](https://huggingface.co/datasets/SeeWye/NFA_OCR_qwen_grpo_format1) | 2026-09-13 | text-recognition | candidate | — |
| [ryantanakawyn/document-ocr-image-audio-benchmark](https://huggingface.co/datasets/ryantanakawyn/document-ocr-image-audio-benchmark) | 2026-09-13 | text-recognition | candidate | 
	
		
	
	
		Document OCR Image Audio Data Notes
	


	
		
	
	
		Dataset summary
	

A documented Document OCR data-preparation workflow for Image Audio records. The bundled rows demonstrate the schema and validation path rather than pretending to be a full training corpus.

	
		
	
	
		Included material
	


clean.py — loading, cleaning, and split preparation code.
dataset_infos.json — schema and split metadata.
metadata_sample.jsonl — small, human-readable records for checking the schema.… See the full description on the dataset page: https://huggingface.co/datasets/ryantanakawyn/document-ocr-image-audio-benchmark. |
| [GwendalTsang/OCR-grec-polytonique](https://huggingface.co/datasets/GwendalTsang/OCR-grec-polytonique) | 2026-09-13 | text-recognition | candidate | 
	
		
	
	
		Dataset OCR aligné — grec polytonique imprimé (Legrand 1918)
	

Petit jeu de données page-image ↔ texte grec, destiné à évaluer des modèles
sur la transcription de grec ancien polytonique imprimé.

	
		
	
	
		Source
	


Fac-similé : bibliographiehel0001unse_t9o1.pdf (588 p.), numérisation
Internet Archive de É. Legrand, Bibliographie hellénique ou description
raisonnée des ouvrages publiés par des Grecs au dix-huitième siècle, t. 1,
Paris, 1918 —… See the full description on the dataset page: https://huggingface.co/datasets/GwendalTsang/OCR-grec-polytonique. |
| [francescores/document-ocr-pointcloud-text](https://huggingface.co/datasets/francescores/document-ocr-pointcloud-text) | 2026-09-13 | text-recognition | candidate | 
	
		
	
	
		Document OCR Pointcloud Text Data Notes
	


	
		
	
	
		Dataset summary
	

This repository contains a preparation pipeline and a small metadata sample for Document OCR work with Pointcloud Text inputs. It does not claim to be a complete benchmark release; the loader documents how source data is normalized and validated.

	
		
	
	
		Included material
	


clean.py — loading, cleaning, and split preparation code.
dataset_infos.json — schema and split metadata.
metadata_sample.jsonl —… See the full description on the dataset page: https://huggingface.co/datasets/francescores/document-ocr-pointcloud-text. |
| [PiotrSty/ocr-pl-lines](https://huggingface.co/datasets/PiotrSty/ocr-pl-lines) | 2026-09-12 | text-recognition | candidate | 
	
		
	
	
		ocr-pl-lines
	

Syntetyczny zbiór linii tekstu po polsku do fine-tuningu OCR (TrOCR).
Pary NNNNN.png (obraz linii) + NNNNN.txt (transkrypcja).

	
		
	
	
		Struktura
	


train/ — 2000 par (seed 42)
val/ — 200 par (seed 123)


	
		
	
	
		Generowanie
	

OCR_engine —
python -m training.generate_synthetic
Korpus: zdania potoczne i urzędowe, domeny (faktury, umowy, medyczne,
prawnicze), losowe daty/kwoty/adresy/NIP/PESEL, zdania z pl.wikipedia.org.
Augmentacje: pochylenie, blur, szum… See the full description on the dataset page: https://huggingface.co/datasets/PiotrSty/ocr-pl-lines. |
| [tehnik-tehnolog/bilingual-ocr-ru-en-synthetic](https://huggingface.co/datasets/tehnik-tehnolog/bilingual-ocr-ru-en-synthetic) | 2026-09-11 | text-recognition | candidate | 
	
		
	
	
		Bilingual OCR RU-EN Synthetic Dataset
	

This synthetic dataset is designed for bilingual text recognition (OCR) and script classification tasks (cyrillic / latin) at the word and short-line level.

	
		
	
	
		Why are numbers, mathematical symbols, and the Greek alphabet included in the generation?
	

When creating synthetic OCR datasets, including an expanded set of characters (digits, mathematical signs, and Greek letters) is a deliberate step aimed at two main goals:… See the full description on the dataset page: https://huggingface.co/datasets/tehnik-tehnolog/bilingual-ocr-ru-en-synthetic. |
| [Smartlearners/LaTeX_OCR](https://huggingface.co/datasets/Smartlearners/LaTeX_OCR) | 2026-09-11 | text-recognition | candidate | — |
| [Nexdata-kr/104320-Images-Korean-and-Hindi-OCR-Data-in-Natural-Scenes](https://huggingface.co/datasets/Nexdata-kr/104320-Images-Korean-and-Hindi-OCR-Data-in-Natural-Scenes) | 2026-09-11 | text-recognition | candidate | 
	
		
	
	
		Description
	

104,320장 규모의 한국어 및 힌디어 자연 환경 OCR 데이터셋입니다. 데이터는 포장지, 포스터, 티켓, 안내문, 메뉴, 건물 표지판 등 다양한 실환경에서 수집되었습니다. 다양한 자연 환경, 촬영 각도 및 조명 조건을 포함하여 데이터의 다양성을 확보했습니다.
어노테이션은 텍스트의 행 단위 폴리곤 바운딩 박스(또는 사각형/직사각형 바운딩 박스), 전사 및 텍스트 속성(언어 유형) 정보를 포함하며, 세로 방향 텍스트에 대해서도 폴리곤 바운딩 박스(또는 사각형/직사각형 바운딩 박스), 전사 및 텍스트 속성(언어 유형) 정보를 제공합니다. 본 데이터셋은 자연 환경에서의 한국어 및 힌디어 OCR 작업에 활용할 수 있습니다.
자세한 내용은 아래 링크를 참고해 주세요: https://ko.nexdata.ai/datasets/ocr/1254?source=hf.kr

	
		
	
	
		Data size
	

한국어 이미지 76,861장… See the full description on the dataset page: https://huggingface.co/datasets/Nexdata-kr/104320-Images-Korean-and-Hindi-OCR-Data-in-Natural-Scenes. |
| [nlpctx/sansad-ocr](https://huggingface.co/datasets/nlpctx/sansad-ocr) | 2026-09-10 | text-recognition | candidate | — |
| [HugoFernandeznon/ml-document-ocr](https://huggingface.co/datasets/HugoFernandeznon/ml-document-ocr) | 2026-09-10 | text-recognition | candidate | 
	
		
	
	
		Document OCR Video Text Data Notes
	


	
		
	
	
		Dataset summary
	

This repository contains a preparation pipeline and a small metadata sample for Document OCR work with Video Text inputs. It does not claim to be a complete benchmark release; the loader documents how source data is normalized and validated.

	
		
	
	
		Included material
	


clean.py — loading, cleaning, and split preparation code.
dataset_infos.json — schema and split metadata.
metadata_sample.jsonl — small… See the full description on the dataset page: https://huggingface.co/datasets/HugoFernandeznon/ml-document-ocr. |
| [Elliot-Data/ocrvqa_train_cleaned](https://huggingface.co/datasets/Elliot-Data/ocrvqa_train_cleaned) | 2026-09-10 | text-recognition | candidate | 
	
		
	
	
		ocrvqa_train_cleaned
	

The ocrvqa_train family of the ElliotVL supervised-fine-tuning pool, after VLM cleaning.

	
		




		
images
501,894


QA turns
3,616,618


answers rewritten by the cleaning pass
0


QA created by the cleaning pass (new_qa)
not measured for this family


shards
104


	


	
		
	
	
		How this was cleaned
	

A vision-language model read each image together with its QA and judged the item. The pass is
not a filter that only removes rows — it rewrites answers it… See the full description on the dataset page: https://huggingface.co/datasets/Elliot-Data/ocrvqa_train_cleaned. |
| [Somtharu181coder/Legal_domain_ocr_extracted_Nepali_sft_dataset](https://huggingface.co/datasets/Somtharu181coder/Legal_domain_ocr_extracted_Nepali_sft_dataset) | 2026-09-09 | text-recognition | candidate | 
	
		
	
	
		Nepali Legal SFT Dataset — Software Development & Operation Committee Order, 2083
	


	
		
	
	
		Dataset Summary
	

This dataset contains 31 single-turn instruction/response pairs in Nepali (Devanagari script), derived from a single Government of Nepal legal instrument:

सफ्टवेयर विकास तथा सञ्चालन समिति (गठन) आदेश, २०८३
(Software Development and Operation Committee (Formation) Order, 2083)

The order was issued by the Government of Nepal under Section 3 of the विकास समिति ऐन, २०१३… See the full description on the dataset page: https://huggingface.co/datasets/Somtharu181coder/Legal_domain_ocr_extracted_Nepali_sft_dataset. |
| [lab-ii/sakha-ocr-synth](https://huggingface.co/datasets/lab-ii/sakha-ocr-synth) | 2026-09-09 | text-recognition | candidate | 
	
		
	
	
		Синтетические строки якутского текста для OCR
	

500 000 изображений строк с точной разметкой. Сделано для обучения
распознавателя якутского (саха) текста: готовые движки для этого языка не
работают, а размеченных строк почти нет.
Зачем вообще синтетика: у tesseract-rus и ABBYY FineReader 10 на якутской
печати доля правильно прочитанных специфических букв ҕ ҥ ө һ ү равна нулю.
Не «низкая» — ноль на 460 тысячах букв, при том что эти буквы составляют около
7% всех букв и встречаются… See the full description on the dataset page: https://huggingface.co/datasets/lab-ii/sakha-ocr-synth. |
| [Elliot-Data/ureader_ocr_cleaned](https://huggingface.co/datasets/Elliot-Data/ureader_ocr_cleaned) | 2026-09-09 | text-recognition | candidate | 
	
		
	
	
		ureader_ocr_cleaned
	

The ureader_ocr__x family of the ElliotVL supervised-fine-tuning pool, after VLM cleaning.

	
		




		
images
862


QA turns
6,038


answers rewritten by the cleaning pass
403


QA created by the cleaning pass (new_qa)
3,952 (65.5%)


shards
1


	


	
		
	
	
		How this was cleaned
	

A vision-language model read each image together with its QA and judged the item. The pass is
not a filter that only removes rows — it rewrites answers it finds wrong but… See the full description on the dataset page: https://huggingface.co/datasets/Elliot-Data/ureader_ocr_cleaned. |
| [Elliot-Data/latex_ocr_cleaned](https://huggingface.co/datasets/Elliot-Data/latex_ocr_cleaned) | 2026-09-09 | text-recognition | candidate | 
	
		
	
	
		latex_ocr_cleaned
	

The latex_ocr__x family of the ElliotVL supervised-fine-tuning pool, after VLM cleaning.

	
		




		
images
72,345


QA turns
132,970


answers rewritten by the cleaning pass
7,072


QA created by the cleaning pass (new_qa)
66,310 (49.9%)


shards
1


	


	
		
	
	
		How this was cleaned
	

A vision-language model read each image together with its QA and judged the item. The pass is
not a filter that only removes rows — it rewrites answers it finds wrong but… See the full description on the dataset page: https://huggingface.co/datasets/Elliot-Data/latex_ocr_cleaned. |
| [Elliot-Data/invoices-and-receipts_ocr_cleaned](https://huggingface.co/datasets/Elliot-Data/invoices-and-receipts_ocr_cleaned) | 2026-09-09 | text-recognition | candidate | 
	
		
	
	
		invoices-and-receipts_ocr_cleaned
	

The invoices-and-receipts_ocr__x family of the ElliotVL supervised-fine-tuning pool, after VLM cleaning.

	
		




		
images
2,221


QA turns
7,696


answers rewritten by the cleaning pass
1,517


QA created by the cleaning pass (new_qa)
4,651 (60.4%)


shards
4


	


	
		
	
	
		How this was cleaned
	

A vision-language model read each image together with its QA and judged the item. The pass is
not a filter that only removes rows — it rewrites… See the full description on the dataset page: https://huggingface.co/datasets/Elliot-Data/invoices-and-receipts_ocr_cleaned. |
| [baicai1145/pp-ocr-mnn-eval](https://huggingface.co/datasets/baicai1145/pp-ocr-mnn-eval) | 2026-09-09 | text-recognition | candidate | 
	
		
	
	
		PP-OCR MNN evaluation dataset (811-cell matrix)
	

Images (273) + canonical paddle.inference baselines (808 json) + configs
for scoring pp-ocr-mnn outputs. See README.md and
https://github.com/baicai1145/pp-ocr-mnn (tools/score.py).
A single-file snapshot is also included as ppocr-eval-dataset.tar.zst.
 |
| [arolstar52/ocr-synthetic-multilingual-v1-tokenized-en](https://huggingface.co/datasets/arolstar52/ocr-synthetic-multilingual-v1-tokenized-en) | 2026-09-09 | text-recognition | candidate | — |
| [AndyC01/raw_4experts_ocr_chart_gd_zoom](https://huggingface.co/datasets/AndyC01/raw_4experts_ocr_chart_gd_zoom) | 2026-09-09 | text-recognition | candidate | — |
| [sshenfiona1992/document-ocr-pointcloud-text-mini](https://huggingface.co/datasets/sshenfiona1992/document-ocr-pointcloud-text-mini) | 2026-09-08 | text-recognition | candidate | 
	
		
	
	
		Document OCR Pointcloud Text Data Notes
	


	
		
	
	
		Dataset summary
	

This repository contains a preparation pipeline and a small metadata sample for Document OCR work with Pointcloud Text inputs. It does not claim to be a complete benchmark release; the loader documents how source data is normalized and validated.

	
		
	
	
		Included material
	


dataset.py — loading, cleaning, and split preparation code.
dataset_infos.json — schema and split metadata.
metadata_sample.jsonl —… See the full description on the dataset page: https://huggingface.co/datasets/sshenfiona1992/document-ocr-pointcloud-text-mini. |
| [Nexdata-kr/5711-Images-Korean-Handwriting-OCR-Dataset](https://huggingface.co/datasets/Nexdata-kr/5711-Images-Korean-Handwriting-OCR-Dataset) | 2026-09-08 | handwriting-recognition, text-recognition | candidate | 
	
		
	
	
		Description
	

5,711장의 한국어 손글씨 OCR 데이터셋으로, A4 용지, 줄노트, 모눈종이 등 다양한 형태의 용지에 작성된 한국어 손글씨 데이터를 포함하고 있습니다. 총 593명의 참여자로부터 수집되었으며, 스마트폰을 사용하여 정면 시점에서 촬영되었습니다. 데이터 내용은 한국어 작문, 시, 산문, 뉴스, 이야기 등 다양한 유형의 텍스트로 구성되어 있습니다. 어노테이션은 텍스트 라인 단위의 사각형 영역과 라인 단위 텍스트 전사로 구성되어 있습니다. 본 데이터셋은 한국어 손글씨 OCR 인식 및 관련 AI 모델 학습에 활용할 수 있습니다.
자세한 내용은 아래 링크를 참고해 주세요: https://ko.nexdata.ai/datasets/ocr/1297?source=hf.kr

	
		
	
	
		Specifications
	


	
		
	
	
		Data size
	

5,711장

	
		
	
	
		Speaker
	

총 593명성별 분포:… See the full description on the dataset page: https://huggingface.co/datasets/Nexdata-kr/5711-Images-Korean-Handwriting-OCR-Dataset. |
| [Nexdata-kr/500000-Images-Multilingual-OCR-Dataset-in-21-Languages](https://huggingface.co/datasets/Nexdata-kr/500000-Images-Multilingual-OCR-Dataset-in-21-Languages) | 2026-09-08 | text-recognition | candidate | 
	
		
	
	
		Description
	

500,000장 규모의 21개국 다국어 OCR 데이터로, 자연 환경, 문서 촬영 환경 및 전자 환경에서 수집된 이미지로 구성되어 있습니다. 본 데이터셋은 총 21개 언어를 지원하며, 각 언어별 데이터 수량은 약 20,000~25,000장입니다. 데이터 유형은 자연 환경 이미지, 문서 촬영 이미지, 전자 환경 이미지로 구성되어 있으며, 다양한 데이터 유형과 촬영 각도, 다국어 데이터를 포함하여 높은 데이터 다양성을 제공합니다. 어노테이션은 행(열) 단위의 사각형 또는 폴리곤 영역과 행(열) 단위의 텍스트 전사 방식으로 구성되어 있습니다. 본 데이터셋은 다국어 OCR 인식 및 관련 AI 모델 학습에 활용할 수 있습니다.
자세한 내용은 아래 링크를 참고해 주세요: https://ko.nexdata.ai/datasets/ocr/1862?source=hf.kr

	
		
	
	
		Specifications… See the full description on the dataset page: https://huggingface.co/datasets/Nexdata-kr/500000-Images-Multilingual-OCR-Dataset-in-21-Languages. |
| [arolstar52/ocr-synthetic-multilingual-v1-tokenized-ja](https://huggingface.co/datasets/arolstar52/ocr-synthetic-multilingual-v1-tokenized-ja) | 2026-09-08 | text-recognition | candidate | — |
| [hocnt84/vi-ocr-rec-v17-dataset](https://huggingface.co/datasets/hocnt84/vi-ocr-rec-v17-dataset) | 2026-09-07 | text-recognition | candidate | 
	
		
	
	
		vi-ocr-rec-v17-dataset
	

Dataset nhận dạng dòng chữ (PP-OCR recognition) dùng để train
hocnt84/vi-ocr-rec-v17.
Snapshot đúng lúc train V17 (2026-08-14): không phải rec_train.txt hiện tại
của repo (đã append V18/V19/V20…).

	
		
	
	
		Splits
	


	
		
File
Dòng
Vai trò


		
rec_train.txt
14.836
Train — nguồn rec_train.txt.bak_pre_v18


rec_val.txt
645
Val đã soi tay — thước đo cố định


vi_dict.txt
234 ký tự
Dict khớp V7/V15/V16/V17


lines/<hh>/
15.481 ảnh
Crop dòng (jpg); hh = 2… See the full description on the dataset page: https://huggingface.co/datasets/hocnt84/vi-ocr-rec-v17-dataset. |
| [cloudfrm-site/ocr-document-processing-eval](https://huggingface.co/datasets/cloudfrm-site/ocr-document-processing-eval) | 2026-09-07 | text-recognition | candidate | — |
| [cloudfrm-site/nepali-deva-ocr-eval](https://huggingface.co/datasets/cloudfrm-site/nepali-deva-ocr-eval) | 2026-09-07 | text-recognition | candidate | — |
| [cloudfrm-site/indic-deva-ocr-eval](https://huggingface.co/datasets/cloudfrm-site/indic-deva-ocr-eval) | 2026-09-07 | text-recognition | candidate | — |
| [cloudfrm-site/devanagari_ocr_pretrain](https://huggingface.co/datasets/cloudfrm-site/devanagari_ocr_pretrain) | 2026-09-07 | text-recognition | candidate | — |
| [chagatai-project/ocr](https://huggingface.co/datasets/chagatai-project/ocr) | 2026-09-07 | text-recognition | candidate | 
	
		
	
	
		Chagatai OCR
	

Chagatai text in Arabic script, with Cyrillic transcriptions and Kazakh translations.
The dataset is available as Dataset_OCR.xlsx and UTF-8 Dataset_OCR.csv. Both contain 875 non-empty data rows.

	
		
Column
Contents


		
Original
Text in Arabic script


Transcript
Cyrillic transcription


Translation (?)
Kazakh translation; the original column label is retained


Pages
Page markers, provided on selected rows


	

The Excel workbook is provided unchanged. The CSV… See the full description on the dataset page: https://huggingface.co/datasets/chagatai-project/ocr. |
| [xgboostgod/ottoman-newdata-ocr](https://huggingface.co/datasets/xgboostgod/ottoman-newdata-ocr) | 2026-09-06 | text-recognition | candidate | 
	
		
	
	
		📚 Ottoman NewData OCR Dataset (Matbu Nesih & Rika El Yazısı)
	

Bu veri kümesi, tarihî Osmanlıca belgeler ve matbuat arşivinden derlenmiş 1.951 satırlık yüksek kaliteli satır görseli (line crops) ve harfiyen doğrulanmış zemin gerçeği (ground truth) metinlerini içerir.

	
		
	
	
		📊 Dağılım ve İstatistikler
	


	
		
Alt Küme (Source)
Satır Sayısı
Yazı Türü / Baskı Tipi
Açıklama


		
naskh (Matbu)
376
Tarihî Matbuat / Nesih Font
Kitap ve gazetelerden kesilmiş satırlar… See the full description on the dataset page: https://huggingface.co/datasets/xgboostgod/ottoman-newdata-ocr. |
| [Safak11/lilly-ocr-paddle-runs](https://huggingface.co/datasets/Safak11/lilly-ocr-paddle-runs) | 2026-09-06 | text-recognition | candidate | — |
| [Raphael2099/zhou-ancient-texts-ocr-sources-20260906](https://huggingface.co/datasets/Raphael2099/zhou-ancient-texts-ocr-sources-20260906) | 2026-09-06 | text-recognition | candidate | 
	
		
	
	
		周代古文字编注与复旦教材 OCR 来源仓
	

公开 source-only 仓库，供来源审查和 OCR 流程复核。此仓库不是 OCR 结果仓，也不授予原书再分发许可。

	
		
	
	
		文件
	


	
		
ID
文件
页数
SHA-256
古文字策略


		
LZB-01
sources/LZB-01.pdf
977
6417f63272f8e6c9396ba7bceeb49159af0d30e3b0498dd0e92be20219de87ba
dictionary_whole_page_figure


LZB-02
sources/LZB-02.pdf
961
d6d60e245c1e4122c2def09f5c8dcb91272ff561c16848f408ee5664454b8948
dictionary_whole_page_figure


LZB-03
sources/LZB-03.pdf
973
714f16bfbe2a8e21ac6887b9056a6cf958c2a82292e19c088fff78a1e75728a8… See the full description on the dataset page: https://huggingface.co/datasets/Raphael2099/zhou-ancient-texts-ocr-sources-20260906. |
| [OCR-Data-new/ocr_data](https://huggingface.co/datasets/OCR-Data-new/ocr_data) | 2026-09-06 | text-recognition | candidate | 
	
		
	
	
		ocr_data
	

Synthetic Arabic document images with layout annotations, for OCR training.

	
		
	
	
		Layout
	

WebDataset .tar shards. Files sharing a basename are one sample, so the
image becomes the image column and the annotation the json column.
data/<contributor>_<NNN>.tar            originals (PNG + JSON)
data_aug/<contributor>_<NNN>_aug<K>.tar augmented variants (JPEG/PNG + JSON)

Each shard holds up to 9990 samples (~1.2 GB). data/ and data_aug/
are separate so you can train… See the full description on the dataset page: https://huggingface.co/datasets/OCR-Data-new/ocr_data. |
| [Kotomiya07/premodern-japanese-books-ocr-pairs](https://huggingface.co/datasets/Kotomiya07/premodern-japanese-books-ocr-pairs) | 2026-09-06 | text-recognition | candidate | 
	
		
	
	
		Premodern Japanese Books OCR Pairs
	


	
		
	
	
		日本語
	


	
		
	
	
		概要
	

日本古典籍統一データセット v0.1.0 の公開用Viewです。固定済み内部Releaseから、再配布と機械学習利用が許可された行だけを収録しています。収録行数は 641,400 行、収録SourceDataset数は 1 件です。

	
		
	
	
		用途
	

日本語歴史資料の研究、検索、OCRまたは言語モデル用データ処理に利用できます。個々の行には採用したCanonical ID、権利判定、必要な帰属を保持しています。

	
		
	
	
		権利
	

単一のライセンス値は全行の条件を表しません。必ず NOTICE.md と行単位の権利列を確認してください。

	
		
	
	
		限界
	

v0.1.0 は監査対象52候補のうち、固定入力が成立した21 SourceDatasetを対象とする段階公開です。内容の正確性、外部参照の永続性、特定用途への適合性を保証しません。… See the full description on the dataset page: https://huggingface.co/datasets/Kotomiya07/premodern-japanese-books-ocr-pairs. |
| [Raphael2099/qiuli-collected-works-ocr-sources-20260905](https://huggingface.co/datasets/Raphael2099/qiuli-collected-works-ocr-sources-20260905) | 2026-09-05 | text-recognition | candidate | 
	
		
	
	
		裘李全集：36册源书
	

公开来源核验与 OCR 工作档案（按用户要求供比赛评委核查）。李学勤30册、裘锡圭6册，15719 PDF页。原书仅作为来源材料，尚未完成本次OCR与GPT复核。文件映射、字节数、SHA256和页数见 SOURCE_MANIFEST.json。两个完全相同副本排除重复上传；裘集20页总目是辅助材料，不计入36册。
PDF页从1起；印刷页码另行OCR核定。本仓不授予原书公开再分发许可。
裘锡圭集按原页保留繁体，李学勤集按原页保留简体；引用古字、隶定字、异体不做全局繁简转换。模型配置沿用上一轮正式PaddleOCR-VL-1.5、PP-DocLayoutV3与Qwen3.5-9B。
 |
| [Raphael2099/qiuli-collected-works-ocr-reviewed-20260906](https://huggingface.co/datasets/Raphael2099/qiuli-collected-works-ocr-reviewed-20260906) | 2026-09-05 | text-recognition | candidate | 
	
		
	
	
		裘李全集逐页审核输出
	

当前只有以下 2页 按百度首扫、千问疑难/全页盘点、GPT本地原图全文审核分工验收并冻结。千问盘点不等于千问全文校对。

LXQ-01 PDF第6页：revision3，原冻结包保留；PDF7仅跨页证据。
QXG-4 PDF第30页（书页25）：revision3；PDF31仅跨页证据。

逐页canonical JSON是唯一当前真值，原始证据、模型版本/SHA与绝对路径映射均保留。源PDF仍在独立source-only仓。本仓不表示36册均审核完成，不额外授予原书版权许可。
 |
| [LocalDoc/azerbaijani-ocr-lines](https://huggingface.co/datasets/LocalDoc/azerbaijani-ocr-lines) | 2026-09-05 | text-recognition | candidate | 
	
		
	
	
		Azerbaijani OCR Lines
	

Line-level training data for Azerbaijani text recognition, in Latin and
Cyrillic script, extracted from scanned books.

	
		
	
	
		Fields
	


	
		
field
description


		
image
cropped text line, grayscale, height 48 px


text
transcription


script
az_latin or az_cyrillic


book
anonymised source-book id


	


	
		
	
	
		How it was built
	

Pages come from scanned PDFs that already carried an OCR text layer. Line
boxes were taken from that layer, rendered… See the full description on the dataset page: https://huggingface.co/datasets/LocalDoc/azerbaijani-ocr-lines. |
| [LocalDoc/azerbaijani-ocr-benchmark](https://huggingface.co/datasets/LocalDoc/azerbaijani-ocr-benchmark) | 2026-09-05 | text-recognition | candidate | 
	
		
	
	
		Azerbaijani OCR Benchmark
	

Line-level OCR benchmark for Azerbaijani in both Latin and Cyrillic script,
built from scanned books.

	
		
	
	
		Fields
	


	
		
field
description


		
image
cropped text line, grayscale, height 48 px


text
verbatim transcription


script
az_latin or az_cyrillic


book
anonymised source-book id


	


	
		
	
	
		How labels were produced
	

Every line carries a label agreed on independently by three sources: the
OCR text layer already present in the… See the full description on the dataset page: https://huggingface.co/datasets/LocalDoc/azerbaijani-ocr-benchmark. |
| [KunanonKhai/Synthetic-GOaT-OCR](https://huggingface.co/datasets/KunanonKhai/Synthetic-GOaT-OCR) | 2026-09-05 | text-recognition | candidate | — |
| [YortHurng/Shan_OCR_Dataset](https://huggingface.co/datasets/YortHurng/Shan_OCR_Dataset) | 2026-09-04 | text-recognition | candidate | — |
| [philippschulz/document-ocr-image-depth](https://huggingface.co/datasets/philippschulz/document-ocr-image-depth) | 2026-09-04 | text-recognition | candidate | 
	
		
	
	
		Document OCR Image Depth Data Notes
	


	
		
	
	
		Dataset summary
	

This data card accompanies a lightweight Document OCR loader for Image Depth metadata. It is meant for pipeline inspection, source adaptation, and reproducible split preparation.

	
		
	
	
		Included material
	


build_dataset.py — loading, cleaning, and split preparation code.
dataset_infos.json — schema and split metadata.
metadata_sample.jsonl — small, human-readable records for checking the schema.
README.md… See the full description on the dataset page: https://huggingface.co/datasets/philippschulz/document-ocr-image-depth. |
| [ivrit-ai/hebrew-handwriting-ocr-benchmark](https://huggingface.co/datasets/ivrit-ai/hebrew-handwriting-ocr-benchmark) | 2026-09-04 | handwriting-recognition, text-recognition | candidate | 
	
		
	
	
		Hebrew Handwriting OCR Benchmark
	

A small, human-verified benchmark for OCR / handwritten text recognition (HTR) on
modern Hebrew handwriting: 225 gold lines across 10 pages, one page per
writer, drawn from the transcriptor.ivrit.ai
volunteer transcription corpus.
This is a test set. There is no train split, by design — it exists to be held
out. It is deliberately small and clean rather than large and noisy: every line
was transcribed by at least two volunteers independently and… See the full description on the dataset page: https://huggingface.co/datasets/ivrit-ai/hebrew-handwriting-ocr-benchmark. |
| [tadad/kat57-ocr-bench-results](https://huggingface.co/datasets/tadad/kat57-ocr-bench-results) | 2026-09-03 | text-recognition | candidate | 
	
		
	
	
		Kat57 OCR smoke benchmark results
	

Exact ground-truth scoring for a 50-card Tesseract integration run over tadad/kat57-ground-truth-smoke. OCR outputs are published in the tesseract config of tadad/kat57-ocr-bench.

	
		
Model
CER
WER
Evaluated
Empty outputs
Error sentinels
Skipped references


		
Tesseract 5
0.4656
0.8605
50
1
0
0


	

The corpus totals are 4,629 character edits over 9,941 reference characters and 1,221 word edits over 1,419 reference words. Scoring used… See the full description on the dataset page: https://huggingface.co/datasets/tadad/kat57-ocr-bench-results. |
| [tadad/kat57-ocr-bench-500-results](https://huggingface.co/datasets/tadad/kat57-ocr-bench-500-results) | 2026-09-03 | text-recognition | candidate | 
	
		
	
	
		Kat57 OCR benchmark — CER/WER
	

Strict reference-based evaluation of 16 OCR models on a deterministic 500-card sample from Lund University Library's Kat57 catalogue-card collection. This result set contains only Character Error Rate (CER) and Word Error Rate (WER); it does not contain VLM judging or ELO ratings.
The sample was drawn with seed 57 from tadad/kat57-ground-truth and is published as tadad/kat57-ground-truth-500. The OCR outputs are retained in… See the full description on the dataset page: https://huggingface.co/datasets/tadad/kat57-ocr-bench-500-results. |
| [tadad/kat57-ocr-bench-500](https://huggingface.co/datasets/tadad/kat57-ocr-bench-500) | 2026-09-03 | text-recognition | candidate | 
	
		
	
	
		Kat57 OCR outputs
	

Raw outputs from 16 OCR models on the same deterministic 500-card sample of Lund University Library's Kat57 catalogue-card collection.
Each model is stored as a separate dataset configuration. Every configuration retains the source card identifiers, image, PAGE XML reference transcription, model output, and inference metadata so the results can be rescored without rerunning inference.

Source sample
CER/WER results and limitations
ocr-bench… See the full description on the dataset page: https://huggingface.co/datasets/tadad/kat57-ocr-bench-500. |
| [tadad/kat57-ocr-bench](https://huggingface.co/datasets/tadad/kat57-ocr-bench) | 2026-09-03 | text-recognition | candidate | 
	
		
	
	
		Document OCR using Tesseract
	

This dataset contains OCR results from images in tadad/kat57-ground-truth-smoke using Tesseract, the classical open-source CPU OCR engine — a cheap, no-GPU baseline alongside the VLM OCR recipes.

	
		
	
	
		Processing Details
	


Source Dataset: tadad/kat57-ground-truth-smoke
Engine: Tesseract 5.3.0
Language(s): eng
Number of Samples: 50
Processing Time: 1.1 min
Processing Date: 2026-09-03 18:39 UTC


	
		
	
	
		Configuration
	


Image Column: image… See the full description on the dataset page: https://huggingface.co/datasets/tadad/kat57-ocr-bench. |
| [sarmisarmitha/sinhala-handwritten-ocr-623](https://huggingface.co/datasets/sarmisarmitha/sinhala-handwritten-ocr-623) | 2026-09-03 | handwriting-recognition, text-recognition | candidate | — |
| [Raphael2099/oracle-ocr-project-backup-private](https://huggingface.co/datasets/Raphael2099/oracle-ocr-project-backup-private) | 2026-09-03 | text-recognition | candidate | 
	
		
	
	
		甲骨文 OCR：本机可读关键资产的部分备份
	

状态：部分备份；不是完整项目备份，不能据此删除整个源目录。

原目录：/Users/wyf/Desktop/AI4S 古文字/甲骨文OCR
生成时间：2026-09-03，Asia/Singapore。
压缩包：readable_critical_assets.tar.zst
包大小：4,127,757,967 字节。
内容：16,383 个文件或链接，归档源文件逻辑大小合计 4,421,632,250 字节。
压缩包 SHA-256：1fabb055bad4bc03b6ac3ed35eddb71438097bf7c06975885061a11ab2d9720e。
校验：独立解压数据流，逐文件比较大小和 SHA-256；链接比较目标；完整 zstd 数据流通过。
原件没有删除或覆盖。没有包含 macOS 扩展属性；不是完整的系统级恢复镜像。


	
		
	
	
		包含与缺失… See the full description on the dataset page: https://huggingface.co/datasets/Raphael2099/oracle-ocr-project-backup-private. |
| [OCR-Data/ocr_data](https://huggingface.co/datasets/OCR-Data/ocr_data) | 2026-09-03 | text-recognition | candidate | 
	
		
	
	
		ocr_data
	

Synthetic Arabic document images with layout annotations, for OCR training.

	
		
	
	
		Layout
	

WebDataset .tar shards. Files sharing a basename are one sample, so the
image becomes the image column and the annotation the json column.
data/<contributor>_<NNN>.tar            originals (PNG + JSON)
data_aug/<contributor>_<NNN>_aug<K>.tar augmented variants (JPEG/PNG + JSON)

Each shard holds up to 9990 samples (~1.2 GB). data/ and data_aug/
are separate so you can train… See the full description on the dataset page: https://huggingface.co/datasets/OCR-Data/ocr_data. |
| [beatsprom/multimodal-vision-ocr-document-parsing-2026](https://huggingface.co/datasets/beatsprom/multimodal-vision-ocr-document-parsing-2026) | 2026-09-03 | document-parsing, text-recognition | candidate | 
	
		
	
	
		📐 Multimodal Vision-Language & Industrial OCR Document Parsing SFT/DPO Suite (2026)
	





This repository provides the official 100-sample production teaser of the Multimodal Vision-Language & Industrial OCR Document Parsing SFT/DPO Suite (2026) by BeatsProm AI Research Lab.
The dataset is engineered to train open-weights Vision-Language Models (Qwen2-VL, Pixtral-12B, Llama-3.2-Vision, ColPali) on dense document parsing, normalized spatial bounding boxes (<box>[ymin, xmin, ymax… See the full description on the dataset page: https://huggingface.co/datasets/beatsprom/multimodal-vision-ocr-document-parsing-2026. |
| [TajikNLPWorld/tajik-ocr](https://huggingface.co/datasets/TajikNLPWorld/tajik-ocr) | 2026-09-02 | text-recognition | candidate | 
	
		
	
	
		Dataset Card for TajikOCR
	


	
		
	
	
		Dataset Details
	


	
		
	
	
		Dataset Description
	

TajikOCR is a synthetic dataset of page images containing texts in Tajik (Cyrillic script). The pages imitate old book leaves with classical poetry (Ferdowsi, Saadi, Rumi, Nizami, Bedil, Asadi, and others). Each page features various backgrounds (from plain white to aged paper with vignetting), borders, ornaments, and realistic defects (noise, blur, ink stains, folds, fiber texture). The… See the full description on the dataset page: https://huggingface.co/datasets/TajikNLPWorld/tajik-ocr. |
| [abzoo/arabic-names-synthetic-ocr](https://huggingface.co/datasets/abzoo/arabic-names-synthetic-ocr) | 2026-09-02 | text-recognition | candidate | — |
| [wuvictor/work-document-ocr](https://huggingface.co/datasets/wuvictor/work-document-ocr) | 2026-09-01 | text-recognition | candidate | 
	
		
	
	
		Document OCR Image Audio Data Notes
	


	
		
	
	
		Dataset summary
	

A documented Document OCR data-preparation workflow for Image Audio records. The bundled rows demonstrate the schema and validation path rather than pretending to be a full training corpus.

	
		
	
	
		Included material
	


build_dataset.py — loading, cleaning, and split preparation code.
dataset_infos.json — schema and split metadata.
metadata_sample.jsonl — small, human-readable records for checking the schema.… See the full description on the dataset page: https://huggingface.co/datasets/wuvictor/work-document-ocr. |
| [srilubis/document-ocr-corpus50-2023](https://huggingface.co/datasets/srilubis/document-ocr-corpus50-2023) | 2026-09-01 | text-recognition | candidate | 
	
		
	
	
		Document OCR Sensor Fusion Data Notes
	


	
		
	
	
		Dataset summary
	

This repository contains a preparation pipeline and a small metadata sample for Document OCR work with Sensor Fusion inputs. It does not claim to be a complete benchmark release; the loader documents how source data is normalized and validated.

	
		
	
	
		Included material
	


preprocess.py — loading, cleaning, and split preparation code.
dataset_infos.json — schema and split metadata.
metadata_sample.jsonl —… See the full description on the dataset page: https://huggingface.co/datasets/srilubis/document-ocr-corpus50-2023. |
| [Raphael2099/chujian-ocr-shiwen-20260901](https://huggingface.co/datasets/Raphael2099/chujian-ocr-shiwen-20260901) | 2026-09-01 | text-recognition | candidate | 
	
		
	
	
		OCR 释文三步流水线
	

本目录是 2026-09-01 正式释文 OCR 的本地交付根目录。
固定顺序：

百度 PaddleOCR-VL-1.5 保守首识；
Qwen3-VL-4B-Instruct 对照页图和百度结果复核；
GPT-5.6 只处理分歧、低置信和版式异常页，不对已一致页做语言润色。

字段分离保存：paddle_raw、qwen_review、gpt_review、accepted_text、review_status、source_sha256。古字图版、无码字和无法解释的分歧必须进入 quarantine，不得静默改成通顺文字。
资产详情、页数、SHA-256 与模型 revision 见 HF_ASSET_MANIFEST_20260901.json。
 |
| [ram-lexsi/curatorkit-testrun-OCR](https://huggingface.co/datasets/ram-lexsi/curatorkit-testrun-OCR) | 2026-09-01 | text-recognition | candidate | 
  
    
      
        
      
    
  



	
		
	
	
		curatorkit-testrun-OCR
	

Built using CuratorKIT — provenance-grounded curation and synthesis for LLM post-training.

	
		




		
Method
qa


Backend
litellm


Model
openai/Qwen/Qwen2.5-0.5B-Instruct


Formats
—


Artifact
dataset


Published
2026-09-01 06:26 UTC


	


	
		
	
	
		Usage
	

from datasets import load_dataset

ds = load_dataset("ram-lexsi/curatorkit-testrun-OCR")

 |
| [JustANormalTinkerer/animetext-ocr](https://huggingface.co/datasets/JustANormalTinkerer/animetext-ocr) | 2026-09-01 | text-recognition | candidate | — |
| [yadavrajesh/document-ocr-dataset96](https://huggingface.co/datasets/yadavrajesh/document-ocr-dataset96) | 2026-08-31 | text-recognition | candidate | 
	
		
	
	
		Document OCR Image Text Data Notes
	


	
		
	
	
		Dataset summary
	

Preparation notes and schema examples for Document OCR tasks using Image Text data. Full source material is intentionally not bundled, so provenance and licensing remain explicit.

	
		
	
	
		Included material
	


build_dataset.py — loading, cleaning, and split preparation code.
dataset_infos.json — schema and split metadata.
metadata_sample.jsonl — small, human-readable records for checking the schema.
README.md… See the full description on the dataset page: https://huggingface.co/datasets/yadavrajesh/document-ocr-dataset96. |
| [SeeWye/NFA_OCR_qwen_sft_format_test6](https://huggingface.co/datasets/SeeWye/NFA_OCR_qwen_sft_format_test6) | 2026-08-31 | text-recognition | candidate | — |
| [large-language-leonid/e_cup_2026_ocr](https://huggingface.co/datasets/large-language-leonid/e_cup_2026_ocr) | 2026-08-31 | text-recognition | candidate | — |
| [kreativetimebox/ktb-ocr-dataset](https://huggingface.co/datasets/kreativetimebox/ktb-ocr-dataset) | 2026-08-31 | text-recognition | candidate | — |
| [infokreativetimebox/ktb-ocr-dataset](https://huggingface.co/datasets/infokreativetimebox/ktb-ocr-dataset) | 2026-08-31 | text-recognition | candidate | 
	
		
	
	
		PDFA OCR Dataset
	

Curated and Published by KREATIVE TIME BOX
This dataset contains document page images along with their corresponding OCR layout bounding box annotations derived from PDFA document extraction pipelines.


	
		
	
	
		Dataset Overview
	


Organization / Creator: KREATIVE TIME BOX
Total Images: 42,627 PNG files (~19 GB)
Total JSON Annotations: 42,628 JSON files (~322 MB)
Image Format: PNG (RGB document page renders)
Annotation Format: JSON with text lines… See the full description on the dataset page: https://huggingface.co/datasets/infokreativetimebox/ktb-ocr-dataset. |
| [elliot-mllm/tal_ocr_eng_cleaned](https://huggingface.co/datasets/elliot-mllm/tal_ocr_eng_cleaned) | 2026-08-31 | text-recognition | candidate | 
	
		
	
	
		tal_ocr_eng_cleaned
	

The tal_ocr_eng__x family of the ElliotVL supervised-fine-tuning pool, after VLM cleaning.

	
		




		
images
231,524


QA turns
581,960


answers rewritten by the cleaning pass
111,158


QA created by the cleaning pass (new_qa)
352,691 (60.6%)


shards
9


	


	
		
	
	
		How this was cleaned
	

A vision-language model read each image together with its QA and judged the item. The pass is
not a filter that only removes rows — it rewrites answers it finds… See the full description on the dataset page: https://huggingface.co/datasets/elliot-mllm/tal_ocr_eng_cleaned. |
| [elliot-mllm/OCRVQA_RS_think](https://huggingface.co/datasets/elliot-mllm/OCRVQA_RS_think) | 2026-08-31 | text-recognition | candidate | — |
| [elliot-mllm/OCRVQA_rejected](https://huggingface.co/datasets/elliot-mllm/OCRVQA_rejected) | 2026-08-31 | text-recognition | candidate | — |
| [elliot-mllm/OCRVQA_longform](https://huggingface.co/datasets/elliot-mllm/OCRVQA_longform) | 2026-08-31 | text-recognition | candidate | — |
| [elliot-mllm/ocr_cleaned](https://huggingface.co/datasets/elliot-mllm/ocr_cleaned) | 2026-08-31 | text-recognition | candidate | 
	
		
	
	
		ocr_cleaned
	

The ocr__x family of the ElliotVL supervised-fine-tuning pool, after VLM cleaning.

	
		




		
images
234,142


QA turns
1,232,495


answers rewritten by the cleaning pass
0


QA created by the cleaning pass (new_qa)
not measured for this family


shards
172


	


	
		
	
	
		How this was cleaned
	

A vision-language model read each image together with its QA and judged the item. The pass is
not a filter that only removes rows — it rewrites answers it finds wrong but… See the full description on the dataset page: https://huggingface.co/datasets/elliot-mllm/ocr_cleaned. |
| [tetrak/armenian-ocr-crops](https://huggingface.co/datasets/tetrak/armenian-ocr-crops) | 2026-08-30 | text-recognition | candidate | 
	
		
	
	
		Tetrak Armenian OCR crops
	

Training data for tetrak_hy, the Armenian text recogniser we are
building as an EasyOCR custom model in
tetrak-hy-trainer
for Tetrak, an OCR pipeline for community
archives.
The dataset has two configurations:

corpus — 1,190 proofread pages of the Armenian Soviet
Encyclopedia, as plain text with full Wikisource provenance.
crops — the v0 synthetic pre-training set: 181,800 rendered
word crops with transcriptions.


	
		
	
	
		The corpus configuration… See the full description on the dataset page: https://huggingface.co/datasets/tetrak/armenian-ocr-crops. |
| [Reza2kn/persian-ocr-gemini37-wins-bina-misses-viewer](https://huggingface.co/datasets/Reza2kn/persian-ocr-gemini37-wins-bina-misses-viewer) | 2026-08-30 | text-recognition | candidate | 
	
		
	
	
		Gemini 3.7 exact / Bina miss OCR crops
	

53 non-empty bbox crops from the PersianVLM submitted-10 benchmark where
google/gemini-3.7-flash was normalized-exact and Bina Koochik 0.1 was not.
This is a minimal Hugging Face ImageFolder dataset for reliable viewer support.
It contains exactly two columns: image and ocr. The ocr value is Gemini's
actual output for the corresponding crop.
 |
| [Reza2kn/persian-ocr-gemini37-wins-bina-misses-v2](https://huggingface.co/datasets/Reza2kn/persian-ocr-gemini37-wins-bina-misses-v2) | 2026-08-30 | text-recognition | candidate | 
	
		
	
	
		Gemini 3.7 exact / Bina miss OCR crops
	

53 non-empty bbox crops from the PersianVLM submitted-10 benchmark where
google/gemini-3.7-flash produced a normalized-exact transcription and
Bina Koochik 0.1 did not.
This release uses the standard Hugging Face ImageFolder layout. The viewer's
first column is image, followed by ocr containing Gemini's actual output.
Gold and Bina outputs are retained for comparison.
 |
| [Reza2kn/persian-ocr-gemini37-wins-bina-misses-parquet](https://huggingface.co/datasets/Reza2kn/persian-ocr-gemini37-wins-bina-misses-parquet) | 2026-08-30 | text-recognition | candidate | 
	
		
	
	
		Gemini 3.7 exact / Bina miss OCR crops
	

53 bbox crops. Columns: image and ocr.
 |
| [Reza2kn/persian-ocr-gemini37-wins-bina-misses](https://huggingface.co/datasets/Reza2kn/persian-ocr-gemini37-wins-bina-misses) | 2026-08-30 | text-recognition | candidate | 
	
		
	
	
		Gemini 3.7 vs Bina OCR comparison crops
	

53 non-empty bbox crops where Gemini 3.7 Flash was normalized-exact and Bina
Koochik 0.1 was not. The first columns are image, gemini_ocr, bina_ocr,
and gold_text for direct visual and OCR comparison.
 |
| [Raphael2099/chujian-ocr-sources](https://huggingface.co/datasets/Raphael2099/chujian-ocr-sources) | 2026-08-30 | text-recognition | candidate | — |
| [Formian/ocra-v2.1](https://huggingface.co/datasets/Formian/ocra-v2.1) | 2026-08-30 | text-recognition | candidate | 
	
		
	
	
		O-CRA Model Disposition Scores (V2.1)
	

Organizational Cognitive Resonance & Alignment (O-CRA) is a framework for measuring the disposition of AI language models — not their benchmark performance, but their underlying behavioural tendencies across six dimensions that determine how they fit into organisations and workflows.
This dataset contains disposition scores for 135 models from 29 labs, tested under the V2.1 protocol across 203+ scenarios. It is the current public reference… See the full description on the dataset page: https://huggingface.co/datasets/Formian/ocra-v2.1. |
| [Formian-Labs/ocra-v2.1](https://huggingface.co/datasets/Formian-Labs/ocra-v2.1) | 2026-08-30 | text-recognition | candidate | 
	
		
	
	
		Which AI Model Fits Your Organisation?
	

Disposition scores for 135 AI language models from 29 labs — O-CRA V2.1
Organizational Cognitive Resonance & Alignment (O-CRA) is a framework for measuring the disposition of AI language models — not their benchmark performance, but their underlying behavioural tendencies across six dimensions that determine how they fit into organisations and workflows.
This dataset contains disposition scores for 135 models from 29 labs, tested under the… See the full description on the dataset page: https://huggingface.co/datasets/Formian-Labs/ocra-v2.1. |
| [Emulated-Inc/captcha-ocr-verifier](https://huggingface.co/datasets/Emulated-Inc/captcha-ocr-verifier) | 2026-08-30 | text-recognition | candidate | — |
| [elliot-mllm/ureader_ocr_cleaned](https://huggingface.co/datasets/elliot-mllm/ureader_ocr_cleaned) | 2026-08-30 | text-recognition | candidate | 
	
		
	
	
		ureader_ocr_cleaned
	

The ureader_ocr__x family of the ElliotVL supervised-fine-tuning pool, after VLM cleaning.

	
		




		
images
862


QA turns
6,038


answers rewritten by the cleaning pass
403


QA created by the cleaning pass (new_qa)
3,952 (65.5%)


shards
1


	


	
		
	
	
		How this was cleaned
	

A vision-language model read each image together with its QA and judged the item. The pass is
not a filter that only removes rows — it rewrites answers it finds wrong but… See the full description on the dataset page: https://huggingface.co/datasets/elliot-mllm/ureader_ocr_cleaned. |
| [elliot-mllm/OCRVQA_RS_nothink](https://huggingface.co/datasets/elliot-mllm/OCRVQA_RS_nothink) | 2026-08-30 | text-recognition | candidate | 
	
		
	
	
		OCRVQA — OCRVQA_RS_nothink
	

Rejection-sampled from the OCRVQA train split. This split holds the accepted items, answer only.

	
		




		
rows
450,389


QA pairs
1,298,217


shards
1959


accepted / rejected (whole family)
1,298,217 / 794,326


accept rate
62.0%


verifier
anls


	


	
		
	
	
		How the data was produced
	

A VLM answers every question at temperature 0 with reasoning enabled. Its answer is compared with
the official ground truth by the verifier described below;… See the full description on the dataset page: https://huggingface.co/datasets/elliot-mllm/OCRVQA_RS_nothink. |
| [elliot-mllm/latex_ocr_cleaned](https://huggingface.co/datasets/elliot-mllm/latex_ocr_cleaned) | 2026-08-30 | text-recognition | candidate | 
	
		
	
	
		latex_ocr_cleaned
	

The latex_ocr__x family of the ElliotVL supervised-fine-tuning pool, after VLM cleaning.

	
		




		
images
72,345


QA turns
132,970


answers rewritten by the cleaning pass
7,072


QA created by the cleaning pass (new_qa)
66,310 (49.9%)


shards
1


	


	
		
	
	
		How this was cleaned
	

A vision-language model read each image together with its QA and judged the item. The pass is
not a filter that only removes rows — it rewrites answers it finds wrong but… See the full description on the dataset page: https://huggingface.co/datasets/elliot-mllm/latex_ocr_cleaned. |
| [elliot-mllm/invoices-and-receipts_ocr_cleaned](https://huggingface.co/datasets/elliot-mllm/invoices-and-receipts_ocr_cleaned) | 2026-08-30 | text-recognition | candidate | 
	
		
	
	
		invoices-and-receipts_ocr_cleaned
	

The invoices-and-receipts_ocr__x family of the ElliotVL supervised-fine-tuning pool, after VLM cleaning.

	
		




		
images
2,221


QA turns
7,696


answers rewritten by the cleaning pass
1,517


QA created by the cleaning pass (new_qa)
4,651 (60.4%)


shards
4


	


	
		
	
	
		How this was cleaned
	

A vision-language model read each image together with its QA and judged the item. The pass is
not a filter that only removes rows — it rewrites… See the full description on the dataset page: https://huggingface.co/datasets/elliot-mllm/invoices-and-receipts_ocr_cleaned. |
| [abzoo/egyptian-id-ocr](https://huggingface.co/datasets/abzoo/egyptian-id-ocr) | 2026-08-30 | text-recognition | candidate | — |
| [a7x3a/qai-ocr-v1-small](https://huggingface.co/datasets/a7x3a/qai-ocr-v1-small) | 2026-08-30 | text-recognition | candidate | 
	
		
	
	
		QAI OCR v1 Small
	

OCR image-text dataset stored as WebDataset TAR shards.

	
		
	
	
		Dataset structure
	

train/
val/
test/
Each split contains TAR shards and metadata.jsonl.

	
		
	
	
		Sample structure
	

Each OCR sample contains two files with the SAME key:
000000000000.jpg
000000000000.txt
The TXT file contains only the OCR transcription.
Labels are stored as UTF-8 text.
Original metadata is preserved in metadata.jsonl.

	
		
	
	
		Splits
	

train - training data
val -… See the full description on the dataset page: https://huggingface.co/datasets/a7x3a/qai-ocr-v1-small. |
| [SeeWye/NFA_OCR_reinforcement_learning_format_TEST6](https://huggingface.co/datasets/SeeWye/NFA_OCR_reinforcement_learning_format_TEST6) | 2026-08-29 | text-recognition | candidate | — |
| [SeeWye/NFA_OCR_reinforcement_learning_format_TEST5](https://huggingface.co/datasets/SeeWye/NFA_OCR_reinforcement_learning_format_TEST5) | 2026-08-29 | text-recognition | candidate | — |
| [SeeWye/NFA_OCR_reinforcement_learning_format_TEST4](https://huggingface.co/datasets/SeeWye/NFA_OCR_reinforcement_learning_format_TEST4) | 2026-08-28 | text-recognition | candidate | — |
| [Reza2kn/persian-ocr-bench-submitted10-bbox-crops](https://huggingface.co/datasets/Reza2kn/persian-ocr-bench-submitted10-bbox-crops) | 2026-08-28 | text-recognition | candidate | 
	
		
	
	
		Persian OCR benchmark — selected submitted bbox crops
	

This dataset contains the non-empty OCR bboxes from the ten explicitly selected
submitted pages in persian_ocr_bench_bbox_review.
Each row is one PNG crop. gold_text is the current editable OCR content from
the live Argilla bbox field (content_text). Geometry is stored both as source
page pixels and as percentages of the source page. The original record ID,
external ID, bbox ID, source URL, and SHA-256 hashes are included for… See the full description on the dataset page: https://huggingface.co/datasets/Reza2kn/persian-ocr-bench-submitted10-bbox-crops. |
| [Reza2kn/persian-ocr-bench-submitted10-additional4-results](https://huggingface.co/datasets/Reza2kn/persian-ocr-bench-submitted10-additional4-results) | 2026-08-28 | text-recognition | candidate | 
	
		
	
	
		Persian OCR benchmark
	

This run evaluates 4 vision OCR lanes over 193 bbox crops from Reza2kn/persian-ocr-bench-submitted10-bbox-crops.
Each row in results.jsonl preserves the crop identity and current gold content_text, then records the model output, latency, usage, provider hint, HTTP status, and normalized OCR metrics. Failures are retained.
OpenRouter constraints: Grok uses xai/zdr, GPT uses openai, GLM uses baseten/fp8, Gemma 4 26B uses cloudflare, and Gemma 4 31B uses… See the full description on the dataset page: https://huggingface.co/datasets/Reza2kn/persian-ocr-bench-submitted10-additional4-results. |
| [pan-dece/document-ocr-image-text-v2-2024](https://huggingface.co/datasets/pan-dece/document-ocr-image-text-v2-2024) | 2026-08-28 | text-recognition | candidate | 
	
		
	
	
		Document OCR Image Text Data Notes
	


	
		
	
	
		Dataset summary
	

Preparation notes and schema examples for Document OCR tasks using Image Text data. Full source material is intentionally not bundled, so provenance and licensing remain explicit.

	
		
	
	
		Included material
	


load_data.py — loading, cleaning, and split preparation code.
dataset_infos.json — schema and split metadata.
metadata_sample.jsonl — small, human-readable records for checking the schema.
README.md —… See the full description on the dataset page: https://huggingface.co/datasets/pan-dece/document-ocr-image-text-v2-2024. |
| [kkumarmanoj/document-ocr-pointcloud-text-clean](https://huggingface.co/datasets/kkumarmanoj/document-ocr-pointcloud-text-clean) | 2026-08-28 | text-recognition | candidate | 
	
		
	
	
		Document OCR Pointcloud Text Data Notes
	


	
		
	
	
		Dataset summary
	

This data card accompanies a lightweight Document OCR loader for Pointcloud Text metadata. It is meant for pipeline inspection, source adaptation, and reproducible split preparation.

	
		
	
	
		Included material
	


preprocess.py — loading, cleaning, and split preparation code.
dataset_infos.json — schema and split metadata.
metadata_sample.jsonl — small, human-readable records for checking the schema.… See the full description on the dataset page: https://huggingface.co/datasets/kkumarmanoj/document-ocr-pointcloud-text-clean. |
| [Jes-cott/document-ocr-data](https://huggingface.co/datasets/Jes-cott/document-ocr-data) | 2026-08-28 | text-recognition | candidate | 
	
		
	
	
		Document OCR Image Audio Data Notes
	


	
		
	
	
		Dataset summary
	

Preparation notes and schema examples for Document OCR tasks using Image Audio data. Full source material is intentionally not bundled, so provenance and licensing remain explicit.

	
		
	
	
		Included material
	


clean.py — loading, cleaning, and split preparation code.
dataset_infos.json — schema and split metadata.
metadata_sample.jsonl — small, human-readable records for checking the schema.
README.md — data… See the full description on the dataset page: https://huggingface.co/datasets/Jes-cott/document-ocr-data. |
| [hsbharadwaj/ocr_datasets](https://huggingface.co/datasets/hsbharadwaj/ocr_datasets) | 2026-08-28 | handwriting-recognition, text-recognition | candidate | 
	
		
	
	
		Combined OCR Dataset for Text Recognition
	


	
		
	
	
		Dataset Description
	

This is a large-scale dataset (~11M training, ~0.9M validation images) for Optical Character Recognition (OCR), aggregated from several common benchmarks and sources (see Sources below). It includes scene text, handwritten text, and synthetic images with corresponding text labels.
Training Code: https://github.com/ducto489/lib_ocr

	
		
	
	
		Dataset Structure
	

./data/
├── train/
│   ├── images/*.jpg… See the full description on the dataset page: https://huggingface.co/datasets/hsbharadwaj/ocr_datasets. |
| [davanstrien/moh-ocr-sample-20](https://huggingface.co/datasets/davanstrien/moh-ocr-sample-20) | 2026-08-28 | text-recognition | candidate | — |
| [darrenten/assignment-document-ocr40](https://huggingface.co/datasets/darrenten/assignment-document-ocr40) | 2026-08-28 | text-recognition | candidate | 
	
		
	
	
		Document OCR Sensor Fusion Data Notes
	


	
		
	
	
		Dataset summary
	

This data card accompanies a lightweight Document OCR loader for Sensor Fusion metadata. It is meant for pipeline inspection, source adaptation, and reproducible split preparation.

	
		
	
	
		Included material
	


prepare.py — loading, cleaning, and split preparation code.
dataset_infos.json — schema and split metadata.
metadata_sample.jsonl — small, human-readable records for checking the schema.
README.md —… See the full description on the dataset page: https://huggingface.co/datasets/darrenten/assignment-document-ocr40. |
| [alphabot2/28_Aug_OCR_Bimanual_Niranjan](https://huggingface.co/datasets/alphabot2/28_Aug_OCR_Bimanual_Niranjan) | 2026-08-28 | text-recognition | candidate | This dataset was created using LeRobot.







	
		
	
	
		Dataset Structure
	

meta/info.json:
{
    "codebase_version": "v3.0",
    "robot_type": "aibot2",
    "total_episodes": 35,
    "total_frames": 16309,
    "total_tasks": 1,
    "chunks_size": 1000,
    "data_files_size_in_mb": 100,
    "video_files_size_in_mb": 200,
    "fps": 10,
    "splits": {
        "train": "0:35"
    },
    "data_path": "data/chunk-{chunk_index:03d}/file-{file_index:03d}.parquet",
    "video_path":… See the full description on the dataset page: https://huggingface.co/datasets/alphabot2/28_Aug_OCR_Bimanual_Niranjan. |
| [Takumiabe0213/document-ocr-pointcloud-text](https://huggingface.co/datasets/Takumiabe0213/document-ocr-pointcloud-text) | 2026-08-27 | text-recognition | candidate | 
	
		
	
	
		Document OCR Pointcloud Text Data Notes
	


	
		
	
	
		Dataset summary
	

A documented Document OCR data-preparation workflow for Pointcloud Text records. The bundled rows demonstrate the schema and validation path rather than pretending to be a full training corpus.

	
		
	
	
		Included material
	


clean.py — loading, cleaning, and split preparation code.
dataset_infos.json — schema and split metadata.
metadata_sample.jsonl — small, human-readable records for checking the schema.… See the full description on the dataset page: https://huggingface.co/datasets/Takumiabe0213/document-ocr-pointcloud-text. |
| [phamrita/study-document-ocr](https://huggingface.co/datasets/phamrita/study-document-ocr) | 2026-08-27 | text-recognition | candidate | 
	
		
	
	
		Document OCR Text Tabular Data Notes
	


	
		
	
	
		Dataset summary
	

Preparation notes and schema examples for Document OCR tasks using Text Tabular data. Full source material is intentionally not bundled, so provenance and licensing remain explicit.

	
		
	
	
		Included material
	


dataset.py — loading, cleaning, and split preparation code.
dataset_infos.json — schema and split metadata.
metadata_sample.jsonl — small, human-readable records for checking the schema.
README.md —… See the full description on the dataset page: https://huggingface.co/datasets/phamrita/study-document-ocr. |
| [OCR-Data/ocr_dataset](https://huggingface.co/datasets/OCR-Data/ocr_dataset) | 2026-08-27 | text-recognition | candidate | — |
| [EDWINSANTOSO/document-ocr-pointcloud-text-benchmark](https://huggingface.co/datasets/EDWINSANTOSO/document-ocr-pointcloud-text-benchmark) | 2026-08-27 | text-recognition | candidate | 
	
		
	
	
		Document OCR Pointcloud Text Data Notes
	


	
		
	
	
		Dataset summary
	

A documented Document OCR data-preparation workflow for Pointcloud Text records. The bundled rows demonstrate the schema and validation path rather than pretending to be a full training corpus.

	
		
	
	
		Included material
	


dataset.py — loading, cleaning, and split preparation code.
dataset_infos.json — schema and split metadata.
metadata_sample.jsonl — small, human-readable records for checking the… See the full description on the dataset page: https://huggingface.co/datasets/EDWINSANTOSO/document-ocr-pointcloud-text-benchmark. |
| [christopherxzyx/ocr_financials_statements_2020_2025](https://huggingface.co/datasets/christopherxzyx/ocr_financials_statements_2020_2025) | 2026-08-27 | text-recognition | candidate | 
	
		
	
	
		📋 Vietnam Annual Financial Statements (2020–2025) (PDF & OCR)
	


	
		
	
	
		📌 Overview
	

OCR Vietnam Annual Financial Statements (2020–2025) là bộ dữ liệu báo cáo tài chính thường niên của các doanh nghiệp niêm yết tại Việt Nam. Đây là phiên bản được chọn lọc và tinh chỉnh từ bộ dữ liệu gốc TiniX Vietnam OCR Annual Financial Statements do TiniX AI thu thập.
Điểm khác biệt của bộ dữ liệu này:

Tập trung chuyên sâu vào giai đoạn mới nhất: 2020–2025.
Cung cấp song song cả định… See the full description on the dataset page: https://huggingface.co/datasets/christopherxzyx/ocr_financials_statements_2020_2025. |
| [alphabot2/Aibot2_27Aug_STEA_Pick_OCR](https://huggingface.co/datasets/alphabot2/Aibot2_27Aug_STEA_Pick_OCR) | 2026-08-27 | text-recognition | candidate | This dataset was created using LeRobot.







	
		
	
	
		Dataset Structure
	

meta/info.json:
{
    "codebase_version": "v3.0",
    "robot_type": "aibot2",
    "total_episodes": 10,
    "total_frames": 3891,
    "total_tasks": 1,
    "chunks_size": 1000,
    "data_files_size_in_mb": 100,
    "video_files_size_in_mb": 200,
    "fps": 10,
    "splits": {
        "train": "0:10"
    },
    "data_path": "data/chunk-{chunk_index:03d}/file-{file_index:03d}.parquet",
    "video_path":… See the full description on the dataset page: https://huggingface.co/datasets/alphabot2/Aibot2_27Aug_STEA_Pick_OCR. |
| [minh2128/colab-paddle-env-for-ocr](https://huggingface.co/datasets/minh2128/colab-paddle-env-for-ocr) | 2026-08-26 | text-recognition | candidate | — |
| [MingxuChai/SCVER-fr-ocr](https://huggingface.co/datasets/MingxuChai/SCVER-fr-ocr) | 2026-08-26 | text-recognition | candidate | — |
| [kailasa-ngpt/gemini-3.7-flash-ocr-26-aug-2026](https://huggingface.co/datasets/kailasa-ngpt/gemini-3.7-flash-ocr-26-aug-2026) | 2026-08-26 | text-recognition | candidate | 
	
		
	
	
		gemini-3.7-flash-ocr-26-aug-2026
	

Page-image → transcription pairs for finetuning a vision-language model to OCR
Devanagari and Tamil printed books.
These labels are not human ground truth. They are the output of a teacher
model, so its accuracy is the ceiling for anything trained on them.

	
		
	
	
		Provenance
	


	
		




		
Teacher model
google/gemini-3.7-flash (via OpenRouter, reasoning.effort=low)


Page render
PyMuPDF at 200 DPI, grayscale JPEG q90


Sampling
stratified —… See the full description on the dataset page: https://huggingface.co/datasets/kailasa-ngpt/gemini-3.7-flash-ocr-26-aug-2026. |
| [Darmm/darmm-ocr-kazakh-v2](https://huggingface.co/datasets/Darmm/darmm-ocr-kazakh-v2) | 2026-08-26 | text-recognition | candidate | 
	
		
	
	
		Darmm Kazakh OCR v2
	

Synthetic OCR dataset for printed Kazakh (Cyrillic script), built to train and evaluate models on realistic document conditions — scans, photos, and degraded print — not just clean renders. It supersedes Darmm/darmm-ocr-kazakh-cyrillic, which it fully includes as its clean tier.
Full coverage of the Kazakh-specific letters: Ә Ғ Қ Ң Ө Ұ Ү Һ І (all 17 fonts used were verified to render them).

	
		
	
	
		Tiers
	


	
		
tier
level
what it is


		
clean
word… See the full description on the dataset page: https://huggingface.co/datasets/Darmm/darmm-ocr-kazakh-v2. |
| [ankitamam/document-ocr-video-text-mini](https://huggingface.co/datasets/ankitamam/document-ocr-video-text-mini) | 2026-08-26 | text-recognition | candidate | 
	
		
	
	
		Document OCR Video Text Data Notes
	


	
		
	
	
		Dataset summary
	

This data card accompanies a lightweight Document OCR loader for Video Text metadata. It is meant for pipeline inspection, source adaptation, and reproducible split preparation.

	
		
	
	
		Included material
	


preprocess.py — loading, cleaning, and split preparation code.
dataset_infos.json — schema and split metadata.
metadata_sample.jsonl — small, human-readable records for checking the schema.
README.md —… See the full description on the dataset page: https://huggingface.co/datasets/ankitamam/document-ocr-video-text-mini. |
| [srmistbiolab/ocr-lab56](https://huggingface.co/datasets/srmistbiolab/ocr-lab56) | 2026-08-25 | text-recognition | candidate | 
	
		
	
	
		dataloader.py
	


	
		
	
	
		Dataset Summary
	

A education dataset with image text modality, stored in npy sharded format.

	
		
	
	
		Preprocessing & Augmentation
	


Preprocessing: adaptive
Augmentation: light


	
		
	
	
		Splits & Sampling
	


Split strategy: random 90 10
Sampling: curriculum


	
		
	
	
		Quality & Labeling
	


Quality filtering: lenient
Labeling: pseudo label


	
		
	
	
		Files
	


dataloader.py — main artifact of this repository


	
		
	
	
		License
	

See… See the full description on the dataset page: https://huggingface.co/datasets/srmistbiolab/ocr-lab56. |
| [OCR-Data/datatest_nihal](https://huggingface.co/datasets/OCR-Data/datatest_nihal) | 2026-08-25 | text-recognition | candidate | — |
| [michalkowalski/llm-ocr-lite91](https://huggingface.co/datasets/michalkowalski/llm-ocr-lite91) | 2026-08-25 | text-recognition | candidate | 
	
		
	
	
		prepare.py
	


	
		
	
	
		Dataset Summary
	

A security dataset with pointcloud text modality, stored in lmdb format.

	
		
	
	
		Preprocessing & Augmentation
	


Preprocessing: progressive
Augmentation: heavy


	
		
	
	
		Splits & Sampling
	


Split strategy: temporal
Sampling: contrastive


	
		
	
	
		Quality & Labeling
	


Quality filtering: lenient
Labeling: pseudo label


	
		
	
	
		Files
	


prepare.py — main artifact of this repository


	
		
	
	
		License
	

See the license… See the full description on the dataset page: https://huggingface.co/datasets/michalkowalski/llm-ocr-lite91. |
| [lucasvandijk/roberta-ocr](https://huggingface.co/datasets/lucasvandijk/roberta-ocr) | 2026-08-25 | text-recognition | candidate | 
	
		
	
	
		build_dataset.py
	


	
		
	
	
		Dataset Summary
	

A wildlife dataset with video text modality, stored in hdf5 format.

	
		
	
	
		Preprocessing & Augmentation
	


Preprocessing: adaptive
Augmentation: mixup cutmix


	
		
	
	
		Splits & Sampling
	


Split strategy: random 90 10
Sampling: curriculum


	
		
	
	
		Quality & Labeling
	


Quality filtering: moderate
Labeling: pseudo label


	
		
	
	
		Files
	


build_dataset.py — main artifact of this repository


	
		
	
	
		License… See the full description on the dataset page: https://huggingface.co/datasets/lucasvandijk/roberta-ocr. |
| [kaylaedwa/ocr-lite](https://huggingface.co/datasets/kaylaedwa/ocr-lite) | 2026-08-25 | text-recognition | candidate | 
	
		
	
	
		prepare.py
	


	
		
	
	
		Dataset Summary
	

A memes dataset with image depth modality, stored in csv format.

	
		
	
	
		Preprocessing & Augmentation
	


Preprocessing: standard
Augmentation: light


	
		
	
	
		Splits & Sampling
	


Split strategy: temporal
Sampling: stratified


	
		
	
	
		Quality & Labeling
	


Quality filtering: adaptive
Labeling: weak supervision


	
		
	
	
		Files
	


prepare.py — main artifact of this repository


	
		
	
	
		License
	

See the license field… See the full description on the dataset page: https://huggingface.co/datasets/kaylaedwa/ocr-lite. |
| [kaizhangana/ocr](https://huggingface.co/datasets/kaizhangana/ocr) | 2026-08-25 | text-recognition | candidate | 
	
		
	
	
		loader.py
	


	
		
	
	
		Dataset Summary
	

A movie posters dataset with image depth modality, stored in huggingface format.

	
		
	
	
		Preprocessing & Augmentation
	


Preprocessing: minimal
Augmentation: none


	
		
	
	
		Splits & Sampling
	


Split strategy: temporal
Sampling: active


	
		
	
	
		Quality & Labeling
	


Quality filtering: strict
Labeling: manual


	
		
	
	
		Files
	


loader.py — main artifact of this repository


	
		
	
	
		License
	

See the license field… See the full description on the dataset page: https://huggingface.co/datasets/kaizhangana/ocr. |
| [Jiangnan-genomics1/ocr-playground](https://huggingface.co/datasets/Jiangnan-genomics1/ocr-playground) | 2026-08-25 | text-recognition | candidate | 
	
		
	
	
		clean.py
	


	
		
	
	
		Dataset Summary
	

A finance dataset with pointcloud text modality, stored in lmdb format.

	
		
	
	
		Preprocessing & Augmentation
	


Preprocessing: minimal
Augmentation: mixup cutmix


	
		
	
	
		Splits & Sampling
	


Split strategy: random 90 10
Sampling: hard negative


	
		
	
	
		Quality & Labeling
	


Quality filtering: lenient
Labeling: pseudo label


	
		
	
	
		Files
	


clean.py — main artifact of this repository


	
		
	
	
		License
	

See the… See the full description on the dataset page: https://huggingface.co/datasets/Jiangnan-genomics1/ocr-playground. |
| [dijohnson/ocr-v2](https://huggingface.co/datasets/dijohnson/ocr-v2) | 2026-08-25 | text-recognition | candidate | 
	
		
	
	
		clean.py
	


	
		
	
	
		Dataset Summary
	

A speech dataset with image audio modality, stored in lmdb format.

	
		
	
	
		Preprocessing & Augmentation
	


Preprocessing: adaptive
Augmentation: none


	
		
	
	
		Splits & Sampling
	


Split strategy: stratified 90 10
Sampling: contrastive


	
		
	
	
		Quality & Labeling
	


Quality filtering: strict
Labeling: manual


	
		
	
	
		Files
	


clean.py — main artifact of this repository


	
		
	
	
		License
	

See the license field above.
 |
| [Blrmehta01/ocr-playground](https://huggingface.co/datasets/Blrmehta01/ocr-playground) | 2026-08-25 | text-recognition | candidate | 
	
		
	
	
		build_dataset.py
	


	
		
	
	
		Dataset Summary
	

A robotics dataset with pointcloud text modality, stored in parquet format.

	
		
	
	
		Preprocessing & Augmentation
	


Preprocessing: curriculum
Augmentation: none


	
		
	
	
		Splits & Sampling
	


Split strategy: temporal
Sampling: hard negative


	
		
	
	
		Quality & Labeling
	


Quality filtering: moderate
Labeling: pseudo label


	
		
	
	
		Files
	


build_dataset.py — main artifact of this repository


	
		
	
	
		License… See the full description on the dataset page: https://huggingface.co/datasets/Blrmehta01/ocr-playground. |
| [amitiyerpaw/ocr-tryout](https://huggingface.co/datasets/amitiyerpaw/ocr-tryout) | 2026-08-25 | text-recognition | candidate | 
	
		
	
	
		prepare.py
	


	
		
	
	
		Dataset Summary
	

A traffic dataset with text tabular modality, stored in webdataset format.

	
		
	
	
		Preprocessing & Augmentation
	


Preprocessing: progressive
Augmentation: heavy


	
		
	
	
		Splits & Sampling
	


Split strategy: temporal
Sampling: balanced


	
		
	
	
		Quality & Labeling
	


Quality filtering: moderate
Labeling: weak supervision


	
		
	
	
		Files
	


prepare.py — main artifact of this repository


	
		
	
	
		License
	

See the… See the full description on the dataset page: https://huggingface.co/datasets/amitiyerpaw/ocr-tryout. |
| [Aleksanderszyma/gpt2-ocr-v2](https://huggingface.co/datasets/Aleksanderszyma/gpt2-ocr-v2) | 2026-08-25 | text-recognition | candidate | 
	
		
	
	
		preprocess.py
	


	
		
	
	
		Dataset Summary
	

A news media dataset with audio text modality, stored in webdataset format.

	
		
	
	
		Preprocessing & Augmentation
	


Preprocessing: standard
Augmentation: heavy


	
		
	
	
		Splits & Sampling
	


Split strategy: kfold 5
Sampling: hard negative


	
		
	
	
		Quality & Labeling
	


Quality filtering: strict
Labeling: self training


	
		
	
	
		Files
	


preprocess.py — main artifact of this repository


	
		
	
	
		License
	

See the… See the full description on the dataset page: https://huggingface.co/datasets/Aleksanderszyma/gpt2-ocr-v2. |
| [Hisham20/ocr-bundles](https://huggingface.co/datasets/Hisham20/ocr-bundles) | 2026-08-24 | text-recognition | candidate | — |
| [elichen-skymizer/GAP-ocrbench-v2](https://huggingface.co/datasets/elichen-skymizer/GAP-ocrbench-v2) | 2026-08-24 | text-recognition | candidate | — |
| [elichen-skymizer/GAP-ocrbench-v1](https://huggingface.co/datasets/elichen-skymizer/GAP-ocrbench-v1) | 2026-08-24 | text-recognition | candidate | — |
| [context212/context212-alhazen-ocr-khattmix](https://huggingface.co/datasets/context212/context212-alhazen-ocr-khattmix) | 2026-08-24 | text-recognition | candidate | — |
| [NicholasThomas/dataset_152013975_document_ocr_multimodal3](https://huggingface.co/datasets/NicholasThomas/dataset_152013975_document_ocr_multimodal3) | 2026-08-23 | text-recognition | candidate | 
	
		
	
	
		dataset_152013975_document_ocr_multimodal3.py
	


	
		
	
	
		Dataset Summary
	

A document ocr dataset with multimodal3 modality, stored in huggingface format.

	
		
	
	
		Preprocessing & Augmentation
	


Preprocessing: progressive
Augmentation: randaugment


	
		
	
	
		Splits & Sampling
	


Split strategy: random 90 10
Sampling: contrastive


	
		
	
	
		Quality & Labeling
	


Quality filtering: lenient
Labeling: manual


	
		
	
	
		Files… See the full description on the dataset page: https://huggingface.co/datasets/NicholasThomas/dataset_152013975_document_ocr_multimodal3. |
| [JuanfelipeX123/high-quality-invoice-images-for-ocr](https://huggingface.co/datasets/JuanfelipeX123/high-quality-invoice-images-for-ocr) | 2026-08-23 | document-parsing, text-recognition | candidate | 
	
		
	
	
		Dataset Card for high_quality_invoice_images_ocr
	


This is a FiftyOne dataset containing 8,181 high-quality synthetic invoice images for OCR and document understanding tasks. The dataset includes 1,489 fully annotated samples with structured JSON metadata and raw OCR text, plus 6,692 unannotated images for semi-supervised learning or annotation projects.

	
		
	
	
		Installation
	

If you haven't already, install FiftyOne:
pip install -U fiftyone


	
		
	
	
		Usage
	

import… See the full description on the dataset page: https://huggingface.co/datasets/JuanfelipeX123/high-quality-invoice-images-for-ocr. |
| [hoainv/ocr-lmdb-vi-sample20pct](https://huggingface.co/datasets/hoainv/ocr-lmdb-vi-sample20pct) | 2026-08-23 | text-recognition | candidate | 
	
		
	
	
		ocr-lmdb-vi (20% random sample)
	

Random 20% subsample of each LMDB sub-dataset from the
private hoainv/ocr-lmdb-vi dataset, sampled without replacement with a fixed
seed (42) for reproducibility. Directory structure and LMDB key
scheme (image-%09d, label-%09d, wh-%09d, num-samples, 1-indexed)
are unchanged, so it's a drop-in replacement for LMDBDataSet
(octools/data/lmdb_dataset.py).

	
		
folder
total samples
sampled


		
lmdb_pdf/pdf_line_crops_0905
2169
434


	

 |
| [context212/context212-alhazen-ocr](https://huggingface.co/datasets/context212/context212-alhazen-ocr) | 2026-08-23 | handwriting-recognition, text-recognition | candidate | 
	
		
	
	
		Alhazen-OCR Data
	

alhazen-ocr is the training dataset behind
context212/alhazen-ocr, an
Arabic-first OCR vision-language model. It combines license-clean Arabic
OCR sources — synthetic documents, institutional invoices, and handwritten
text — into a single normalized image + text format, with a held-out eval
split for CER/WER benchmarking.
Quick links:

🤗 Model: context212/alhazen-ocr
🛠️ Code (data pipeline, training, eval): github.com/context212/atlas-ocr
📊 External… See the full description on the dataset page: https://huggingface.co/datasets/context212/context212-alhazen-ocr. |
| [context212/atlas-ocr-data](https://huggingface.co/datasets/context212/atlas-ocr-data) | 2026-08-23 | text-recognition | candidate | — |
| [SeeWye/NFA_OCR_reinforcement_learning_format_TEST3](https://huggingface.co/datasets/SeeWye/NFA_OCR_reinforcement_learning_format_TEST3) | 2026-08-22 | text-recognition | candidate | — |
| [murchgrey/docparser-ocr-samples](https://huggingface.co/datasets/murchgrey/docparser-ocr-samples) | 2026-08-22 | text-recognition | candidate | — |
| [IshaanKaur/dataset_152150257_document_ocr_image_depth](https://huggingface.co/datasets/IshaanKaur/dataset_152150257_document_ocr_image_depth) | 2026-08-22 | text-recognition | candidate | 
	
		
	
	
		dataset_152150257_document_ocr_image_depth.py
	


	
		
	
	
		Dataset Summary
	

A document ocr dataset with image depth modality, stored in parquet format.

	
		
	
	
		Preprocessing & Augmentation
	


Preprocessing: aggressive
Augmentation: autoaugment


	
		
	
	
		Splits & Sampling
	


Split strategy: stratified 90 10
Sampling: balanced


	
		
	
	
		Quality & Labeling
	


Quality filtering: adaptive
Labeling: weak supervision


	
		
	
	
		Files… See the full description on the dataset page: https://huggingface.co/datasets/IshaanKaur/dataset_152150257_document_ocr_image_depth. |
| [gonzalezadrian/dataset_153097816_document_ocr_audio_video](https://huggingface.co/datasets/gonzalezadrian/dataset_153097816_document_ocr_audio_video) | 2026-08-22 | text-recognition | candidate | 
	
		
	
	
		dataset_153097816_document_ocr_audio_video.py
	


	
		
	
	
		Dataset Summary
	

A document ocr dataset with audio video modality, stored in huggingface format.

	
		
	
	
		Preprocessing & Augmentation
	


Preprocessing: adaptive
Augmentation: mixup cutmix


	
		
	
	
		Splits & Sampling
	


Split strategy: temporal
Sampling: random


	
		
	
	
		Quality & Labeling
	


Quality filtering: strict
Labeling: semi auto


	
		
	
	
		Files
	


dataset_153097816_document_ocr_audio_video.py —… See the full description on the dataset page: https://huggingface.co/datasets/gonzalezadrian/dataset_153097816_document_ocr_audio_video. |
| [themohal/saraiki-ocr-general-dataset](https://huggingface.co/datasets/themohal/saraiki-ocr-general-dataset) | 2026-08-21 | text-recognition | candidate | 
	
		
	
	
		Saraiki OCR General Dataset (Gemini-generated, Jataki dialect)
	

Original Jataki Saraiki text -- spanning 21 everyday genres (poetry, prose, dialogue, proverbs,
riddles, lists/notes, letters, instructions, recipes, news-style reports, table-style data,
receipts/bills, form fields, classified ads, public notices, exam questions, SMS-style messages,
signage/labels, weather notes, numeral-heavy text, and children's stories) -- generated by Gemini,
quality/dialect-purity judged, then… See the full description on the dataset page: https://huggingface.co/datasets/themohal/saraiki-ocr-general-dataset. |
| [rydalharbi/dataset_150683796_document_ocr_video_text](https://huggingface.co/datasets/rydalharbi/dataset_150683796_document_ocr_video_text) | 2026-08-21 | text-recognition | candidate | 
	
		
	
	
		dataset_150683796_document_ocr_video_text.py
	


	
		
	
	
		Dataset Summary
	

A document ocr dataset with video text modality, stored in npy sharded format.

	
		
	
	
		Preprocessing & Augmentation
	


Preprocessing: domain specific
Augmentation: light


	
		
	
	
		Splits & Sampling
	


Split strategy: leave one out
Sampling: contrastive


	
		
	
	
		Quality & Labeling
	


Quality filtering: moderate
Labeling: semi auto


	
		
	
	
		Files… See the full description on the dataset page: https://huggingface.co/datasets/rydalharbi/dataset_150683796_document_ocr_video_text. |
| [Peterleo5/uae-ocr-test](https://huggingface.co/datasets/Peterleo5/uae-ocr-test) | 2026-08-21 | text-recognition | candidate | — |
| [MR3z4/persian-handwriting-ocr](https://huggingface.co/datasets/MR3z4/persian-handwriting-ocr) | 2026-08-21 | handwriting-recognition, text-recognition | candidate | 
	
		
	
	
		Persian Handwriting OCR Dataset
	


	
		
	
	
		Dataset Summary
	

A standardized dataset of Persian (Farsi) handwritten pages with word-level
bounding-box annotations and transcriptions. The dataset is page-level:
each sample is a full page scan; annotations are one row per word bbox on
that page. This is the most flexible form -- users can train page-level OCR,
word detection (DBNet/PaddleOCR), or derive word/line crops as needed.

Pages: 1115 scanned pages (canonical IDs… See the full description on the dataset page: https://huggingface.co/datasets/MR3z4/persian-handwriting-ocr. |
| [mason1998/kurdish-ocr-100](https://huggingface.co/datasets/mason1998/kurdish-ocr-100) | 2026-08-21 | text-recognition | candidate | — |
| [lingamvamshikrishnareddy/ramanv-document-ocr-2](https://huggingface.co/datasets/lingamvamshikrishnareddy/ramanv-document-ocr-2) | 2026-08-21 | text-recognition | candidate | — |
| [lingamvamshikrishnareddy/ramanv-document-ocr](https://huggingface.co/datasets/lingamvamshikrishnareddy/ramanv-document-ocr) | 2026-08-21 | text-recognition | candidate | — |
| [Ihayashi/dataset_149844858_document_ocr_image_text](https://huggingface.co/datasets/Ihayashi/dataset_149844858_document_ocr_image_text) | 2026-08-21 | text-recognition | candidate | 
	
		
	
	
		dataset_149844858_document_ocr_image_text.py
	


	
		
	
	
		Dataset Summary
	

A document ocr dataset with image text modality, stored in csv format.

	
		
	
	
		Preprocessing & Augmentation
	


Preprocessing: aggressive
Augmentation: autoaugment


	
		
	
	
		Splits & Sampling
	


Split strategy: stratified 90 10
Sampling: balanced


	
		
	
	
		Quality & Labeling
	


Quality filtering: lenient
Labeling: self training


	
		
	
	
		Files… See the full description on the dataset page: https://huggingface.co/datasets/Ihayashi/dataset_149844858_document_ocr_image_text. |
| [gabrielvieiraah/dataset_150426115_document_ocr_audio_text](https://huggingface.co/datasets/gabrielvieiraah/dataset_150426115_document_ocr_audio_text) | 2026-08-21 | text-recognition | candidate | 
	
		
	
	
		dataset_150426115_document_ocr_audio_text.py
	


	
		
	
	
		Dataset Summary
	

A document ocr dataset with audio text modality, stored in jsonl format.

	
		
	
	
		Preprocessing & Augmentation
	


Preprocessing: adaptive
Augmentation: randaugment


	
		
	
	
		Splits & Sampling
	


Split strategy: temporal
Sampling: curriculum


	
		
	
	
		Quality & Labeling
	


Quality filtering: moderate
Labeling: manual


	
		
	
	
		Files
	


dataset_150426115_document_ocr_audio_text.py — main… See the full description on the dataset page: https://huggingface.co/datasets/gabrielvieiraah/dataset_150426115_document_ocr_audio_text. |
| [daan-dekker/dataset_150386258_document_ocr_audio_text](https://huggingface.co/datasets/daan-dekker/dataset_150386258_document_ocr_audio_text) | 2026-08-21 | text-recognition | candidate | 
	
		
	
	
		dataset_150386258_document_ocr_audio_text.py
	


	
		
	
	
		Dataset Summary
	

A document ocr dataset with audio text modality, stored in parquet format.

	
		
	
	
		Preprocessing & Augmentation
	


Preprocessing: adaptive
Augmentation: none


	
		
	
	
		Splits & Sampling
	


Split strategy: stratified 90 10
Sampling: balanced


	
		
	
	
		Quality & Labeling
	


Quality filtering: moderate
Labeling: self training


	
		
	
	
		Files
	


dataset_150386258_document_ocr_audio_text.py —… See the full description on the dataset page: https://huggingface.co/datasets/daan-dekker/dataset_150386258_document_ocr_audio_text. |
| [andrewtya04/dataset_152294269_document_ocr_image_depth](https://huggingface.co/datasets/andrewtya04/dataset_152294269_document_ocr_image_depth) | 2026-08-21 | text-recognition | candidate | 
	
		
	
	
		dataset_152294269_document_ocr_image_depth.py
	


	
		
	
	
		Dataset Summary
	

A document ocr dataset with image depth modality, stored in parquet format.

	
		
	
	
		Preprocessing & Augmentation
	


Preprocessing: auto ml
Augmentation: autoaugment


	
		
	
	
		Splits & Sampling
	


Split strategy: temporal
Sampling: balanced


	
		
	
	
		Quality & Labeling
	


Quality filtering: adaptive
Labeling: pseudo label


	
		
	
	
		Files
	


dataset_152294269_document_ocr_image_depth.py —… See the full description on the dataset page: https://huggingface.co/datasets/andrewtya04/dataset_152294269_document_ocr_image_depth. |
| [OCR-Data/dataset_nihal](https://huggingface.co/datasets/OCR-Data/dataset_nihal) | 2026-08-20 | text-recognition | candidate | — |
| [nikhitrivedi1/OCR4_Base_STRATIFIED_20K](https://huggingface.co/datasets/nikhitrivedi1/OCR4_Base_STRATIFIED_20K) | 2026-08-20 | text-recognition | candidate | — |
| [Ericu950/swedish-print-ocr-training-data](https://huggingface.co/datasets/Ericu950/swedish-print-ocr-training-data) | 2026-08-20 | text-recognition | candidate | 
	
		
	
	
		Swedish Print OCR — training and evaluation data
	

Training mixture and benchmarks for
Ericu950/swedish-print-ocr-3b (production)
and
Ericu950/swedish-print-ocr-3b-benchmark
(held-out evaluation model). Each training row is a chat-format example:
{"messages": [{"role": "user", "content": "<image>Transkribera sidans brödtext normaliserat: ..."},
              {"role": "assistant", "content": "..."}],
 "images": ["<absolute path on the training cluster>"]}

Images are included under… See the full description on the dataset page: https://huggingface.co/datasets/Ericu950/swedish-print-ocr-training-data. |
| [Ericu950/swedish-print-ocr-code](https://huggingface.co/datasets/Ericu950/swedish-print-ocr-code) | 2026-08-20 | text-recognition | candidate | 
	
		
	
	
		Swedish Print OCR — training and evaluation code
	

The code behind the paper A Vision–Language OCR Model and an Open Corpus
(Cullhed). This is the curated pipeline that produced the released models,
benchmarks and corpus — exploratory and superseded experiment code is not
included. Comments and docstrings are in Swedish; they document not just what
each script does but why it is built the way it is.

	
		
	
	
		Companion repositories
	


Evaluation model:… See the full description on the dataset page: https://huggingface.co/datasets/Ericu950/swedish-print-ocr-code. |
| [Yesianrohn/ocr_image_urls](https://huggingface.co/datasets/Yesianrohn/ocr_image_urls) | 2026-08-19 | text-recognition | candidate | — |
| [Werea-co/werea-tr-doc-ocr-enterprise-v2](https://huggingface.co/datasets/Werea-co/werea-tr-doc-ocr-enterprise-v2) | 2026-08-19 | text-recognition | candidate | 
	
		
	
	
		Werea Turkish Enterprise Documents v2 📄🇹🇷
	

v1 setinin
enterprise sürümü: 12 belge türü × 3 çekim koşulu, 12.960 train + 900 test
sayfası. Werea-DocOCR v2 modellerinin eğitimi için üretilmiştir.

	
		
	
	
		Belge türleri (12)
	

Genel vekaletname · DASK poliçesi · e-Arşiv fatura · Konut kira sözleşmesi ·
Banka dekontu · Tapu senedi · Maaş bordrosu · Kasko poliçesi · Araç tescil
bilgi formu · Resmî kurum yazısı · Ticaret sicil ilanı · SGK hizmet dökümü

	
		
	
	
		Çekim… See the full description on the dataset page: https://huggingface.co/datasets/Werea-co/werea-tr-doc-ocr-enterprise-v2. |
| [thundarstrom/synthetic-indian-anpr-ocr](https://huggingface.co/datasets/thundarstrom/synthetic-indian-anpr-ocr) | 2026-08-19 | text-recognition | candidate | 
	
		
	
	
		Synthetic Indian License Plate Character Generator Corpus
	

Part of the Edge-AI Traffic & Vehicle Analytics System repository by thundarstrom.

	
		
	
	
		Dataset Summary
	

18,000 synthetically generated Indian plate crops covering all 36 Indian states and Union Territories with diverse fonts, spacing, distortion, and noise.
Ideal for pretraining sequence recognition models on rare RTO state codes before real data fine-tuning.


	
		
	
	
		How to Access and Download… See the full description on the dataset page: https://huggingface.co/datasets/thundarstrom/synthetic-indian-anpr-ocr. |
| [thundarstrom/indian-anpr-ocr-corpus](https://huggingface.co/datasets/thundarstrom/indian-anpr-ocr-corpus) | 2026-08-19 | text-recognition | candidate | 
	
		
	
	
		Indian License Plate Character Recognition (PARSeq & LMDB)
	

Part of the Edge-AI Traffic & Vehicle Analytics System repository by thundarstrom.

	
		
	
	
		Dataset Summary
	

A curated dataset of 18,537 normalized license plate image crops aligned strictly with Indian Motor Vehicle Act alphanumeric formats (^[A-Z]{2}[0-9]{1,2}[A-Z]{1,3}[0-9]{4}$).

	
		
	
	
		Formats Provided
	


Raw Crops & Ground Truth: parseq_dataset/ with gt.txt (Tab-delimited: filename \t text).… See the full description on the dataset page: https://huggingface.co/datasets/thundarstrom/indian-anpr-ocr-corpus. |
| [thundarstrom/indian-anpr-ocr-benchmark](https://huggingface.co/datasets/thundarstrom/indian-anpr-ocr-benchmark) | 2026-08-19 | text-recognition | candidate | 
	
		
	
	
		DashCop Real-World Out-of-Distribution ANPR Benchmark
	

Part of the Edge-AI Traffic & Vehicle Analytics System repository by thundarstrom.

	
		
	
	
		Dataset Summary
	

A frozen evaluation benchmark of 3,034 real dashcam plate crops captured in challenging conditions (low resolution median 56x34 px, motion blur, direct sunlight, rain).

	
		
	
	
		Policy
	


FROZEN TEST SET: Never train, augment, or fine-tune models on this dataset.
Use exclusively to evaluate zero-shot… See the full description on the dataset page: https://huggingface.co/datasets/thundarstrom/indian-anpr-ocr-benchmark. |
| [Peterleo5/uae-ocr-gemma4](https://huggingface.co/datasets/Peterleo5/uae-ocr-gemma4) | 2026-08-19 | text-recognition | candidate | — |
| [Ericu950/litteraturbanken-ocr-corpus](https://huggingface.co/datasets/Ericu950/litteraturbanken-ocr-corpus) | 2026-08-19 | text-recognition | candidate | 
	
		
	
	
		Litteraturbanken OCR Corpus
	

Machine-read text of Litteraturbanken's facsimile collection, produced by a fine-tuned
vision-language OCR model (see
Ericu950/swedish-print-ocr-3b).
13,647 works, 2,260,417 pages, 2.95 billion characters, one row per printed page, keyed by
the catalogue's own page name. 179,768 of those pages (247.6 million characters) predate 1800,
including the 1541 Gustav Vasa Bible in full and all five volumes of Rudbeck's Atlantica
(1679–1702).
This is the only… See the full description on the dataset page: https://huggingface.co/datasets/Ericu950/litteraturbanken-ocr-corpus. |
| [BIUS-batch1/ocr-1fps](https://huggingface.co/datasets/BIUS-batch1/ocr-1fps) | 2026-08-19 | text-recognition | candidate | — |
| [Werea-co/werea-tr-doc-ocr-synthetic](https://huggingface.co/datasets/Werea-co/werea-tr-doc-ocr-synthetic) | 2026-08-18 | text-recognition | candidate | 
	
		
	
	
		Werea Turkish Enterprise Documents 📄🇹🇷
	

Türkçe kurumsal belge OCR eğitimi için tamamı sentetik sayfa görüntüleri ve
birebir eşleşen markdown ground-truth metinleri. Werea
tarafından Werea-DocOCR modellerinin eğitimi için üretilmiştir.

	
		
	
	
		Belge türleri
	


	
		
Tür
Train
Test
İçerik


		
Genel vekaletname
500
50
Noter başlığı, taraflar, yetki maddeleri, noter şerhi


DASK poliçesi
500
50
Poliçe/sigortalı/bina bilgileri, prim tablosu


e-Arşiv fatura
500
50
Satıcı/alıcı… See the full description on the dataset page: https://huggingface.co/datasets/Werea-co/werea-tr-doc-ocr-synthetic. |
| [themohal/saraiki-ocr-poetry-dataset](https://huggingface.co/datasets/themohal/saraiki-ocr-poetry-dataset) | 2026-08-18 | text-recognition | candidate | 
	
		
	
	
		Saraiki OCR Poetry Dataset (Gemini-generated, Jataki dialect)
	

Original Jataki Saraiki poems generated by Gemini, quality/dialect-purity judged, then rendered as images with the Mehr Nastaliq Saraiki font (RAQM-shaped for correct Perso-Arabic joining) -- for OCR / text-recognition training.
Row format:
{"id": ..., "image": <PIL image>, "text": "<poem, \n-separated lines>",
  "length_category": "short|medium|long", "line_count": ..., "word_count": ..., "judge_score": ...}… See the full description on the dataset page: https://huggingface.co/datasets/themohal/saraiki-ocr-poetry-dataset. |
| [rocky1410/goat-ocr-color-synth-300k-v0](https://huggingface.co/datasets/rocky1410/goat-ocr-color-synth-300k-v0) | 2026-08-18 | text-recognition | candidate | — |
| [hydroshiba/aic26-b1-ocr](https://huggingface.co/datasets/hydroshiba/aic26-b1-ocr) | 2026-08-18 | text-recognition | candidate | — |
| [florapeterpaul3/geeklink-ocr-benchmark](https://huggingface.co/datasets/florapeterpaul3/geeklink-ocr-benchmark) | 2026-08-18 | text-recognition | candidate | 
	
		
	
	
		GeekLink OCR Benchmark
	

A benchmark for burned-in video subtitle OCR: 600 subtitle images across
6 languages (English, Spanish, Japanese, Korean, Chinese, Greek), rendered
onto real film footage with exact known ground truth — so there's no
ambiguity about what the "correct" answer is, and no privacy or copyright
risk in the images themselves.
Unlike document-OCR benchmarks (scanned pages, receipts, street signs), this
targets the specific failure modes of subtitle OCR in video:… See the full description on the dataset page: https://huggingface.co/datasets/florapeterpaul3/geeklink-ocr-benchmark. |
| [vaishnavi0901/kannada-ocr-dataset](https://huggingface.co/datasets/vaishnavi0901/kannada-ocr-dataset) | 2026-08-17 | handwriting-recognition, text-recognition | candidate | 
	
		
	
	
		Kannada OCR Fine-Tuning Dataset
	

Fine-tuning dataset for training vision-language models to read handwritten Kannada text from historical birth and death register images.

	
		
	
	
		Dataset Description
	

This dataset pairs scanned register page images with structured JSON ground truth extracted from verified source data. The goal is to fine-tune a model that can look at a register page and output the correct field values for every row on that page.

	
		
	
	
		Source… See the full description on the dataset page: https://huggingface.co/datasets/vaishnavi0901/kannada-ocr-dataset. |
| [nubuwwat/khatme-nubuwwat-ocr-dataset](https://huggingface.co/datasets/nubuwwat/khatme-nubuwwat-ocr-dataset) | 2026-08-17 | text-recognition | candidate | 
	
		
	
	
		Khatme-Nubuwwat Urdu OCR Corpus
	

This is a structure-aware, fully OCR'd text dataset of around 215 Urdu Khatme Nubuwat books/volumes (approximately 86,557 pages of text). The text dataset is paried with source-page scans.
The books are composed of Nastaliq prose with heavy references to Quran and Hadith. Effort was made to ensure that the OCR pipeline transcribed the text verbatim without any modifications. The transcribed pages were passed through a multi-signal accuracy layer… See the full description on the dataset page: https://huggingface.co/datasets/nubuwwat/khatme-nubuwwat-ocr-dataset. |
| [hotsheep/legal-ocr](https://huggingface.co/datasets/hotsheep/legal-ocr) | 2026-08-17 | text-recognition | candidate | — |
| [formospeech/yttd_ocrcap](https://huggingface.co/datasets/formospeech/yttd_ocrcap) | 2026-08-16 | text-recognition | candidate | 
	
		
	
	
		TRAIN
	


	
		
Subset
lang_name
hours
n_utts
n_chars_in_utts
secs/utt
chars/sec
n_sents
n_chars_in_sents


		
nan_tw
Taigi
97.87
169,038
1,540,824
2.08
4.37
0
0


Total
-
97.87
169,038
1,540,824
2.08
4.37
0
0


	

 |
| [remots/ocr-corrections-digar-est](https://huggingface.co/datasets/remots/ocr-corrections-digar-est) | 2026-08-15 | text-recognition | candidate | — |
| [kdeng03/mol-rep-ocr-v1.1](https://huggingface.co/datasets/kdeng03/mol-rep-ocr-v1.1) | 2026-08-14 | text-recognition | candidate | — |
| [alphabot2/14_RGB_OCR](https://huggingface.co/datasets/alphabot2/14_RGB_OCR) | 2026-08-14 | text-recognition | candidate | This dataset was created using LeRobot.







	
		
	
	
		Dataset Structure
	

meta/info.json:
{
    "codebase_version": "v3.0",
    "robot_type": "aibot2",
    "total_episodes": 62,
    "total_frames": 25168,
    "total_tasks": 1,
    "chunks_size": 1000,
    "data_files_size_in_mb": 100,
    "video_files_size_in_mb": 200,
    "fps": 10,
    "splits": {
        "train": "0:62"
    },
    "data_path": "data/chunk-{chunk_index:03d}/file-{file_index:03d}.parquet",
    "video_path":… See the full description on the dataset page: https://huggingface.co/datasets/alphabot2/14_RGB_OCR. |
| [alphabot2/14_Merged_RGB_ocr](https://huggingface.co/datasets/alphabot2/14_Merged_RGB_ocr) | 2026-08-14 | text-recognition | candidate | This dataset was created using LeRobot.







	
		
	
	
		Dataset Structure
	

meta/info.json:
{
    "codebase_version": "v3.0",
    "robot_type": "aibot2",
    "total_episodes": 126,
    "total_frames": 54648,
    "total_tasks": 3,
    "chunks_size": 1000,
    "data_files_size_in_mb": 100,
    "video_files_size_in_mb": 200,
    "fps": 10,
    "splits": {
        "train": "0:126"
    },
    "data_path": "data/chunk-{chunk_index:03d}/file-{file_index:03d}.parquet",
    "video_path":… See the full description on the dataset page: https://huggingface.co/datasets/alphabot2/14_Merged_RGB_ocr. |
| [alphabot2/14_Merged_Depth_ocr](https://huggingface.co/datasets/alphabot2/14_Merged_Depth_ocr) | 2026-08-14 | text-recognition | candidate | This dataset was created using LeRobot.







	
		
	
	
		Dataset Structure
	

meta/info.json:
{
    "codebase_version": "v3.0",
    "robot_type": "aibot2",
    "total_episodes": 126,
    "total_frames": 52829,
    "total_tasks": 3,
    "chunks_size": 1000,
    "data_files_size_in_mb": 100,
    "video_files_size_in_mb": 200,
    "fps": 10,
    "splits": {
        "train": "0:126"
    },
    "data_path": "data/chunk-{chunk_index:03d}/file-{file_index:03d}.parquet",
    "video_path":… See the full description on the dataset page: https://huggingface.co/datasets/alphabot2/14_Merged_Depth_ocr. |
| [alphabot2/14_Depth_OCR](https://huggingface.co/datasets/alphabot2/14_Depth_OCR) | 2026-08-14 | text-recognition | candidate | This dataset was created using LeRobot.







	
		
	
	
		Dataset Structure
	

meta/info.json:
{
    "codebase_version": "v3.0",
    "robot_type": "aibot2",
    "total_episodes": 62,
    "total_frames": 24846,
    "total_tasks": 1,
    "chunks_size": 1000,
    "data_files_size_in_mb": 100,
    "video_files_size_in_mb": 200,
    "fps": 10,
    "splits": {
        "train": "0:62"
    },
    "data_path": "data/chunk-{chunk_index:03d}/file-{file_index:03d}.parquet",
    "video_path":… See the full description on the dataset page: https://huggingface.co/datasets/alphabot2/14_Depth_OCR. |
| [OCR-Data/dataset](https://huggingface.co/datasets/OCR-Data/dataset) | 2026-08-13 | text-recognition | candidate | — |
| [ymfl/LaTeX_OCR](https://huggingface.co/datasets/ymfl/LaTeX_OCR) | 2026-08-12 | text-recognition | candidate | 
	
		
	
	
		LaTeX OCR 的数据仓库
	

本数据仓库是专为 LaTeX_OCR 及 LaTeX_OCR_PRO 制作的数据，来源于 https://zenodo.org/record/56198#.V2p0KTXT6eA 以及 https://www.isical.ac.in/~crohme/ 以及我们自己构建。
如果这个数据仓库有帮助到你的话，请点亮 ❤️like ++
后续追加新的数据也会放在这个仓库 ~~

原始数据仓库在github LinXueyuanStdio/Data-for-LaTeX_OCR.


	
		
	
	
		数据集
	

本仓库有 5 个数据集

small 是小数据集，样本数 110 条，用于测试
full 是印刷体约 100k 的完整数据集。实际上样本数略小于 100k，因为用 LaTeX 的抽象语法树剔除了很多不能渲染的 LaTeX。
synthetic_handwrite 是手写体 100k 的完整数据集，基于 full 的公式，使用手写字体合成而来，可以视为人类在纸上的手写体。样本数实际上略小于 100k，理由同上。… See the full description on the dataset page: https://huggingface.co/datasets/ymfl/LaTeX_OCR. |
| [SeeWye/Nondeterministic_Finite_Automata_OCR_Conversations_Format2](https://huggingface.co/datasets/SeeWye/Nondeterministic_Finite_Automata_OCR_Conversations_Format2) | 2026-08-12 | text-recognition | candidate | — |
| [Roy229/hf7192-ocr-testsuite-504791](https://huggingface.co/datasets/Roy229/hf7192-ocr-testsuite-504791) | 2026-08-12 | text-recognition | candidate | — |
| [kdeng03/mol-rep-ocr-v1](https://huggingface.co/datasets/kdeng03/mol-rep-ocr-v1) | 2026-08-12 | text-recognition | candidate | — |
| [zhuq41/huggingface_5318_20260811_cand_ocr_pub_nk9x](https://huggingface.co/datasets/zhuq41/huggingface_5318_20260811_cand_ocr_pub_nk9x) | 2026-08-11 | text-recognition | candidate | — |
| [ussooraj/OCR-bench-Malayalam](https://huggingface.co/datasets/ussooraj/OCR-bench-Malayalam) | 2026-08-11 | text-recognition | candidate | — |
| [mehdigououiad/permis-ocr-surya](https://huggingface.co/datasets/mehdigououiad/permis-ocr-surya) | 2026-08-11 | text-recognition | candidate | 
	
		
	
	
		Surya OCR 2 (ocr) on mehdigououiad/permis-ocr-bench
	

Full-page ocr (structured html + bounding boxes) over images in
mehdigououiad/permis-ocr-bench using
Surya OCR 2 (650M, Qwen3.5-based) by Datalab, via the
surya-ocr package, run as offline vLLM batch
inference on Hugging Face Jobs.

	
		
	
	
		Processing Details
	


Source Dataset: mehdigououiad/permis-ocr-bench
Model: datalab-to/surya-ocr-2
Task: ocr
Input column: image (image)
Text column: markdown (flattened, reading-order… See the full description on the dataset page: https://huggingface.co/datasets/mehdigououiad/permis-ocr-surya. |
| [mehdigououiad/permis-ocr-ppocrv6](https://huggingface.co/datasets/mehdigououiad/permis-ocr-ppocrv6) | 2026-08-11 | text-recognition | candidate | 
	
		
	
	
		OCR with PP-OCRv6 Medium
	

Plain-text OCR results for images from mehdigououiad/permis-ocr-bench, produced by
PaddlePaddle's PP-OCRv6
medium pipeline (34.5M (22M det + 19M rec)).

	
		
	
	
		Processing details
	


Source: mehdigououiad/permis-ocr-bench
Model: PP-OCRv6_medium (PP-OCRv6_medium_det + PP-OCRv6_medium_rec)
Tier: medium (34.5M (22M det + 19M rec))
Recognition accuracy: 83.2%
Languages: 50 languages (zh, zh-Hant, en, ja + 46 Latin-script)
Engine: paddle_static
Samples: 2… See the full description on the dataset page: https://huggingface.co/datasets/mehdigououiad/permis-ocr-ppocrv6. |
| [mehdigououiad/permis-ocr-ovis](https://huggingface.co/datasets/mehdigououiad/permis-ocr-ovis) | 2026-08-11 | document-parsing, text-recognition | candidate | 
	
		
	
	
		Document OCR using OvisOCR2
	

This dataset contains OCR results from images in mehdigououiad/permis-ocr-bench using OvisOCR2, a compact 0.9B document parsing model (96.58 on OmniDocBench v1.6).

	
		
	
	
		Processing Details
	


Source Dataset: mehdigououiad/permis-ocr-bench
Model: ATH-MaaS/OvisOCR2
Number of Samples: 2
Processing Time: 5.4 min
Processing Date: 2026-08-11 13:57 UTC


	
		
	
	
		Configuration
	


Image Column: image
Dataset Split: train
Batch Size: 16
Max Model… See the full description on the dataset page: https://huggingface.co/datasets/mehdigououiad/permis-ocr-ovis. |
| [mehdigououiad/permis-ocr-nuextract3](https://huggingface.co/datasets/mehdigououiad/permis-ocr-nuextract3) | 2026-08-11 | document-parsing, text-recognition | candidate | 
	
		
	
	
		NuExtract3 on mehdigououiad/permis-ocr-bench
	

This dataset contains outputs from mehdigououiad/permis-ocr-bench processed with NuExtract3, a 4B vision-language model for document understanding.

	
		
	
	
		Processing Details
	


Source Dataset: mehdigououiad/permis-ocr-bench
Model: numind/NuExtract3
Mode: markdown
Number of Samples: 2
Processing Time: 4.4 min
Processing Date: 2026-08-11 13:55 UTC


	
		
	
	
		Configuration
	


Image Column: image
Output Column: markdown
Dataset… See the full description on the dataset page: https://huggingface.co/datasets/mehdigououiad/permis-ocr-nuextract3. |
| [mehdigououiad/permis-ocr-lighton2](https://huggingface.co/datasets/mehdigououiad/permis-ocr-lighton2) | 2026-08-11 | text-recognition | candidate | 
	
		
	
	
		Document OCR using LightOnOCR-2-1B
	

This dataset contains OCR results from images in mehdigououiad/permis-ocr-bench using LightOnOCR-2, a fast and compact 1B OCR model trained with RLVR.

	
		
	
	
		Processing Details
	


Source Dataset: mehdigououiad/permis-ocr-bench
Model: lightonai/LightOnOCR-2-1B
Number of Samples: 2
Processing Time: 1.8 min
Processing Date: 2026-08-11 13:50 UTC


	
		
	
	
		Configuration
	


Image Column: image
Output Column: markdown
Dataset Split: train… See the full description on the dataset page: https://huggingface.co/datasets/mehdigououiad/permis-ocr-lighton2. |
| [mehdigououiad/permis-ocr-glm](https://huggingface.co/datasets/mehdigououiad/permis-ocr-glm) | 2026-08-11 | text-recognition | candidate | 
	
		
	
	
		Document OCR using GLM-OCR
	

This dataset contains OCR results from images in mehdigououiad/permis-ocr-bench using GLM-OCR, a compact 0.9B OCR model achieving SOTA performance.

	
		
	
	
		Processing Details
	


Source Dataset: mehdigououiad/permis-ocr-bench
Model: zai-org/GLM-OCR
Task: text recognition
Number of Samples: 2
Processing Time: 1.3 min
Processing Date: 2026-08-11 13:48 UTC


	
		
	
	
		Configuration
	


Image Column: image
Output Column: markdown
Dataset Split: train… See the full description on the dataset page: https://huggingface.co/datasets/mehdigououiad/permis-ocr-glm. |
| [ilsilfverskiold/ocr-benchmark](https://huggingface.co/datasets/ilsilfverskiold/ocr-benchmark) | 2026-08-11 | text-recognition | candidate | 
	
		
	
	
		OCR Benchmark — Documents
	

The 93 document images and ground truth used by the
ocr-benchmark harness.
The benchmark code, the reference run results, and the full methodology live
in the GitHub repo — this dataset is the document corpus only.

	
		
	
	
		Structure
	

One train split, 93 rows, one row per document:

	
		
Column
Type
Description


		
image
Image
The document page (PNG/JPG)


stem
string
Filename stem (e.g. invoice_000)


tier
string
Difficulty: easy, medium, or hard… See the full description on the dataset page: https://huggingface.co/datasets/ilsilfverskiold/ocr-benchmark. |
| [alphabot2/07-08-2026_OCR_Bimanual_no_depth](https://huggingface.co/datasets/alphabot2/07-08-2026_OCR_Bimanual_no_depth) | 2026-08-11 | text-recognition | candidate | This dataset was created using LeRobot.







	
		
	
	
		Dataset Structure
	

meta/info.json:
{
    "codebase_version": "v3.0",
    "robot_type": "aibot2",
    "total_episodes": 37,
    "total_frames": 19053,
    "total_tasks": 1,
    "chunks_size": 1000,
    "data_files_size_in_mb": 100,
    "video_files_size_in_mb": 200,
    "fps": 10,
    "splits": {
        "train": "0:37"
    },
    "data_path": "data/chunk-{chunk_index:03d}/file-{file_index:03d}.parquet",
    "video_path":… See the full description on the dataset page: https://huggingface.co/datasets/alphabot2/07-08-2026_OCR_Bimanual_no_depth. |
| [kdeng03/mol-rep-ocr-v0](https://huggingface.co/datasets/kdeng03/mol-rep-ocr-v0) | 2026-08-10 | text-recognition | candidate | — |
| [ha684/nxscan-ocr-dataset-v7](https://huggingface.co/datasets/ha684/nxscan-ocr-dataset-v7) | 2026-08-10 | text-recognition | candidate | — |
| [NeuralMetrics/ocr-benchmark](https://huggingface.co/datasets/NeuralMetrics/ocr-benchmark) | 2026-08-09 | text-recognition | candidate | 


	
		
	
	
		Neural Metrics · How good is your OCR, really?
	






A benchmark of real documents paired with ground-truth JSON, designed to score end-to-end accuracy rather than raw character error rate. That distinction matters: an OCR pass can be 99% correct at the character level and still get the invoice total wrong.
We use it for: scoring candidate OCR models on the metric that actually pays the bills - regression testing before a model swap.


	
		
	
	
		Attribution
	

This is an… See the full description on the dataset page: https://huggingface.co/datasets/NeuralMetrics/ocr-benchmark. |
| [NeuralMetrics/invoices-and-receipts-ocr-v1](https://huggingface.co/datasets/NeuralMetrics/invoices-and-receipts-ocr-v1) | 2026-08-09 | table-recognition, text-recognition | candidate | 


	
		
	
	
		Neural Metrics · Receipts too - the hardest easy documents.
	






Invoices and receipts with OCR annotations. Receipts are deceptively hard: thermal print fades, columns drift, and the total is rarely where you expect it.
We use it for: expanding coverage beyond clean A4 invoices - stress-testing line-item table extraction.


	
		
	
	
		Attribution
	

This is an unmodified fork of mychen76/invoices-and-receipts_ocr_v1, created by the Qwen team.
All weights, files and behaviour… See the full description on the dataset page: https://huggingface.co/datasets/NeuralMetrics/invoices-and-receipts-ocr-v1. |
| [harsha-desaraju/telugu-line-ocr-bench](https://huggingface.co/datasets/harsha-desaraju/telugu-line-ocr-bench) | 2026-08-09 | text-recognition | candidate | 
	
		
	
	
		Telugu Wikisource OCR — human-verified line crops
	

1044 single-line crops from Telugu Wikisource page scans, each with a
transcription checked against the image by a human. Grayscale, height 64px,
width a multiple of 8 — the form the encoder consumes.

	
		
	
	
		Columns
	


	
		
column
meaning


		
image
the line crop


text
gold transcription, human-verified


n_graphemes
akshara count of text (regex.\X)


has_english
text contains a Latin-script letter. Digits/punctuation do… See the full description on the dataset page: https://huggingface.co/datasets/harsha-desaraju/telugu-line-ocr-bench. |
| [Ba2han/trl-ocr-dataset](https://huggingface.co/datasets/Ba2han/trl-ocr-dataset) | 2026-08-09 | text-recognition | candidate | — |
| [themohal/saraiki-synthetic-ocr-dataset](https://huggingface.co/datasets/themohal/saraiki-synthetic-ocr-dataset) | 2026-08-08 | text-recognition | candidate | — |
| [SeeWye/Nondeterministic_Finite_Automata_OCR_Conversations_Format](https://huggingface.co/datasets/SeeWye/Nondeterministic_Finite_Automata_OCR_Conversations_Format) | 2026-08-08 | text-recognition | candidate | — |
| [jpeglle/epstein-files-ocr-complete](https://huggingface.co/datasets/jpeglle/epstein-files-ocr-complete) | 2026-08-08 | text-recognition | candidate | 
	
		
	
	
		Epstein Files — Complete OCR Dataset
	


This is a comprehensive, structured publication of the Epstein Files OCR dataset, significantly expanding upon the earlier Datasets 1-8 release.


	
		
	
	
		Dataset Summary
	

This dataset contains page-level OCR output compiled from an extensive release of documents related to Jeffrey Epstein / the Epstein case.
Each row in this dataset represents one scanned PDF document from the original release using a proprietary automated OCR pipeline… See the full description on the dataset page: https://huggingface.co/datasets/jpeglle/epstein-files-ocr-complete. |
| [Congo-digital-service/ocr-lingala-dataset-augmented](https://huggingface.co/datasets/Congo-digital-service/ocr-lingala-dataset-augmented) | 2026-08-08 | text-recognition | candidate | — |
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
