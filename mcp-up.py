#!/usr/bin/python

import sys
from getpass import getpass
from os import system, environ
import argparse

# Arguments
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--tag", default="latest", help="DockerHub images tag")
parser.add_argument("-o", "--org", default="aerogearcatalog", help="DockerHub org")
parser.add_argument("-d", "--dns", default="nip.io", help="Wildcard DNS Host")
parser.add_argument("-c", "--clean", action="store_true", help="Do a make clean prior installation")
args = parser.parse_args()

try:
  dockerHubUser = environ["DOCKERHUB_USER"]
except KeyError:
  dockerHubUser = raw_input("DockerHub user: ")

try:
  dockerHubPass = environ["DOCKERHUB_PASS"]
except KeyError:
  dockerHubPass = getpass("DockerHub password: ")

dockerHubTag = args.tag
dockerHubOrg = args.org
wildcardDnsHost = args.dns

# Print info
print("")
print("===== MCP-UP! =====")
print("DockerHub User: " + dockerHubUser)
print("DockerHub Org: " + dockerHubOrg)
print("Default Tag: " + dockerHubTag)
print("Wildcard DNS Host: " + wildcardDnsHost)
print("===================")
print("")

if args.clean:
  system("set -x; make clean")

bashCommand = '''
ansible-playbook ./installer/playbook.yml \\
  -e "dockerhub_username={dockerHubUser}" \\
  -e "dockerhub_password={dockerHubPass}" \\
  -e "dockerhub_tag={dockerHubTag}" \\
  -e "dockerhub_org={dockerHubOrg}" \\
  -e "wildcard_dns_host={wildcardDnsHost}" \\
  --ask-become-pass;

oc login -u system:admin
oc adm policy add-cluster-role-to-user cluster-admin admin
oc adm policy add-cluster-role-to-user access-asb-role admin
oc adm policy add-cluster-role-to-user cluster-admin developer
oc login -u admin -p admin
'''.format(
  dockerHubUser = dockerHubUser,
  dockerHubPass = dockerHubPass, 
  dockerHubTag = dockerHubTag,
  dockerHubOrg = dockerHubOrg,
  wildcardDnsHost = wildcardDnsHost
)

system(bashCommand)