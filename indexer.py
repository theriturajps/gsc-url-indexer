import os
import json
import requests
import xmltodict
import time
from google.oauth2 import service_account
from googleapiclient.discovery import build
from rich.console import Console
from rich.table import Table
from rich.progress import track
from rich.panel import Panel
from rich.text import Text

# Terminal console with rich formatting
console = Console()

# Path to your Google API credentials
SERVICE_ACCOUNT_FILE = 'key.json'

# Define the scope for accessing the Search Console API
SCOPES = ['https://www.googleapis.com/auth/indexing']

# Sitemap URL to fetch the URLs
sitemap_url = 'https://www.exonoob.in/sitemap.xml'  # Change the url with your own Sitemap URL.

def authenticate_with_google():
    """Authenticate using service account credentials."""
    try:
        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        service = build('indexing', 'v3', credentials=credentials)
        console.print("[green]Authenticated successfully with Google Search Console.[/green]")
        return service
    except Exception as e:
        console.print(f"[bold red]Error during authentication: {e}[/bold red]")
        raise

def fetch_sitemap_urls(sitemap_url):
    """Fetch and parse URLs from the sitemap."""
    try:
        response = requests.get(sitemap_url)
        sitemap_data = xmltodict.parse(response.content)
        urls = [url['loc'] for url in sitemap_data['urlset']['url']]
        console.print(f"[cyan]Fetched {len(urls)} URLs from the sitemap.[/cyan]")
        return urls
    except Exception as e:
        console.print(f"[bold red]Error fetching sitemap: {e}[/bold red]")
        raise

def index_url(service, url):
    """Index or reindex the given URL using the Indexing API."""
    body = {
        "url": url,
        "type": "URL_UPDATED"  # URL_UPDATED for reindexing, URL_DELETED for removal
    }
    try:
        response = service.urlNotifications().publish(body=body).execute()
        return response
    except Exception as e:
        console.print(f"[yellow]Warning: Failed to index {url}: {e}[/yellow]")
        return None

def main():
    # Create the main panel with title and GitHub link centered
    panel_content = ("🚀 [bold magenta]Google Search Console Indexer[/bold magenta] 🚀")
    console.print(Panel(panel_content, expand=False))

    # Authenticate and get service object
    service = authenticate_with_google()
    
    # Fetch URLs from sitemap
    urls = fetch_sitemap_urls(sitemap_url)
    
    # Prepare table for results display
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("URL", justify="left", style="cyan", no_wrap=True)
    table.add_column("Status", justify="center", style="green")
    table.add_column("Details", justify="left", style="magenta")

    successful, failed = 0, 0

    # Index each URL with progress tracking
    for url in track(urls, description="Indexing URLs..."):
        response = index_url(service, url)
        if response:
            table.add_row(url, "[green]Success[/green]", "Indexed successfully")
            successful += 1
        else:
            table.add_row(url, "[red]Failed[/red]", "Error occurred during indexing")
            failed += 1
            time.sleep(2)  # Retry after a short delay if needed (e.g., API limits)

    console.print(table)

    # Summary
    summary_text = Text()
    summary_text.append(f"Total URLs Processed: {len(urls)}\n", style="bold yellow")
    summary_text.append(f"Successful: {successful}\n", style="green")
    summary_text.append(f"Failed: {failed}\n", style="red")

    console.print(Panel(summary_text, title="📊 [bold cyan]Indexing Summary[/bold cyan]", expand=False))

if __name__ == "__main__":
    main()
