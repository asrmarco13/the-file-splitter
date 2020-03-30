import argparse
import os
import constants
from resources.filesplitter import FileSplitter


class Splitter:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--filename",
        type=str,
        required=True,
        help=constants.FILENAME_REQUIRED_HELP,
    )
    parser.add_argument("-r", "--row-count", type=int, help=constants.ROW_COUNT_HELP)
    parser.add_argument("-e", "--encoding", type=str, help=constants.ENCODING_HELP)

    @classmethod
    def run(cls) -> None:
        args = Splitter.parser.parse_args()
        filename = args.filename
        row_count = Splitter.is_row_count(args.row_count)
        encoding = Splitter.is_encoding(args.encoding)
        working_dir = os.getcwd()
        file_base_name, file_ext = os.path.splitext(filename)
        fs = FileSplitter(
            filename, file_base_name, file_ext, working_dir, row_count, encoding
        )
        fs.out()

    @staticmethod
    def is_row_count(row_count: int) -> int:
        if row_count is None:
            row_count = constants.ROW_COUNT

        return row_count

    @staticmethod
    def is_encoding(encoding: str) -> str:
        if encoding is None:
            encoding = constants.ENCODING

        return encoding
