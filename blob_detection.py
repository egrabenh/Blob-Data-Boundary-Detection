
'''
'''
class BlobData():
    '''
    '''
    def __init__(self, input_file):
        self.input_file = input_file
        self.blob_input_data_structure = {}
        self.file_contents = []
        self._read_file()


    # Read sample blob data from text file
    def _read_file(self):
        file = open(self.input_file)
        hash = 0
        for line in file:
            # Save file_contents for printing later
            self.file_contents.append(line.rstrip('\n'))
            line = line.rstrip('\n')
            for c in line:
                self.blob_input_data_structure[hash] = [c, "new"]
                hash += 1
        file.close()

'''
'''
class FindCells():
    '''
    '''
    def __init__(self, blob_dictionary):
        self.blob_input_data_structure = blob_dictionary
        self.current_pos = {'row': 0, 'col': 0}
        self.location = {'top': 10, 'bottom': 0, 'left': 10, 'right': 0}
        self.reads_count = 0


    def find_blob(self):
        for key in self.blob_input_data_structure:
            if self.blob_input_data_structure[key][0] == '1':
                self.search_boolean_grid(key)


    def search_boolean_grid(self, key):
        self.update_position(key)
        self.reads_count += 1
        # Left
        try:
            if self.evaluate_blob(key-1):
                if self.location['left'] > self.current_pos['col']:
                    self.location['left'] = self.current_pos['col']
                self.search_boolean_grid(key-1)
        except KeyError:
            # Caught the left edge
            pass
        # Down
        try:
            if self.evaluate_blob(key+10):
                if self.location['bottom'] < self.current_pos['row']:
                    self.location['bottom'] = self.current_pos['row']
                self.search_boolean_grid(key+10)
        except KeyError:
            # Caught the bottom edge
            pass
        # Right
        try:
            if self.evaluate_blob(key+1):
                if self.location['right'] < self.current_pos['col']:
                    self.location['right'] = self.current_pos['col']
                self.search_boolean_grid(key+1)
        except KeyError:
            # Caught the right edge
            pass
        # Up
        try:
            if self.evaluate_blob(key-10):
                if self.location['top'] > self.current_pos['row']:
                    self.location['top'] = self.current_pos['row']
                self.search_boolean_grid(key-10)
        except KeyError:
            # Caught the top edge
            pass

        # The outer edges of the blob needs to be checked
        self.edge_position_update()


    def edge_position_update(self):
        # Left
        if self.location['left'] > self.current_pos['col']:
            self.location['left'] = self.current_pos['col']
        # Down
        if self.location['bottom'] < self.current_pos['row']:
            self.location['bottom'] = self.current_pos['row']
        # Right
        if self.location['right'] < self.current_pos['col']:
            self.location['right'] = self.current_pos['col']
        # Up
        if self.location['top'] > self.current_pos['row']:
            self.location['top'] = self.current_pos['row']


    def evaluate_blob(self, key):
        blob = False
        if self.blob_input_data_structure[key][0] == '1' and \
           self.blob_input_data_structure[key][1] == "new":
            blob = True
            self.blob_input_data_structure[key][1] = "old"
        return blob

    def update_position(self, key):
        if key == 0:
            self.current_pos['row'] = 0
        else:
            row = int(key/10)
            self.current_pos['row'] = row

        col = key % 10
        self.current_pos['col'] = col

'''
'''
class PrintedResults():
    '''
    '''
    def __init__(self, input_file, edges, cells_read):
        self.input_file = input_file
        self.edges = edges
        self.cells_read = cells_read
        self.generate_printed_results()


    def generate_printed_results(self):
        print("Sample input:")
        print('\n'.join(self.input_file))
        print("\nSample Output:")
        print("Cell Reads: {}".format(self.cells_read))
        print("Top: {}".format(self.edges['top']))
        print("Left: {}".format(self.edges['left']))
        print("Bottom: {}".format(self.edges['bottom']))
        print("Right: {}".format(self.edges['right']))


if __name__ == '__main__':
    input_file = 'sampleInput.txt'
    file_data = BlobData(input_file)
    file_contents = file_data.file_contents
    blob_input_data_structure = file_data.blob_input_data_structure
    find_cells = FindCells(blob_input_data_structure)
    find_cells.find_blob()
    reads_count = find_cells.reads_count
    edges = find_cells.location
    PrintedResults(file_contents, edges, reads_count)