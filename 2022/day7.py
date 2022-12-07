from day_base import Day


class Directory:
    """
    A directory has a name, files and subdirectories.
    """

    def __init__(self, name, parent=None):
        self.name = name
        self.files = []
        self.sub_dirs = []
        self.parent = parent

    def add_file(self, name, size) -> None:
        """
        Adds a file with a given name and size to this directory
        :param name: The name of the file to be added
        :param size: The size of the file to be added
        """
        self.files.append((name, size))

    def add_dir(self, directory) -> None:
        """
        Adds a new directory to this directory
        :param directory: The directory
        """
        self.sub_dirs.append(directory)

    def get_size(self) -> int:
        """
        Get the total size of this directory
        :return: The total size of this directory and all of its subdirectories
        """
        return sum(file[1] for file in self.files) + sum(directory.get_size() for directory in self.sub_dirs)

    def __str__(self):
        return self.name


def get_all_directory_sizes(directory: Directory) -> list[tuple[str, int]]:
    """
    Determine the size of this directory and the sizes of all of its subdirectories
    :param directory: The directory to find the subdirectories of and their sizes
    :return: A list of tuples containing the size of each subdirectory and this directory and their names
    """
    directories = [(directory.name, directory.get_size())]
    for sub_dir in directory.sub_dirs:
        directories += get_all_directory_sizes(sub_dir)
    return directories


class Day7(Day):

    def __init__(self):
        super().__init__(2022, 7, 'No Space Left On Device', expected_a=95437, expected_b=24933642, debug=False)

    def generate_directory_structure(self):
        """
        Generate a directory structure based on the instructions and file structure as exposed during the commandline
        instructions and feedback
        :return: The root directory object containing the file system
        """
        current_path = []
        current_dir = None
        main_dir = Directory("/")
        for line in self.input:
            if line[0] == "$":
                # This is a command that needs to be executed
                command = line[2:]
                if command == "ls":
                    continue
                else:
                    _, directory = command.split(' ')
                    if directory == "..":
                        current_path.pop()
                        current_dir = current_dir.parent
                    elif directory == "/":
                        current_path = ['/']
                        current_dir = main_dir
                    else:
                        current_path.append(f"{directory}/")
                        new_dir = Directory("".join(current_path), current_dir)
                        current_dir.add_dir(new_dir)
                        current_dir = new_dir
            else:
                # This is a file stack
                size, filename = line.split(" ")
                if size == "dir":
                    continue
                current_dir.add_file(filename, int(size))

        return main_dir

    def part_a(self) -> int:
        main_dir = self.generate_directory_structure()
        all_sizes = get_all_directory_sizes(main_dir)
        return sum(size for (_, size) in all_sizes if size <= 100000)

    def part_b(self) -> int:
        main_dir = self.generate_directory_structure()
        total_disk_size = 70000000
        required_size = 30000000
        to_remove = required_size - (total_disk_size - main_dir.get_size())
        all_sizes = get_all_directory_sizes(main_dir)

        return min([size for (_, size) in all_sizes if size >= to_remove])


if __name__ == '__main__':
    (Day7()).run()
