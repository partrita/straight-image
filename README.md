# batch scanner

학회사진을 비스듬하게 찍어서 보기가 힘들어서 편집하는 것을 만들었습니다.

## Batch Image Straightener

A Python-based tool for automatically detecting and correcting skew in batches of images.

### Key Features:

- **Automatic Skew Detection**: Utilizes computer vision techniques to identify the angle of skew in images.
- **Batch Processing**: Efficiently handles large sets of images for streamlined workflow.
- **Customizable Parameters**: Allows fine-tuning of skew correction angles and thresholds.
- **Multiple File Format Support**: Works with common image formats like JPEG, PNG, and TIFF.
- **Preservation of Image Quality**: Maintains image integrity during the straightening process.
- **Progress Tracking**: Provides real-time feedback on batch processing status.
- **Output Options**: Saves corrected images with customizable naming conventions.

### How It Works:

1. **Image Loading**: Reads images from a specified directory.
2. **Skew Detection**: Analyzes each image to determine the angle of skew.
3. **Rotation Correction**: Applies calculated rotation to straighten the image.
4. **Output Generation**: Saves the corrected images to a designated folder.

This tool is ideal for researchers, archivists, and anyone dealing with large volumes of scanned documents or photographs that require alignment correction.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

- python 2.7
- numpy
- openCV

What things you need to install the software and how to install them

### Installing

A step by step series of examples that tell you have to get a development env running

conda를 사용해서 openCV 설치하기

```bash
conda install -c menpo opencv
```


Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

```batch
python batch_scan.py -p images/
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc

