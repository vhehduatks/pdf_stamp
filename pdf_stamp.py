import PyPDF2
import argparse
import os.path
from glob import glob
from reportlab.pdfgen import canvas



#only png available masking
def make_stamp(stamp,x,y,w=None,h=None):
    c=canvas.Canvas('stamp.pdf')
    mask=[255,255,255,255,255,255]
    c.drawImage(stamp, x=x, y=y, width=w, height=h, mask=mask)
    c.save()

def make_output(opt):
    pdf_Path,save_Path,x,y,w,h,page=\
        opt.source,opt.output,opt.x,opt.y,opt.w,opt.h,opt.page

 
    if w+h>0:
        make_stamp('stamp.jpg',x,y,w,h)
    else:
        make_stamp('stamp.jpg',x,y)

    condition='/*.pdf'
    for path in glob(pdf_Path+condition):
        input_pdf=PyPDF2.PdfFileReader(open(path,'rb'))
        stamp_pdf=PyPDF2.PdfFileReader(open('stamp.pdf','rb'))
        output_pdf=PyPDF2.PdfFileWriter()
        file_name=path.split('\\')
        file_name=file_name[-1]
        input_page_num=0
        total_page=input_pdf.getNumPages()

        if opt.page>=total_page:
            print('input page:',opt.page,file_name,'page max:',total_page-1)
            return 0

        if opt.page !=-1:
            input_page_num=opt.page
        else:
            input_page_num=total_page-1 
        for i in range(total_page):
            input_page=input_pdf.getPage(i)
            if i==input_page_num:
                coord='('+str(opt.x)+','+str(opt.y)+')'
                print('stamp in :',file_name,'%4d'%i,'page :','coord',coord)
                input_page.mergePage(stamp_pdf.getPage(0))
            output_pdf.addPage(input_page)


        with open(save_Path+'/output_'+file_name,'wb') as f3:
            output_pdf.write(f3)



if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--source', type=str,default='source', help='pdf input path')
    parser.add_argument('--output', type=str,default='output', help='pdf output path')
    parser.add_argument('--x', type=int,default=10, help='x coord of stamp')
    parser.add_argument('--y', type=int,default=10, help='y coord of stamp')
    parser.add_argument('--w', type=int,default=0, help='width of stamp')
    parser.add_argument('--h', type=int,default=0, help='height of stamp')
    parser.add_argument('--page', type=int,default=-1, help='stamping page')
    args=parser.parse_args()


    make_output(args)
