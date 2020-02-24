import os


class FileReader:

    def __init__(self, filename):
        self.filename = filename

    # regular read method - returns list of elements in the file
    def e_read(self):
        return_list = []

        with open(os.path.dirname(os.path.realpath(__file__)) + '\\' + self.filename) as fd:
            for line in fd:
                for el in line.strip().split():
                    return_list.append(el)

        return return_list

    # Ex. 5 read method - returns TODO: ???
    def e_5_read(self):
        return_list = []
        line_num = 0

        with open(self.filename) as fd:
            for line in fd:
                if line_num % 2 == 1:
                    return_list.append(line)
                line_num += 1
        return return_list

    def e_14_read(self):
        return_list = []

        with open(self.filename) as fd:
            for line in fd:
                return_list.append(line.strip())
        return return_list

    def write_to_file(self, filename, elements):
        try:
            # writes the elements to the file
            with open(os.path.dirname(os.path.realpath(__file__)) + '\\outputs\\' + filename, 'w') as fd:
                for line in elements:
                    fd.write(line)
            return '[OK]'
        except Exception as e:
            print('Exception raised when trying to write a file; ' + str(e))
            return '[ERROR]'

    def write_to_file_7(self, filename, elements):
        try:
            # writes the elements to the file
            with open(os.path.dirname(os.path.realpath(__file__)) + '\\outputs\\' + filename, 'w') as fd:
                    line = str(elements[0]) + ' ' + str(elements[1]) + ' ' + str(elements[2]) + ' ' + str(elements[3])
                    fd.write(line)
            return '[OK]'
        except Exception as e:
            print('Exception raised when trying to write a file; ' + str(e))
            return '[ERROR]'
