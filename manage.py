#!/usr/bin/env python
import os
import sys

# hello how you doing
# i am great bhai 
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
