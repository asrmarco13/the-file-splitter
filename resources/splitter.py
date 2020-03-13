import argparse
import os
from resources.filesplitter import FileSplitter


class Splitter():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f",
                        "--filename",
                        type=str,
                        required=True,
                        help="Option -f <filename> is required")
    parser.add_argument("-r",
                        "--row-count",
                        type=int,
                        help="Row count (default is 1000)")
    parser.add_argument("-e",
                        "--encoding",
                        type=str,
                        help="File encoding (default is utf-8)")

    def run(self):
        args = Splitter.parser.parse_args()
        filename = args.filename
        row_count = Splitter.is_row_count(args.row_count)
        encoding = Splitter.is_encoding(args.encoding)
        working_dir = os.getcwd()
        file_base_name, file_ext = os.path.splitext(filename)
        fs = FileSplitter(filename,
                          file_base_name,
                          file_ext,
                          working_dir,
                          row_count,
                          encoding)
        fs.out()

    def is_row_count(row_count):
        if row_count is None:
            row_count = 1000

        return row_count

    def is_encoding(encoding):
        if encoding is None:
            encoding = "utf-8"

        return encoding
