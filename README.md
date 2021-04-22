# pdf_stamp
---
## Requirements

Python 3.8 or later with all requirements.txt dependencies installed. To install run:
`
pip install -U -r requirements.txt
`
---
##stamping
`
python pdf_stamp.py --source --output --x --y --w --h --page
`
optional arguments:
  -h, --help       show this help message and exit
  --source SOURCE  pdf input path
  --output OUTPUT  pdf output path
  --x X            x coord of stamp
  --y Y            y coord of stamp
  --w W            width of stamp
  --h H            height of stamp
  --page PAGE      stamping page
