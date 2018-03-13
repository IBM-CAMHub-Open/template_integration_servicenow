# =================================================================
# Licensed Materials - Property of IBM
# 5737-E67
# @ Copyright IBM Corporation 2016, 2017 All Rights Reserved
# US Government Users Restricted Rights - Use, duplication or disclosure
# restricted by GSA ADP Schedule Contract with IBM Corp.
# =================================================================

##############################################################
# COMMAND VARIABLES
##############################################################

variable "cmdb_user" { type = "string" description = "Service Now User." default = "admin" }
variable "cmdb_pass" { type = "string" description = "Service Now Password"}
variable "cmdb_instance" { type = "string" description = "Service Now Instance Location" }
variable "cmdb_key" { type = "string" description = "CMDB Unique Record Key, maps to the name field" default = "server1"}
variable "cmdb_record" { type = "map" description = "CMDB MAP Record" }