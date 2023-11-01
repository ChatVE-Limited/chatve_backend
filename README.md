# File Metadata Upload API (Project Documentation)

This repository contains a Django REST Framework (DRF) application designed to upload files and retrieve metadata using an external service, exifmeta.com.

## Features

- File upload endpoint that forwards the uploaded file to the exifmeta.com API.
- JSON responses with status messages and extracted metadata from the uploaded files.

## Requirements

To run this project, you will need:

- Python 3.6 or higher
- Django
- Django REST Framework

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

Install Requirements
```bash
pip install -r requirements.txt
```

Run Server 

```bash
python manage.py runserver
```

# File Metadata Upload API (API Dcumentation)

### The API is now accessible at http://localhost:8000/upload/.

### Usage
#### To upload a file and retrieve its metadata, use the following endpoint:


POST /upload/

- Description: Upload a file to retrieve its metadata.
```json
Content-Type: multipart/form-data
Form data:
file: The file to upload.
cURL Example
bash
Copy code
curl -X POST -F "file=@/path/to/your/file.jpg" http://localhost:8000/upload/
Response
A successful response returns a JSON object with a message and the metadata:

json
Copy code
{
  "message": "file uploaded successfully",
  "data": {
    // Metadata from exifmeta.com
  }
}
In case of failure, a JSON object with an error message is returned.

```

Contributing

Contributions to this project are welcome. To contribute:

- Fork the repository.
- Create a new branch (git checkout -b feature/AmazingFeature).
- Make your changes.
- Commit your changes (git commit -m 'Add some AmazingFeature').
- Push to the branch (git push origin feature/AmazingFeature).
- Open a pull request.

#### License

This project is licensed under the MIT License - see the LICENSE.md file for details.

Contact:

- GitHub: Tobitheprof





