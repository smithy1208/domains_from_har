#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import re


def parse_har(file):
    result = set()
    regex = re.compile(r"https?://([a-zA-Z0-9.]+)/")
    for line in file:
        if m := regex.search(line):
            result.add(m.group(1))
    return sorted(list(result))


def write_addrlist(addr_list, domains):
    with open(f"{addr_list}.rsc", "w") as f:
        for d in domains:
            f.write(f"/ip firewall address-list add address={d} list={addr_list}\n")
    print(f"File {addr_list}.rsc was created successfully.")


def main():
    parser = argparse.ArgumentParser(description="Parcer for har file. Get domains")
    parser.add_argument("harfile", type=argparse.FileType("r"), help="HAR file")
    parser.add_argument(
        "-a",
        dest="addrlist",
        action="store_true",
        help="Make address list as *.rsc",
    )

    args = parser.parse_args()

    domains = parse_har(args.harfile)
    print(domains)

    if args.addrlist:
        addrlistname = f"{args.harfile.name.rstrip('.har')}"
        write_addrlist(addrlistname, domains)


if __name__ == "__main__":
    main()
