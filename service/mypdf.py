import image
import pdf2image, imageio
import time
import os


# DECLARE CONSTANTS
# PDF_PATH = "/home/userd618/Documents/opencv/Not Original Test/doc01119020200302151247_001.pdf"
def f2i(path):
    DPI = 200
    OUTPUT_FOLDER = None
    FIRST_PAGE = None
    LAST_PAGE = None
    FORMAT = 'jpg'
    THREAD_COUNT = 1
    USERPWD = None
    USE_CROPBOX = False
    STRICT = False
    index = 0

    # This method reads a pdf and converts it into a sequence of images
    # PDF_PATH sets the path to the PDF file
    # dpi parameter assists in adjusting the resolution of the image
    # output_folder parameter sets the path to the folder to which the PIL images can be stored (optional)
    # first_page parameter allows you to set a first page to be processed by pdftoppm
    # last_page parameter allows you to set a last page to be processed by pdftoppm
    # fmt parameter allows to set the format of pdftoppm conversion (PpmImageFile, TIFF)
    # thread_count parameter allows you to set how many thread will be used for conversion.
    # userpw parameter allows you to set a password to unlock the converted PDF
    # use_cropbox parameter allows you to use the crop box instead of the media box when converting
    # strict parameter allows you to catch pdftoppm syntax error with a custom type PDFSyntaxError
    # path_1 = os.getcwd()
    path_1 = os.path.join(os.getcwd(), 'images')

    try:
        os.makedirs(path_1, exist_ok=True)
        print("Directory '%s' created successfully" % path_1)
    except OSError as error:
        os.remove(path_1)
        os.makedirs(path_1)
        print("Directory deleted and created")
    images = [[]]
    start_time = time.time()
    dirs = os.listdir(path)
    # print(len(dirs))
    for file in dirs:
        if file.endswith("pdf"):
            path1 = path + "/" + file
            pil_images = pdf2image.convert_from_path(path1, dpi=DPI, output_folder=OUTPUT_FOLDER, first_page=FIRST_PAGE,
                                                     last_page=LAST_PAGE, fmt=FORMAT, thread_count=THREAD_COUNT,
                                                     userpw=USERPWD, use_cropbox=USE_CROPBOX, strict=STRICT)
            #         images.append(pil_images)
            print("Time taken : " + str(time.time() - start_time))
            pathB = os.getcwd()
            os.chdir(path_1)
            # This method helps in converting the images in PIL Image file format to the required image format
            # for image in pil_images:
            for image in pil_images:
                image.save("page" + str(index) + ".jpg")
                index += 1
            os.chdir(pathB)
    # return path_1
