terraform {
  required_version = ">= 1.0.0"

  required_providers {
    camc = {
      source  = "registry.ibm.com/cam/camc"
      version = "0.2.5"
    }
  }
}
