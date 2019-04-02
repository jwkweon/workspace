import cv2
import argparse
import os
import shutil

def main():
    parser = argparse.ArgumentParser()

    #인자 값 등록 -h 로 help 명령  실행 가능
    parser.add_argument("--dir", required = True, help = 'input dir')
    parser.add_argument("--o", required = True, help = 'output dir')

    args = parser.parse_args()
    dir = args.dir
    outdir = args.o

    dir = './' + dir
    outdir = './' + outdir

    #input 이나 output dir이 없는 경우 폴더 생성
    if not os.path.exists(dir):
        os.makedirs(dir)

    if not os.path.exists(outdir):
        os.makedirs(outdir)

    os.chdir(dir)

    #경로 내 파일명을 읽어오기
    for i, img_file in enumerate(os.listdir('./')):
        #읽어온 파일명(이미지)으로 cv read
        img = cv2.imread(img_file)
        height, width, _ = img.shape

        #이미지 학습 셋에 따라 resize 실행
        img = cv2.resize(img , (width // 2 , height // 2))

        #파일명을 숫자.jpg 또는 숫자.png 처럼 수정하기
        result_img = str(i + 1) + img_file[-4:]

        #결과 저장하기
        cv2.imwrite(result_img, img)

        #이미지 복사
        shutil.copy(result_img, '../' + outdir)


if __name__ == '__main__':
    main()
