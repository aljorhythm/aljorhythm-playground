# 5414. People Whose List of Favorite Companies Is Not a Subset of Another List

# Given the array favoriteCompanies where favoriteCompanies[i] is the list of favorites companies for the ith person (indexed from 0).

# Return the indices of people whose list of favorite companies is not a subset of any other list of favorites companies. You must return the indices in increasing order.

def peopleIndexes(favoriteCompanies):
    indices = []
    favoriteCompanies = map(set, favoriteCompanies)
    for i, person in enumerate(favoriteCompanies):
        has_subset = False
        for j, otherPerson in enumerate(favoriteCompanies):
            print("i " + str(i) + " j " + str(j))

            if i == j:
                continue
            
            sorted_person = sorted(person)
            is_subset = True
            for c in sorted_person:
                if c not in otherPerson:
                    is_subset = False
                    break
            if is_subset:
                has_subset = True
                break
        print("not has subset " + str(i), not has_subset)
        if not has_subset:
            indices.append(i)
    return indices


inputs = [
    [["leetcode"],["google"],["facebook"],["amazon"]],
    [["leetcode", "google", "facebook"], ["google", "microsoft"],
        ["google", "facebook"], ["google"], ["amazon"]],
    [["nxaqhyoprhlhvhyojanr", "ovqdyfqmlpxapbjwtssm", "qmsbphxzmnvflrwyvxlc", "udfuxjdxkxwqnqvgjjsp", "yawoixzhsdkaaauramvg", "zycidpyopumzgdpamnty"], [
        "nxaqhyoprhlhvhyojanr", "ovqdyfqmlpxapbjwtssm", "udfuxjdxkxwqnqvgjjsp", "yawoixzhsdkaaauramvg", "zycidpyopumzgdpamnty"], ["ovqdyfqmlpxapbjwtssm", "qmsbphxzmnvflrwyvxlc", "udfuxjdxkxwqnqvgjjsp", "yawoixzhsdkaaauramvg", "zycidpyopumzgdpamnty"]]]
outputs = [[0,1,2,3],[0, 1, 4], [0]]

results = []
for (i, o) in zip(inputs, outputs):
    result = peopleIndexes(i)
    print(result)
    print(result == o)
    results.append((result == o,result))

print("all")
print(results)
