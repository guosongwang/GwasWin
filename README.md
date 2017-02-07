# GwasWin
The script is used for creating sliding window and perform defined calculations for Genome-wide Association Study results. Right now, the script is very primary and can only create non-overlapping sliding window for beta value. Currently only support bovine genome (UMD3.1.x). More functions coming soon. 

# Installation
## Running Environment
Python 2.7.x
## Installation
Download `GwasWin.py` in this repo. You can put it anywhere you want. 

# Usage
## Basic Usage
In terminal, type:
```
python /your/path/GwasWin.py [Options] input_file
```

## Available Options
```
-h, --help            show this help message and exit
-o, --output_path     Define output path. Please provide the path ended with "/". 
-s, --size_window     Define window size. Unit: 1 base-pair. 
```
## Example
Below is an example of handling Gemma results. I defined the window size as 2Mb. 
```
python /my/path/GwasWin.py -s 2000000 -o /my/output/path/ /my/input/path/test.assoc
```
# Results
Four columns will be generated:
```
chromosome  window_start  window_end  value
```
One thing should be noticed is that, the result hasn't been sorted, yet. 
