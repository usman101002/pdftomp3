import pdfplumber
import gtts
from art import tprint
from pathlib import Path

def pdf_to_mp3(file_path='test.pdf', language = 'en'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        print('Работа в процессе...')
        print('Если хотите быстрее завершить, то нажмите на кнопку))')

        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
        text = ''.join(pages)
        text = text.replace('\n', '')

        my_audio = gtts.gTTS(text=text, lang=language, slow = False)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')
        return f'{file_name}.mp3 saved successfully.'

    else:
        return 'Файл не существуент или он некорректен'

def main():
    tprint('PDF TO MP3')
    print(pdf_to_mp3(file_path='english.pdf'))


if __name__ == '__main__':
    main()