
if __name__ == '__main__':
    text = """Standard
Move
Full-round
Swift
Immediate
Free
"""

    done = text.splitlines()
    # w = []
    for d in done:
        print("\"" + d.lower() + " action\", ", end='')
        # x = d.split()[0]
        # if "Domain" not in d:
        #     if d.lower() not in w:
        #         w.append(d.lower())
    # for x in w:
    #     print("\"" + x + "\", ", end='')
        # print("\"" + x.lower() + "\", ", end='')
