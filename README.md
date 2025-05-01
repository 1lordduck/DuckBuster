# DuckBuster

DuckBuster is a very **simple** brute-forcer to discover hidden directories.

This project was started as a way to learn and practice my knowledge in web development and scanning tools, and for fun of course.

### Instalation

1. Clone the repository:
   ```bash
   git clone https://github.com/1lordduck/DuckBuster.git
   cd DuckBuster
   ```

2. You're done!

## Usage

DuckBuster allows you to brute-force a website by providing a website url (`-u`) and a Wordlist (`-w`) You can also set a threshold value (`-T`) (NOT IMPLEMENTED AS OF TODAY!! 1/may/2025)
### Available options:

- `-u URL`: Provide a URL of the website you want to scan.
- `-T THRESHOLD`: Set a threshold value for scanning (you can customize the threshold logic in your code).
  
### Example 1: 
```bash
python3 duckbuster.py -w /usr/share/dirbuster/wordlists/directory-list-2.3-small.txt -u "https://website.com" 
```

DuckBuster will then print out results and their html code.

## License

DuckBuster is licensed under the MIT License. See `LICENSE` for more details.
