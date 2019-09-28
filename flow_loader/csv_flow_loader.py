"""
    FlowCSVLoader: Loads the csv file generated by CIC Flowmeter and reads new entries generated by it.
"""
import time

class CSVFlowLoader(object):
    def __init__(self, csv_filename):
        self.csv_filename = csv_filename
        self.csvfile = open(csv_filename)

    # tailFile: Generator that yields new entries into the csv file.
    def tailFile(self, *args, **kwargs):
        self.csvfile.seek(0,2)
        while True:
            line = self.csvfile.readline()
            if not line:
                time.sleep(0.1)
                continue
            yield line        