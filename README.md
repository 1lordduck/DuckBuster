# DuckBuster

DuckBuster is a **simple** brute-forcer designed to discover hidden directories on websites.

This project was created as a learning exercise to enhance my knowledge of web development and scanning tools—and, of course, for fun.

---

<div align="center">
  <img src="https://github.com/user-attachments/assets/4c3234a7-01f4-419d-9778-e16576adff1c" alt="DuckBuster" />
</div>

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/1lordduck/DuckBuster.git
   cd DuckBuster
   ```

2. Done! You're ready to go.

## Usage

DuckBuster brute-forces hidden directories by taking a website URL (`-u`) and a wordlist (`-w`).  
You can also provide a threshold value (`-T`)—**note: this feature is not implemented yet as of May 1, 2025**.

### Available Options

- `-u URL` — The target website URL to brute-force.
- `-w WORDLIST` — Path to the wordlist used for brute-forcing.
- `-T THRESHOLD` — Optional: Set a threshold value (currently not implemented).

### Example

```bash
python3 duckbuster.py -w /usr/share/dirbuster/wordlists/directory-list-2.3-small.txt -u "https://website.com"
```

DuckBuster will then print out the results and the corresponding HTML code.

## License

DuckBuster is licensed under the MIT License. See `LICENSE` for more details.
