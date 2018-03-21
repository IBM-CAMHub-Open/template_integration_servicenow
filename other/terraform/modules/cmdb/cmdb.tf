# =================================================================
# Licensed Materials - Property of IBM
# 5737-E67
# @ Copyright IBM Corporation 2016, 2017 All Rights Reserved
# US Government Users Restricted Rights - Use, duplication or disclosure
# restricted by GSA ADP Schedule Contract with IBM Corp.
# =================================================================

##############################################################
# Script package to Configure CMDB
##############################################################

resource "camc_scriptpackage" "cmdb_create" {
  program = ["/usr/bin/python", "${path.module}/scripts/cmdb_server.py", "-c", "-u", "${var.cmdb_user}", "-p", "${var.cmdb_pass}", "-i", "${var.cmdb_instance}", "-k", "${var.cmdb_key}", "-r", "${jsonencode(var.cmdb_record)}"]
  on_create = true
}

resource "camc_scriptpackage" "cmdb_delete" {
  depends_on = ["camc_scriptpackage.cmdb_create"] 
  program = ["/usr/bin/python", "${path.module}/scripts/cmdb_server.py", "-d", "-u", "${var.cmdb_user}", "-p", "${var.cmdb_pass}", "-i", "${var.cmdb_instance}", "-k", "${var.cmdb_key}"]
  on_delete = true
}
