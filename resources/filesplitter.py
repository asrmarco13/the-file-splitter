import os


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
            "Splitting %s into multiple files with %s lines"
            % (
                os.path.join(self.working_dir, self.file_base_name + self.file_ext),
                str(self.row_count),
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

        print("Created %s files." % (str(file_number - 1)))

    def split(self, file_number: int) -> str:
        """return a new file object ready to write to"""
        new_file_name = "%s.%s%s" % (
            self.file_base_name,
            str(file_number),
            self.file_ext,
        )
        new_file_path = os.path.join(self.working_dir, new_file_name)
        print("creating file %s" % (new_file_path))
        return new_file_path
