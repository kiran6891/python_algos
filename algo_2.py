import timeit

def find_pairs(input_list, k):
    """
    :param input_list:
    prints all pairs within the input_list whose difference is k
    """

    # convert the list of dict
    start_time = timeit.default_timer()
    input_dict = {item: None for item in input_list}
    dict_conversion_time = timeit.default_timer() - start_time
    print("Dict Conversion Time: {0}".format(dict_conversion_time))

    for key in input_dict.keys():
        if (key + k) in input_dict.keys():
            print(key,key+k)
        if (key - k) in input_dict.keys():
            print(key, key-k)
    elapsed_time = timeit.default_timer() - start_time
    print("Total Elapsed Time: {0}".format(elapsed_time))


if __name__ == "__main__":
    find_pairs(input_list=[1, 7, 5, 3, 6, 100, 97, 98, 54, 345, 55, 53, 46], k=2)
