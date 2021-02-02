variable "region" {
  default = "us-west-2"
}

variable "workspace" {
}

# locals {
#     env_name =lower(terraform.workspace)

# common_tags = {
#   Environment = local.env_name
# }

# }

locals {
    env_name =var.workspace

common_tags = {
  Environment = local.env_name
}

}
