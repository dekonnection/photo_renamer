"""photo_renamer

A simple script to rename your ugly and inconsistently named pictures, to something usable.
"""
from argparse import ArgumentParser, FileType
from datetime import datetime
from exif import Image
from os import rename
from os.path import basename, dirname, join, splitext
from sys import exit


def parse_args(args=None):
    """Parse CLI arguments."""
    parser = ArgumentParser(description="rename photos properly according to EXIF data")
    parser.add_argument(
        "-f",
        "--files",
        required=True,
        nargs="+",
        help="File(s) to rename, separated by spaces",
    )
    return parser.parse_args(args)


def build_rename_dict(file_list):
    rename_dict = {}
    for file in file_list:
        path = dirname(file)
        extension = splitext(file)[1]
        new_name = gen_new_name(file)

        new_full_path = join(path, new_name + extension)

        rename_dict[file] = new_full_path
    return rename_dict


def gen_new_name(filepath):
    with open(filepath, 'rb') as file:
        image = Image(file)
        if not image.has_exif:
            print(
                f"ERROR : '{file.name}' is not a supported image, we will exit. Nothing has been renamed."
            )
            exit(1)

        original_name = splitext(basename(file.name))[0]
        date_id = datetime.strptime(image.datetime_original, "%Y:%m:%d %H:%M:%S").strftime(
            "%Y%m%d-%H%M%S"
        )

        new_name = f"{date_id}_{image.model}_{original_name}"
        return new_name


def massive_rename(rename_dict, dry=False):
    for old_name, new_name in rename_dict.items():
        if dry:
            status = "(preview)"
        else:
            try:
                rename(old_name, new_name)
                status = "OK (renamed successfully)"
            except PermissionError:
                status = "KO (permission error)"
            except Exception as message:
                status = f"KO ({message})"
        print(f"{old_name} => {new_name} : {status}")


def main():
    args = parse_args()
    print(
        "Welcome to photo_renamer !\n(this is unsupported software, please make backups before using it)\n"
    )

    print('Analyzing files ...\n')
    rename_dict = build_rename_dict(args.files)

    print("\nYour files would be renamed like this :\n")
    massive_rename(rename_dict, dry=True)

    rename_confirmation = input("\nIs this OK with you ? (y/N)")
    if rename_confirmation == "y":
        print("\nRenaming :\n")
        massive_rename(rename_dict)
    else:
        print("Nothing has been renamed, we will exit.")
        exit(0)


main()
