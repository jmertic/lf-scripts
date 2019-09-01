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
class UmbrellaWelcomeTemplate:
    dev        = 'email_templates/welcome-devlist.md'
    user       = 'email_templates/welcome-userlist.md'
    discussion = 'email_templates/welcome-discussionlist.md'
    private    = 'email_templates/welcome-privatelist.md'

    def renderTemplate( type, project ):
        template_file = open(eval('UmbrellaWelcomeTemplate.'+type), 'r')
        ret = Liquid(template_file.read()).render(**project)
        output_file = open("welcome-"+project['project']['mailing_lists'][type]+".txt","w")
        output_file.write(ret)
        output_file.close()
        print("Created "+output_file.name)


parser = ArgumentParser()
parser.add_argument("-c", "--config", dest="configfile", default="project.yaml", help="name of YAML config file (defaults to project.yaml)")
args = parser.parse_args()

try:
    with open(args.configfile, 'r') as stream:
        project = yaml.safe_load(stream)
except:
    sys.exit(args.configfile+" config file is not found")

# determine the welcome emails to render
for emaillist in project['project']['mailing_lists']:
    if not project['project']['mailing_lists'][emaillist] == 'nil':
        UmbrellaWelcomeTemplate.renderTemplate(emaillist, project)
