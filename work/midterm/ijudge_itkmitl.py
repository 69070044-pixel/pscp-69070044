"""I judge URL"""
url = input()
if url[-1] == "/":
    url = url[:-1]
if url[:39] == "https://ijudge.it.kmitl.ac.th/problems/":
    p_id = url.replace("https://ijudge.it.kmitl.ac.th/problems/", "")
    if p_id.isdigit() and 0 <= int(p_id) <= 3999 and len(p_id) == 4:
        print(p_id[0], "STAR")
    else:
        print("INVALID")
else:
    print("INVALID")
