import requests

# List of filter list URLs
filter_urls = [
    'https://raw.githubusercontent.com/iam-py-test/my_filters_001/main/antitypo.txt',
    'https://raw.githubusercontent.com/iam-py-test/my_filters_001/main/antimalware.txt'
]

# Function to fetch filter lists
def fetch_filter_lists(urls):
    filters = set()
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            filters.update(response.text.splitlines())
        else:
            print(f"Failed to fetch {url}")
    return filters

# Function to remove duplicates and save to a single file
def save_aggregated_list(filters, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for line in sorted(filters):
            f.write(f"{line}\n")

# Main process
if __name__ == "__main__":
    aggregated_filters = fetch_filter_lists(filter_urls)
    save_aggregated_list(aggregated_filters, 'aggregated_filters.txt')
    print("Aggregated filter list saved to aggregated_filters.txt")
