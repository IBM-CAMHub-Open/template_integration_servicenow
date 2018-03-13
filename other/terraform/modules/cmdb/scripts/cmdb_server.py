#!/usr/bin/python
## =COPYRIGHT=======================================================
# Licensed Materials - Property of IBM
#
# (c) Copyright IBM Corp. 2017, 2018 All Rights Reserved
#
# US Government Users Restricted Rights - Use, duplication or
# disclosure restricted by GSA ADP Schedule Contract with IBM Corp.
# ===============================================================

import argparse
import json

from servicenow import ServiceNow
from servicenow import Connection
from requests.exceptions import ConnectionError

def get_connection(location, instance, user, password):

    """

    Return a connection object for Service Now.

    """

    conn =  Connection.Auth(username=user, password=password, instance=instance, api='JSONv2')
    return conn

def create_cmdb(cmdb_server, cmdb_key, cmdb_record):

    """
    Create a CMDB Record, update if already exists. We assume that the name attribute should be unique
    and that a subsequent create will invoke an update.
    """

    cmdb_records = cmdb_server.list({'name': cmdb_key})
    if len(cmdb_records['records']) == 0:
        print "create_cmdb: Record with name:" + cmdb_key + " does not exist, creating."
        cmdb_response = cmdb_server.create(cmdb_record)
    else:
        print "create_cmdb: Record with name:" + cmdb_key + " already exists, updating."
        cmdb_response = cmdb_server.update({'name': cmdb_key}, cmdb_record)
    return cmdb_response

def delete_cmdb(cmdb_server, cmdb_key):

    """
    Delete a CMDB Record. Assume name is unique, deletion happens using sys_id.
    """

    cmdb_records = cmdb_server.list({'name': cmdb_key})
    if len(cmdb_records['records']) == 0:
        print "delete_cmdb: Record with name:" + cmdb_key + " does not exist, can not delete."
        return None
    elif len(cmdb_records['records']) == 1:
        print "delete_cmdb: Record with name:" + cmdb_key + " found, deleting."
        cmdb_response = cmdb_server.delete(cmdb_records['records'][0])
    else:
        print "delete_cmdb: Multiple records with name:" + cmdb_key + " found, not deleting."
        return None
    return cmdb_response


def main():

    # Process Command Line Parameters
    parser = argparse.ArgumentParser(
             description='Create a CMDB Server Record in ServiceNow. ',
             epilog='')
    parser.add_argument("-l", "--sn_location", dest="sn_location", default='ALL', required=False)
    parser.add_argument("-u", "--sn_user", dest="sn_user", required=True)
    parser.add_argument("-p", "--sn_pass", dest="sn_pass", required=True)
    parser.add_argument("-i", "--sn_instance", dest="sn_instance", required=True)
    parser.add_argument("-k", "--cmdb_key", dest="cmdb_key", required=True)
    # cmdb record is variable and passed on the command line as a json string
    parser.add_argument("-r", "--cmdb_record", dest="cmdb_record", type=json.loads, required=False)
    # -c to add -d to delete
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-c', '--create', default=False, action='store_true')
    group.add_argument('-d', '--delete', default=False, action='store_true')

    args = parser.parse_args()

    sn_instance = args.sn_instance
    sn_user = args.sn_user
    sn_pass = args.sn_pass
    sn_location = args.sn_location

    # Get connection object
    cmdb_conn = get_connection(sn_location, sn_instance, sn_user, sn_pass)

    #Get Server Object
    cmdb_server = ServiceNow.Server(cmdb_conn)

    # Process Request
    if args.create:

        cmdb_record = args.cmdb_record
        cmdb_key = args.cmdb_key

        print 'Create CMDB Server Record....'
        print 'SN Instance: ' + args.sn_instance
        print 'SN User: ' + args.sn_user
        print 'SN Pass: ' + '*****'
        print 'CMDB Record Key: ' + cmdb_key
        print 'CMDB Record'

        cmdb_record = args.cmdb_record
        for key in cmdb_record:
            print '    ' + key + ': ' + cmdb_record[key]

        response = create_cmdb(cmdb_server, cmdb_key, cmdb_record)

    elif args.delete:

        cmdb_key = args.cmdb_key

        print 'Delete CMDB Server Record....'
        print 'SN Instance: ' + args.sn_instance
        print 'SN User: ' + args.sn_user
        print 'SN Pass: ' + '*****'
        print 'CMDB Record Key: ' + cmdb_key

        response = delete_cmdb(cmdb_server, cmdb_key)

    if response:
        exit(0)
    else:
        exit(1)

if __name__ == "__main__":
    main()
