def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx

global num_list, uniq_num_list, sort_num_list
num_list = [4, 8, 1, 3, 2, 5, 9, 1, 3, 2]
uniq_num_list = []
sort_num_list = []

class TestDataEmptyArray(object):
    
    @staticmethod
    def get_array():
        # complete this function
        return []

class TestDataUniqueValues(object):

    @staticmethod
    def get_array():
        # complete this function
        
        for i in num_list:
            available = 0
            if len(uniq_num_list) == 0:
                uniq_num_list.append(i)
            for j in uniq_num_list:
                if i == j:
                    available = 1
            if available == 0:
                uniq_num_list.append(i)

        return uniq_num_list
                
    @staticmethod
    def get_expected_result():
        # complete this function
        temp = uniq_num_list[0]
        min_value_index = 0
        for i in range(len(uniq_num_list)):
            if uniq_num_list[i] < temp:
                temp = uniq_num_list[i]
                min_value_index = i
                       
        return min_value_index
    
class TestDataExactlyTwoDifferentMinimums(object):

    @staticmethod
    def get_array():
        # complete this function
        sort_num_list = sorted(num_list)
        if sort_num_list[0] == sort_num_list[1] and ((len(sort_num_list) == 2 or sort_num_list[1] < sort_num_list[2])):
            return sort_num_list

    @staticmethod
    def get_expected_result():
        # complete this function
        return 0

def TestWithEmptyArray():
    try:
        seq = TestDataEmptyArray.get_array()
        result = minimum_index(seq)
    except ValueError as e:
        pass
    else:
        assert False


def TestWithUniqueValues():
    seq = TestDataUniqueValues.get_array()
    assert len(seq) >= 2

    assert len(list(set(seq))) == len(seq)

    expected_result = TestDataUniqueValues.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result


def TestiWithExactyTwoDifferentMinimums():
    seq = TestDataExactlyTwoDifferentMinimums.get_array()
    assert len(seq) >= 2
    tmp = sorted(seq)
    assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])

    expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result

TestWithEmptyArray()
TestWithUniqueValues()
TestiWithExactyTwoDifferentMinimums()
print("OK")