output "vpc_id" {
  description = "The ID of vpc"
  value       = module.vpc.vpc_id
}

output "public_subnet_id" {
  description = "The ID of Public subnet"
  value       = module.vpc.public_subnet_id
}

output "private_id" {
  description = "The ID of private subnet"
  value       = module.vpc.private_subnet_id
}