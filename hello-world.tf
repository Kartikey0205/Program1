terraform {
  required_providers {
    null = {
      source = "hashicorp/null"
      version = "3.1.0"
    }
  }
}

provider "null" {}

resource "null_resource" "hello_world" {
  provisioner "local-exec" {
    command = "echo hello world!"
  }
}
