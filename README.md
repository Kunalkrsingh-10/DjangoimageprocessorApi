# ImageProcessorAPI

**ImageProcessorAPI** is a Django-based web application for processing images. It utilizes Django REST Framework for creating RESTful APIs and Celery for handling background tasks like image processing. This project serves as a robust backend for managing image-related tasks asynchronously.

## Features

- **Image Upload and Processing**: Upload images and process them asynchronously.
- **Django REST Framework**: RESTful APIs for managing image uploads and retrieving processed images.
- **Celery Integration**: Asynchronous task management for image processing.
- **Redis**: Used as a message broker for Celery.
- **PostgreSQL**: Database backend for storing image metadata.

## Installation

### Prerequisites

- Python 3.x
- Django 4.x
- Celery 5.x
- Redis
- PostgreSQL

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Kunalkrsingh-10/ImageProcessorAPI.git
   cd ImageProcessorAPI
