"""
The main code for the Strings-to-Vectors assignment. See README.md for details.
"""
from typing import Sequence, Any

import numpy as np


class Index:
    """
    Represents a mapping from a vocabulary (e.g., strings) to integers.
    """

    def __init__(self, vocab: Sequence[Any], start=0):
        """
        Assigns an index to each unique item in the `vocab` iterable,
        with indexes starting from `start`.

        Indexes should be assigned in order, so that the first unique item in
        `vocab` has the index `start`, the second unique item has the index
        `start + 1`, etc.
        """

        #Creating a dictionary with blank values, then assigning based on number of unique keys
        self.start = start
        dictionary = dict.fromkeys(vocab)
        dictionary = dict(zip(dictionary,np.arange(self.start,len(dictionary) + \
                                                   self.start)))
        self.dict = dictionary

    def objects_to_indexes(self, object_seq: Sequence[Any]) -> np.ndarray:
        """
        Returns a vector of the indexes associated with the input objects.

        For objects not in the vocabulary, `start-1` is used as the index.

        :param object_seq: A sequence of objects.
        :return: A 1-dimensional array of the object indexes.
        """

        #Providing a key, returning the corresponding index if it exists, else self.start - 1
        indexs = []
        for value in object_seq:
            indexs.append(self.dict.get(value,self.start-1))
        indexs = np.array(indexs)

        return indexs

    def objects_to_index_matrix(
            self, object_seq_seq: Sequence[Sequence[Any]]) -> np.ndarray:
        """
        Returns a matrix of the indexes associated with the input objects.

        For objects not in the vocabulary, `start-1` is used as the index.

        If the sequences are not all of the same length, shorter sequences will
        have padding added at the end, with `start-1` used as the pad value.

        :param object_seq_seq: A sequence of sequences of objects.
        :return: A 2-dimensional array of the object indexes.
        """

        #Providing a key, returning the corresponding index if it exists, else self.start - 1
        columns = []
        for obj in object_seq_seq:
            rows = []
            for index in obj:
                rows.append(self.dict.get(index,self.start-1))
            rows = np.array(rows)
            columns.append(rows)
        indexs = columns

        #Finding the maximum row length in the matrix
        maximum = 0
        for value in indexs:
            if len(value) > maximum:
                maximum = len(value)

        #Adding the self.start-1 padding for rows that are not max length
        new_indexs = []
        for obj in indexs:
            new_rows = []
            length = len(obj)
            for j in range(0,maximum):
                if j > length - 1:
                    new_rows.append(self.start - 1)
                else:
                    new_rows.append(obj[j])
            new_rows = np.array(new_rows)
            new_indexs.append(new_rows)
        new_indexs = np.array(new_indexs)

        return new_indexs

    def objects_to_binary_vector(self, object_seq: Sequence[Any]) -> np.ndarray:
        """
        Returns a binary vector, with a 1 at each index corresponding to one of
        the input objects.

        :param object_seq: A sequence of objects.
        :return: A 1-dimensional array, with 1s at the indexes of each object,
                 and 0s at all other indexes.
        """

        #Adding the front padding
        beginning = np.zeros(self.start)
        binary = np.zeros(len(self.dict))

        #Calling the objects_to_indexs function to retrieve the indexs of the provided keys
        indexs = self.objects_to_indexes(object_seq)

        for value in indexs:
            binary[value - self.start] = 1

        binary = np.concatenate((beginning,binary))

        return binary

    def objects_to_binary_matrix(
            self, object_seq_seq: Sequence[Sequence[Any]]) -> np.ndarray:
        """
        Returns a binary matrix, with a 1 at each index corresponding to one of
        the input objects.

        :param object_seq_seq: A sequence of sequences of objects.
        :return: A 2-dimensional array, where each row in the array corresponds
                 to a row in the input, with 1s at the indexes of each object,
                 and 0s at all other indexes.
        """

        #Forming a list of sorted key values to compare with object_seq_seq
        binary = []
        sort = sorted(self.dict, key=self.dict.get)

        for value in object_seq_seq:
            row = np.zeros(self.start)
            for new_value in sort:
                if new_value in value:
                    row = np.append(row,1)
                else:
                    row = np.append(row,0)
            binary.append(row)

        binary = np.array(binary)
        return binary

    def indexes_to_objects(self, index_vector: np.ndarray) -> Sequence[Any]:
        """
        Returns a sequence of objects associated with the indexes in the input
        vector.

        If, for any of the indexes, there is not an associated object, that
        index is skipped in the output.

        :param index_vector: A 1-dimensional array of indexes
        :return: A sequence of objects, one for each index.
        """

        #Providing an index, pulls the corresponding keys from the dictionary
        objects = []
        for index in index_vector:
            for key,value in self.dict.items():
                if index == value:
                    objects.append(key)

        return objects

    def index_matrix_to_objects(
            self, index_matrix: np.ndarray) -> Sequence[Sequence[Any]]:
        """
        Returns a sequence of sequences of objects associated with the indexes
        in the input matrix.

        If, for any of the indexes, there is not an associated object, that
        index is skipped in the output.

        :param index_matrix: A 2-dimensional array of indexes
        :return: A sequence of sequences of objects, one for each index.
        """

        #Providing an index, pulls the corresponding keys from the dictionary
        column = []
        for index in index_matrix:
            row = []
            for obj in index:
                for key,value in self.dict.items():
                    if obj == value:
                        row.append(key)
            column.append(row)

        objects = column
        return objects

    def binary_vector_to_objects(self, vector: np.ndarray) -> Sequence[Any]:
        """
        Returns a sequence of the objects identified by the nonzero indexes in
        the input vector.

        If, for any of the indexes, there is not an associated object, that
        index is skipped in the output.

        :param vector: A 1-dimensional binary array
        :return: A sequence of objects, one for each nonzero index.
        """

        #Providing an index, pulls the corresponding keys from the dictionary
        vector = vector[self.start:]
        objects = []
        sort = sorted(self.dict, key=self.dict.get)

        for idx,val in enumerate(vector):
            if val == 1:
                objects.append(sort[idx])

        return objects

    def binary_matrix_to_objects(
            self, binary_matrix: np.ndarray) -> Sequence[Sequence[Any]]:
        """
        Returns a sequence of sequences of objects identified by the nonzero
        indices in the input matrix.

        If, for any of the indexes, there is not an associated object, that
        index is skipped in the output.

        :param binary_matrix: A 2-dimensional binary array
        :return: A sequence of sequences of objects, one for each nonzero index.
        """

        #Eliminating unnecessary values
        new_binary = []
        for item in binary_matrix:
            new_binary.append(item[self.start:])

        objects = []
        sort = sorted(self.dict, key=self.dict.get)

        #Providing an index, if the index has a corresponding key, returns 1.
        for j in new_binary:
            rows = []
            for idx,val in enumerate(j):
                if val == 1:
                    rows.append(sort[idx])
            objects.append(rows)

        return objects
