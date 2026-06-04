terraform {
  required_version = ">= 1.3"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
  backend "gcs" {
    bucket = "cis410-delphin-tfstate"
    prefix = "capstone/infrastructure"
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

# VPC Network
resource "google_compute_network" "vpc" {
  name                    = "acsa-vpc"
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "subnet" {
  name          = "acsa-subnet"
  ip_cidr_range = "10.0.0.0/24"
  region        = var.region
  network       = google_compute_network.vpc.id
}

# Cloud SQL (PostgreSQL)
resource "google_sql_database_instance" "main" {
  name             = "acsa-db"
  database_version = "POSTGRES_15"
  region           = var.region

  settings {
    tier = "db-f1-micro"
    ip_configuration {
      ipv4_enabled = false
    }
  }
  deletion_protection = false
}

resource "google_sql_database" "database" {
  name     = "acsa_security"
  instance = google_sql_database_instance.main.name
}

# Secret Manager
resource "google_secret_manager_secret" "db_password" {
  secret_id = "acsa-db-password"
  replication {
    auto {}
  }
}

# Artifact Registry
resource "google_artifact_registry_repository" "app" {
  location      = var.region
  repository_id = "acsa-app"
  format        = "DOCKER"
}
