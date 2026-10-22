# Encrypted Diary

A simple Python application for writing and storing diary entries securely.

The idea is pretty straightforward: write your diary, encrypt it with a master password, and decrypt it whenever you want to read it again. Your entries stay encrypted when they're stored, so people can't simply open the files and read your secrets.

## Features

- Write and save diary entries.
- Encrypt entries before storing them.
- Keep encrypted entries in a dedicated folder.
- Decrypt and read entries using your master password.

## Built With

- Python
- Cryptography

## Getting Started

### Installation

Clone the repository:

```bash
git clone <repository-url>
cd encrypted-diary
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

### Running the App

```bash
python main.py
```

More detailed usage instructions will be added as the project develops.

## How It Works

Diary entries are saved as text files, encrypted, and stored in a separate folder. When you want to read an entry, you can decrypt it using your master password.

The goal is to keep things simple without compromising the basic security of your private entries.

## Roadmap

- [ ] Create diary entries.
- [ ] Encrypt and save entries.
- [ ] Decrypt and read entries.
- [ ] Handle incorrect passwords and errors.
- [ ] Improve security and usability.

## Project Status

Currently in development. This is a personal project to practice Python, file handling, and encryption.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
