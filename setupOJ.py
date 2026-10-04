"""This module for set up to start work"""
import os
import shutil

work_path = "work/WORKING"

def setup_workflow():
    """
    setup process
    """
    oj_id, name = input().split(" ", 1)
    is_log = input("Do you want submission.md ? [y/n] : ").casefold() == "y"

    os.makedirs(work_path + f"/oj{oj_id}_work", exist_ok=True)
    with open(work_path + f"/oj{oj_id}_work/main.py", "w") as file:
        file.write(f'"""{name}"""\n')
    if is_log:
        empty_submission = "empty_submission.md"
        to = work_path + f"/oj{oj_id}_work/submission.md"
        shutil.copyfile(empty_submission, to)
    print(f"Complete to add {oj_id} to working dir.")

def lnlog_subbmit(ojid):
    """
    auto leaninglog oj submit submission.md
    """
    complete_submission = work_path + f"/oj{ojid}_work/submission.md"
    if complete_submission:
        os.makedirs(f"oj{ojid}", exist_ok=True)
        print(f"oj{ojid} added.")
        oj_path = f"oj{ojid}/submission.md"
        shutil.copyfile(complete_submission, oj_path)
        
        print("submission.md clone complete.")
