def start_spring(**spring_objects):
    final_dict = {}

    for object, type in spring_objects.items():
        if type not in final_dict:
            final_dict[type] = []
        final_dict[type].append(object)

    sorted_dict = sorted(final_dict.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    final_str = ""
    for tp, lst_objects in sorted_dict:
        sorted_lst_obs = sorted(lst_objects)
        final_str += f"{tp}:\n"
        for obj in sorted_lst_obs:
            final_str += f"-{obj}\n"
    return final_str




example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))

example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))

