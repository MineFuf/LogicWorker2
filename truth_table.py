from typing import Tuple, List, Union
from pathlib import Path


class TruthTable:
    def __init__(self, path: Union[str, Path] = None,
                 data: Tuple[Union[str, List[bool]], Union[str, List[bool]]] = None):
        def error():
            raise TypeError('Invalid File')

        def read_data(data: str):
            if not v2:
                data = data.split(',')

            return [False if it == '0' else True if it == '1' else error() for it in data]

        if path is not None:
            v2 = Path(path).suffix == '.tbl2'  # enable v2 formating if filename ends with .tbl2
            self.i, self.o = [], []

            with open(path, 'r') as f:
                self.i_n, self.o_n = 0, 0
                while (line := f.readline().strip()) != '':
                    data = line.split(' ')
                    if len(data) != 2:
                        error()
                    if (len(data[0]) == self.i_n or self.i_n == 0) and (len(data[1]) == self.o_n or self.o_n == 0):
                        self.i_n = len(data[0])
                        self.o_n = len(data[1])
                        self.i.append(read_data(data[0]))
                        self.o.append(read_data(data[1]))
                    else:
                        error()
                if len(self.i) == 0:
                    error()
        else:
            # TODO Implement TruthTable contructor for creating without path
            raise NotImplementedError('Creating TruthTable by inputs and outputs not implemented yet')

        print(self.i)
        print(self.o)
