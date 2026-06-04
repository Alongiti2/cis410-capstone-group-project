variable "project_id" {
  description = "GCP Project ID"
  type        = string
}

variable "region" {
  description = "GCP Region"
  type        = string
  default     = "us-west1"
}

variable "db_password" {
  description = "Cloud SQL database password"
  type        = string
  sensitive   = true
}
