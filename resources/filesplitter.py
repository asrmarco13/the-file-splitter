import os
import constants


class FileSplitter:
    def __init__(
        self,
        filename: str,
        file_base_name: str,
        file_ext: str,
        working_dir: str,
        row_count: int,
        encoding: str,
    ):
        self.filename = filename
        self.file_base_name = file_base_name
        self.file_ext = file_ext
        self.working_dir = working_dir
        self.row_count = row_count
        self.encoding = encoding

    def out(self) -> None:
        """ Split file and print result """
        file_number = 1
        split_file = None

        print(
            constants.INITIAL_SPLIT_HELP.format(
                FileSplitter.path_join(self.working_dir, self.filename), self.row_count
            )
        )

        with open(self.filename, "r", encoding=self.encoding) as f:
            for count, line in enumerate(f):
                if count % self.row_count == 0:
                    if split_file:
                        split_file.close()
                    split_file_path = self.split(file_number)
                    file_number += 1
                    split_file = open(split_file_path, "w")
                split_file.write(line)
            if split_file:
                split_file.close()

        file_number = FileSplitter.total_file_number(file_number)
        print(
            constants.TOTAL_FILES_CREATED_HELP.format(
                file_number, FileSplitter.is_single_split_file(file_number)
            )
        )

    def split(self, file_number: int) -> str:
        """return a new file object ready to write to"""
        new_file_name = "{}.{}{}".format(
            self.file_base_name, file_number, self.file_ext,
        )
        new_file_path = FileSplitter.path_join(self.working_dir, new_file_name)
        print(constants.CREATE_FILES_HELP.format(new_file_path))
        return new_file_path

    @staticmethod
    def path_join(*paths: str) -> str:
        return os.path.join(*paths)

    @staticmethod
    def total_file_number(file_number: int) -> int:
        return file_number - 1

    @staticmethod
    def is_single_split_file(file_number: int) -> str:
        if file_number > 1:
            return "files"

        return "file"
