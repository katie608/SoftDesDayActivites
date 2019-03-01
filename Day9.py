known = {}

def nchoosek(n, k):
    """ returns the number of combinations of size k
        that can be made from n items.

        >>> nchoosek(5,3)
        10
        >>> nchoosek(1,1)
        1
        >>> nchoosek(4,2)
        6
    """
    if (n, k) in known:
        return known[(n,k)]
    if k == 0:
        return 1
    if n == k:
        return 1
    if n < k:
        return "n must be greater than k"
    result =  nchoosek(n - 1, k - 1) + nchoosek(n - 1, k)
    known[(n,k)] = result
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=False)

# print(nchoosek(895, 230))
# print(nchoosek(230, 90))
print(nchoosek(895, 90))
