# Integration - ServiceNow CMDB
Copyright IBM Corp. 2018, 2018

## Description

Integration to manage the creation and deletion of CMDB records as a part of deploying a Virtual Machine. This template will execute a python script on the local Terraform container.

## Integration Method

Script local.

## Orchestration Reccomendation

This script should be executed after the successful execution of a Terraform Template to register the Server Assets in CMDB.

## Methods Implemented

- **on_create** Create the CMDB Record or update the CMDB record if an existing record already exists.
- **on_delete** Delete the CMDB Record.

## Prerequisites

- A working version of Service Now addressable from the Terraform Engine.
- The Terraform container requires the **servicenow** module installed.
- The Terraform container requires that **python 2.7** is installed.

<table>
  <tr>
    <th>Variable</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>cmdb_pass</td>
    <td>User to connect to Service Now</td>
  </tr>
  <tr>
    <td>cmdb_user</td>
    <td>Administrative user password.</td>
  </tr>
  <tr>
    <td>cmdb_instance</td>
    <td>Target Service Now instance.</td>
  </tr>
  <tr>
    <td>cmdb_key</td>
    <td>Key value for the Server, this may be the host name. THis field will realte to the cmdb_ci_server name field.</td>
  </tr>
  <tr>
    <td>cmdb_key</td>
    <td>Key value for the Server, this may be the host name. THis field will realte to the cmdb_ci_server name field.</td>
  </tr>
  <tr>
    <td>cmdb_record</td>
    <td>A MAp of values that constitute the CMDB Record. The structure is user defined and should follow the fields describe in the ServiceNow ci_cmdb_server record. The only mandatory value is the name field.</td>
  </tr>
</table>
