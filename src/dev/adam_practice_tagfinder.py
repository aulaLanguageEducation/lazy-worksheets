import bs4

with open("sample_webpage.html") as html_file:
    html = html_file.read()

soup = bs4.BeautifulSoup(html, "html.parser")

def p_tag_finder(my_soup):

    # Lines 12 - 17 find all the <p> tags in the html file and count them, creating the...
    # ...variable called 'total_number_of_p_tags'.
    p_tags = my_soup.findAll('p')

    total_number_of_p_tags = 0

    for item in p_tags:
        total_number_of_p_tags +=1

    # Lines 21 - 24 find ALL parents of EVERY <p> tag and add them to the list...
    # ...called 'p_tag_parents'.
    p_tag_parents = []

    for tag in p_tags:
        p_tag_parents.append(tag.parents)

    # Lines 30 - 40 iterate through this list of <p> tag parents and count...
    # ...the number of <p> tags for each parent, creating a dictionary called 'p_tag_dict'...
    # ...where the keys are the names of these parent tags and their (integer) values are...
    # ...the number of <p> tags which they each contain.
    sub_tag_p_number = 0

    p_tag_dict = {}

    for parent in p_tag_parents:
        for sub_tag in parent:
            sub_tag_contents = sub_tag.findAll('p')
            for tag in sub_tag_contents:
                sub_tag_p_number +=1
                p_tag_dict.update({sub_tag.name: sub_tag_p_number})
            sub_tag_p_number = 0

    # Lines 44 - 46 sort the 'p_tag_dict' into ascending order as per the values, and then...
    # ...turn this sorted dictionary into a list (of tuples).
    sorted_dict = {key: val for key, val in sorted(p_tag_dict.items(), key=lambda ele: ele[1])}

    dict_as_sorted_list = list(sorted_dict.items())

    # Line 51 removes all items in this list where the value (i.e. the number of <p> tags)...
    # ...is the same as the total number of <p> tags in the whole html file. This should therefore remove...
    # ...the oldest grandparents, which contain ALL <p> tags in the html file.
    dict_as_sorted_list = [(x, y) for (x, y) in dict_as_sorted_list if y != total_number_of_p_tags]

    # Line 57 finds the remaining 'parent tag' in this sorted/edited list...
    # ...which has the highest number of <p> tags. When there are two tags which have the same value...
    # ...this function (conveniently) seems to give the 'furthest to the left' which happens to be...
    # ...the youngest grandparent and the tag which we want.
    highest_tag = sorted(dict_as_sorted_list, key=lambda i: i[1], reverse=True)[0][0]

    print('Here is the total number of p tags: ', total_number_of_p_tags)
    print('\n')
    print('Here is the sorted dictionary: ', str(dict_as_sorted_list))
    print('\n')
    print('The key with the highest value is: ', highest_tag)

p_tag_finder(soup)

