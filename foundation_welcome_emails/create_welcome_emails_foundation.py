#!/usr/bin/env python3
#
# Script to create everything for an umbrella project
#
# Loads config file ( set with -c command line arg ) for project details
#
# Copyright this project and it's contributors
# SPDX-License-Identifier: Apache-2.0
#
# encoding=utf8

from argparse import ArgumentParser
from liquid import Liquid
import yaml
import sys

# statics for template file paths
class FoundationWelcomeTemplate:
    announce    = 'email_templates/welcome-announce.md'
    board       = 'email_templates/welcome-board.md'
    outreach    = 'email_templates/welcome-outreach.md'
    members     = 'email_templates/welcome-members.md'
    tac         = 'email_templates/welcome-tac.md'
    private     = 'email_templates/welcome-private.md'
    staff       = 'email_templates/welcome-staff.md'

    def renderTemplate( type, foundation ):
        template_file = open(eval('FoundationWelcomeTemplate.'+type), 'r')
        ret = Liquid(template_file.read()).render(**foundation)
        output_file = open("welcome-"+foundation['foundation']['mailing_lists'][type]+".txt","w")
        output_file.write(ret)
        output_file.close()
        print("Created "+output_file.name)


parser = ArgumentParser()
parser.add_argument("-c", "--config", dest="configfile", default="foundation.yaml", help="name of YAML config file (defaults to foundation.yaml)")
args = parser.parse_args()

try:
    with open(args.configfile, 'r') as stream:
        foundation = yaml.safe_load(stream)
except:
    sys.exit(args.configfile+" config file is not found")

# determine the welcome emails to render
for emaillist in foundation['foundation']['mailing_lists']:
    if not foundation['foundation']['mailing_lists'][emaillist] == 'None':
        FoundationWelcomeTemplate.renderTemplate(emaillist, foundation)
