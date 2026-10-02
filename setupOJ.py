"""This module for set up to start work"""
import os
import shutil

def setup_workflow():
    """
    setup process
    """
    oj_id, name = input().split()
    is_log = input("Do you want submission.md ? [y/n] : ").casefold() == "y"

    work_path = "work/WORKING"

    os.makedirs(work_path + f"/oj{oj_id}_work", exist_ok=True)
    with open(work_path + f"/oj{oj_id}_work/main.py", "w") as file:
        file.write(f'"""{name}"""')
    if is_log:
        empty_submission = "empty_submission.md"
        to = work_path + f"/oj{oj_id}_work/submission.md"
        shutil.copyfile(empty_submission, to)
    print(f"Complete to add {oj_id} to working dir.")
