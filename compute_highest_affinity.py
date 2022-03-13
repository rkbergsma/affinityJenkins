# No need to process files and manipulate strings - we will
# pass in lists (of equal length) that correspond to
# sites views. The first list is the site visited, the second is
# the user who visited the site.

# See the test cases for more details.

def highest_affinity(site_list, user_list, time_list):
    # Returned string pair should be ordered by dictionary order
    # I.e., if the highest affinity pair is "foo" and "bar"
    # return ("bar", "foo").

    user_history = {}

    for site, user in zip(site_list, user_list):
        if user not in user_history:
            user_history[user] = set()

        user_history[user].add(site)

    affinities = {}
    for user, history in user_history.items():
        history = list(history)
        history.sort()
        for i, site1 in enumerate(history):
            for site2 in history[i+1:]:
                pair = (site1, site2)
                if pair not in affinities:
                    affinities[pair] = 0
                affinities[pair] += 1

    return max(affinities, key=affinities.get)

def reverse_user_names(user_list):
    new_user_list = []
    for user in user_list:
        new_user = user[::-1]
        new_user.upper()
        new_user_list.append(new_user)
    return new_user_list

def split_site_domain(site_list):
    site_domain_list = []
    for site in site_list:
        (new_site_domain) = site.split(',')
        site_domain_list.append(new_site_domain)

def do_nothing():
    num_list = []
    for i in range(0,10):
        num_list.append(i)
    return sum(num_list)

def fibonacci(number):
    if number == 0 or number == 1:
        return number
    result = fibonacci(number - 1) + fibonacci(number - 2)
    return result

def sum_list_long_way(input):
    sum = 0
    for item in list:
        if isinstance(item, int):
            sum = sum + item
    return sum
