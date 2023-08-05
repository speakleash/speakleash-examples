import os

from speakleash import Speakleash


def save_high_quality_docs(txt_folder_name):
    """
    :param txt_folder_name: The name of the folder where the high-quality documents will be saved.
    :return: None

    This method saves high-quality documents from the Speakleash dataset to a specified folder.
    It creates the necessary directories if they don't already exist.

    Example usage:
    save_high_quality_docs("txt_folder")
    """
    base_dir = os.path.join(".")
    speakleash_dir = os.path.join(base_dir, "datasets")
    replicate_to_txt = os.path.join(base_dir, txt_folder_name)

    if not os.path.exists(speakleash_dir):
        os.makedirs(speakleash_dir)
    if not os.path.exists(replicate_to_txt):
        os.makedirs(replicate_to_txt)

    sl = Speakleash(speakleash_dir)
    name = "plwiki"
    limit = 500
    counter = 0
    ds = sl.get(name).ext_data

    for doc in ds:
        txt, meta = doc

        if meta.get("quality", "") == 'HIGH':
            print("High-quality document")
            with open(os.path.join(replicate_to_txt, f'high_quality_doc_{counter}.txt'), 'w') as out_file:
                out_file.write(txt)
            counter = counter + 1
            if counter > limit:
                break


save_high_quality_docs("datasets_high_quality_txt")
