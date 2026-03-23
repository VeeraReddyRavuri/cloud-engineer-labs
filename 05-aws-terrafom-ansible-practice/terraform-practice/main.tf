terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  backend "s3" {
    bucket = "YOUR_BUCKET_NAME"
    key = "dev/terraform.tfstate"
    region = "us-east-1"
    dynamodb_table = "YOUR_TABLE"
    encrypt = true
  }
}
provider "aws" {
  region = "us-east-1"
}

module "vpc" {
  source       = "./modules/vpc"    # path to module folder
  vpc_cidr     = var.vpc_cidr       # passing values in
  project_name = var.project_name
}
