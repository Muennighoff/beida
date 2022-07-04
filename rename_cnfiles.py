import argparse
import os
import requests

def parse_args():
    # Parse command line arguments
    parser = argparse.ArgumentParser()

    parser.add_argument("--dir", type=str, default="./", help="Path to dir within all files in all folders will be renamed")
    parser.add_argument("--gjson", type=str, default=None, help="Path to G Cloud Service Key JSON for translation API")

    args = parser.parse_args()
    return args

# Quality not good enough - bad for single words
#from transformers import AutoModelWithLMHead, AutoTokenizer, pipeline
#model = AutoModelWithLMHead.from_pretrained("Helsinki-NLP/opus-mt-zh-en")
#tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-zh-en")
#translation = pipeline("translation_en_to_zh", model=model, tokenizer=tokenizer)


# From GCloud - Make sure to have json file
def translate_text(target, text):
    """Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages

    (pip install --upgrade google-api-python-client)
    pip install google-cloud-translate
    """
    import six
    from google.cloud import translate_v2 as translate

    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target)

    print(u"Text: {}".format(result["input"]))
    print(u"Translation: {}".format(result["translatedText"]))
    print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))

    return result["translatedText"]

accept_chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_-+-(). "

def check_rename(entry, full_path):
    """
    Presents option to rename files with invalid chars.
    """
    print(entry)

    if " " in entry:
        out = input("Remove space from: {} ? (Just hit ENTER for NO)".format(entry))
        if len(out) > 0:
            new_entry = entry.replace(" ", "")
            new_path = full_path.replace(entry, new_entry)

            os.rename(full_path, new_path)

            entry = new_entry
            full_path = new_path

    not_accept = ''
    for char in entry:
        if char not in accept_chars:
            # Rectify
            not_accept += char

    if len(not_accept) > 0:
        # Translate
        accept = "".join([i for i in entry if i not in not_accept])
        translated = "".join([i for i in "_".join(translate_text("en", not_accept).split(" ")).lower() if i in accept_chars])

        new_entry = translated + accept

        out = input("Rename {}  --->  {} ? (Just hit ENTER for NO)".format(entry, new_entry))
        if len(out) > 0:
            new_path = full_path.replace(entry, new_entry)

            os.rename(full_path, new_path)

            entry = new_entry
            full_path = new_path

    return entry, full_path

def iterate_files(dir):
    """
    Iterates through all files
    """
    # create a list of file and sub directories 
    # names in the given directory 
    file_list = os.listdir(dir)
    all_files = list()
    # Iterate over all the entries
    for entry in file_list:
        # Create full path & check name
        full_path = os.path.join(dir, entry)
        print(full_path)
        new_entry, new_path = check_rename(entry, full_path)

        if entry != new_entry:
            print("Renamed {} ----> {}\nNew Path: {}".format(entry, new_entry, new_path))
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(new_path):
            all_files = all_files + iterate_files(new_path)
        else:
            all_files.append(new_path)
                
    return all_files


if __name__ == "__main__":
    args = parse_args()

    if args.gjson is not None:
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=args.gjson

    x = iterate_files(args.dir)


    