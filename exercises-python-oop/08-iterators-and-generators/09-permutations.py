from itertools import permutations

# # easy mode:
# def possible_permutations(sequence):
#     for perm in permutations(sequence):
#         yield list(perm)


# hard mode:
def possible_permutations(sequence):
    def recurse(sequence, target_idx, perm, used):
        if perm is None:
            perm = [0] * len(sequence)

        if used is None:
            used = [False] * len(sequence)

        if target_idx == len(sequence):
            print(perm)
            return

        for i, x in enumerate(sequence):
            if not used[i]:
                perm[target_idx] = x
                used[i] = True
                recurse(sequence, target_idx + 1, perm, used)
                used[i] = False

    return recurse(sequence, target_idx=0, perm=None, used=None)


print(possible_permutations([1, 2, 3]))
