# pdf_stamp
![캡처](https://user-images.githubusercontent.com/64114699/115660743-6ec87a00-a377-11eb-9b28-64530ce393b4.JPG)

## Requirements
Python 3.8 or later with all requirements.txt dependencies installed. To install run:  
`
pip install -U -r requirements.txt
`

## stamping
```
python pdf_stamp.py --source --output --x --y --w --h --page  

optional arguments:  
    -h, --help       show this help message and exit  
    --source SOURCE  pdf input path  
    --output OUTPUT  pdf output path  
    --x X            x coord of stamp  
    --y Y            y coord of stamp  
    --w W            width of stamp  
    --h H            height of stamp  
    --page PAGE      stamping page  
`
