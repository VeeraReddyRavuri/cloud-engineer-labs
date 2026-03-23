output "vpc_id" {
  description = "The ID of vpc"
  value       = aws_vpc.main.id
}

output "public_subnet_id" {
  description = "The ID of Public subnet"
  value       = aws_subnet.public.id
}

output "private_subnet_id" {
  description = "The ID of private subnet"
  value       = aws_subnet.private.id
}