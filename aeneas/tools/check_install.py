#!/usr/bin/env python

"""
Check Aeneas is properly installed using the Diagnostics.check_all method.

"""

from __future__ import absolute_import
from __future__ import print_function
import sys

from aeneas.tools.abstract_cli_program import AbstractCLIProgram
from aeneas.diagnostics import Diagnostics
import aeneas.globalfunctions as gf


class CheckInstallCLI(AbstractCLIProgram):
    NAME = gf.file_name_without_extension(__file__)
    HELP = {
        "description": "Check Aeneas is properly installed using the Diagnostics.check_all method.",
    }

    def perform_command(self):
        try:
            self.print_info("Checking diagnostics")
            diagnostics = Diagnostics
            results = diagnostics.check_all()
            if results:
                for result in results:
                    self.print_info("%s" % result)
                return self.NO_ERROR_EXIT_CODE
            else:
                self.print_error("No results")
                return self.ERROR_EXIT_CODE
        except Exception as e:
            self.print_error("Issues with the installation")
            self.print_error("%s" % str(e))
        return self.ERROR_EXIT_CODE


def main():
    CheckInstallCLI().run(arguments=sys.argv)


if __name__ == "__main__":
    main()
