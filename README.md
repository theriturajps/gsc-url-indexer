<div align="center">

# 🚀 Google Search Console Indexer with Python 🚀
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![API](https://img.shields.io/badge/Google%20API-Indexing%20API-yellow.svg)](https://developers.google.com/search/apis/indexing-api/v3/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/theriturajps/gsc-url-indexer/blob/main/LICENSE)
![GitHub Repo stars](https://img.shields.io/github/stars/theriturajps/gsc-url-indexer?style=social)
![GitHub forks](https://img.shields.io/github/forks/theriturajps/gsc-url-indexer?style=social)
![GitHub contributors](https://img.shields.io/github/contributors/theriturajps/gsc-url-indexer)
</div>
<p align="center">
  <img src="https://raw.githubusercontent.com/theriturajps/gsc-url-indexer/main/gsc-url-indexer.png" width="700" alt="Google Search Console Indexer with Python">
</p>

This Python project uses the **Google Search Console API** to automatically index or reindex URLs listed in a sitemap. The script is designed with error handling, retry mechanisms, and a beautiful terminal UI for professional indexing.

## 📋 Features

- **Automated URL Indexing/Reindexing**: Automatically submits URLs for indexing based on your sitemap.
- **Rich Terminal UI**: Displays status and progress of indexing in a professional, colorful, and easy-to-read format.
- **Error Handling**: Gracefully handles indexing failures and retries with appropriate logging.
- **Google API Authentication**: Uses service account credentials for secure API access.

## 🛠️ Prerequisites

Before running the script, ensure you have the following:

- **Python 3.7+** installed
- A Google Cloud project with **Google Search Console Indexing API** enabled
- **Service account credentials** in a `key.json` file
- **Sitemap URL** containing the URLs to be indexed

## 🚀 Getting Started

### 1. Clone the Repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/theriturajps/gsc-url-indexer.git
cd gsc-url-indexer
```

### 2. Set Up Google Search Console API

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Enable the **Indexing API** for your project.
3. Create a **Service Account** and download the JSON key file (`key.json`).
4. Add the service account email to your **Google Search Console property** with **full permissions**.

### 3. Install Dependencies

To run this project, you'll need to install the required Python libraries. You can do this by running:

```bash
pip install -r requirements.txt
```

Alternatively, install them manually:

```bash
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client requests xmltodict rich
```

### 4. Set Up Your Project

Ensure the following project structure:

```
gsc-url-indexer/
│
├── key.json               # Your Google Cloud credentials file
├── indexer.py             # Main script file
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
└── LICENSE                # License for the project
```

### 5. Running the Script

Run the `indexer.py` script with:

```bash
python indexer.py
```

The script will:

- Authenticate with the Google Search Console API.
- Fetch all URLs from your sitemap.
- Index or reindex each URL.
- Display progress, status, and a summary in the terminal.

## 🛠️ Configuration

### Authentication

The script requires a valid **service account** credential file (`key.json`). Ensure your service account is added as a **user** with permissions in your Google Search Console property.

### Sitemap URL

By default, the script is set to use `https://www.riturajps.in/sitemap.xml`. You can replace this URL in the script if you're using a different sitemap.

```python
# Sitemap URL to fetch the URLs
sitemap_url = 'https://www.riturajps.in/sitemap.xml'
```

## 🧾 Example Output

The script provides professional output in the terminal, like the example below:

```bash
🚀 Google Search Console Indexer 🚀
Authenticated successfully with Google Search Console.
Fetched 10 URLs from the sitemap.

Indexing URLs...
----------------------------------------------------------------
| URL                       | Status  | Details                |
----------------------------------------------------------------
| https://example.com/page1 | Success | Indexed successfully   |
| https://example.com/page2 | Success | Indexed successfully   |
| https://example.com/page3 | Failed  | Error occurred         |
----------------------------------------------------------------

📊 Indexing Summary 📊
----------------------------------------------------------------
Total URLs Processed: 10
Successful: 8
Failed: 2
```

## 🔧 Troubleshooting

- **Authentication Errors**: Ensure your `key.json` is valid and your service account has proper permissions.
- **Failed URL Indexing**: Check if the URLs are properly formatted and accessible via Google Search Console.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Feel free to submit a PR or open an issue if you find a bug or have a suggestion for improvement.

## 🙋‍♂️ Support

If you have any issues or questions, feel free to reach out by opening an issue on the GitHub repository.
- **GitHub Sponsor (Global)**: [Click Here](https://github.com/sponsors/theriturajps)
- **UPI (India)**: [Support Using UPI](https://riturajps.vercel.app/)

## 🏅 Acknowledgements

- Thanks to [Google](https://developers.google.com/search/apis/indexing-api/v3/) for providing the **Indexing API**.
