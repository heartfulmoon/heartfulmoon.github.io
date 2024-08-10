#!/usr/bin/env python
# -*- mode: python -*- -*- coding: utf-8 -*-
import argparse
import datetime
import os

ROOT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
CONTENT_DIR = "content"
TIME_FORMAT = "%H:%M:%S+09:00"
DATETIME_FORMAT = f"%Y-%m-%dT{TIME_FORMAT}"


def check_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--slug", help="post slug")
    parser.add_argument("-d", "--date", help="post date")
    parser.add_argument(
        "-t", "--type", help="content type(default post)", default="post"
    )

    return parser.parse_args()


def main():
    args = check_args()
    if not args.slug:
        print("post slug is required")
        return
    now = datetime.datetime.now()
    if args.date:
        year = args.date[:4]
        month = args.date[4:6]
        day = args.date[6:]
        pub_date = f"{year}-{month}-{day}T{now.strftime(TIME_FORMAT)}"
        # pub_date  = f"{year}-{month}-{day}T{now.strftime('%H:%M:%S+09:00')}"
    else:
        year = now.strftime("%Y")
        month = now.strftime("%m")
        # pub_date = now.strftime('%Y-%m-%dT%H:%M:%S+09:00')
        pub_date = now.strftime(DATETIME_FORMAT)

    content_dir = os.path.join(ROOT_DIR, CONTENT_DIR, args.type, year, month)
    filepath = os.path.join(content_dir, f"{args.slug}.md")
    if os.path.exists(filepath):
        print(f"{filepath} is exists")
        return
    os.makedirs(content_dir, exist_ok=True)

    output = f"""\
---
title: "{args.slug}"
slug: "{args.slug}"
date: "{pub_date}"
categories:
  - 映画
#tags:
#  - 
#link_url: 
#thumbnailImage: 
thumbnailImagePosition: left
#draft: true
---

<!--more-->

{{{{< amazon-prime >}}}}
"""
    with open(filepath, "w") as f:
        f.write(output)

    print(f"create {filepath}")


if __name__ == "__main__":
    main()
##### genpost.py ends here
