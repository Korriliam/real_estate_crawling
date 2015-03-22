__author__ = 'korrigan'

import os
import sys
#redirect the Django conf to our scrappy settings file.
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "location.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)