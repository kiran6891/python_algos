import itertools
import timeit


def find_numbers(n):

    """
    :return: a,b,c,d which satisfies the condition
    a^3 + b^3 = c^3 + d^3
    """

    # Algo 1 - Brute force

    start_time = timeit.default_timer()
    final_count_1 = 0
    for a in range(1,n):
        for b in range(1,n):
            for c in range(1,n):
                for d in range(1,n):
                    if pow(a,3)+pow(b,3) == pow(c,3)+pow(d,3):
                        final_count_1 += 1
                        print("{0} {1}".format((a,b), (c,d)))
                        break

    elapsed_time_1 = timeit.default_timer() - start_time

    print("----------------------------------------------------------")

    # Algo 2 - Optimised

    start_time_2 = timeit.default_timer()
    final_count_2 = 0
    final_dict = {}
    for c in range(1, n):
        for d in range(1, n):
            result = pow(c,3) + pow(d,3)
            if result in final_dict:
                result_list = final_dict[result]
                result_list.append((c,d))
                final_dict[result] = result_list
            else:
                final_dict[result] = [(c,d)]
    for key,value in final_dict.items():
        for tup in itertools.product(value, value):
            print("{0}".format(tup))
            final_count_2 += 1

    print("Final Count 1 : {0}".format(final_count_1))
    print("Final Count 2 : {0}".format(final_count_2))
    elapsed_time_2 = timeit.default_timer() - start_time_2
    print("Elapsed Time 1: {0}".format(elapsed_time_1))
    print("Elapsed Time 2: {0}".format(elapsed_time_2))


if __name__ == "__main__":
    find_numbers(50)