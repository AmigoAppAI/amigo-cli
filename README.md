[![Twitter Follow](https://img.shields.io/twitter/follow/AmigoAI?style=social)](https://twitter.com/AmigoAI_)
[![License](https://img.shields.io/pypi/l/amigo.svg)](https://github.com/AmigoAppAI/amigo-cli/blob/main/LICENSE)

# <img src="https://github.com/AmigoAppAI/amigo-cli/assets/1038572/d8651b83-6d4d-4334-9dd5-9a0fc5088447" width="25" height="25"> Amigo Terminal Assistant

---

Amigo is a terminal based copilot to help you work with large projects from your terminal.

With Amigo it is _easy_ to coordinate changes across many files, in some cases implementing entire features from a single prompt.

Amigo is incredibly efficient by leveraging state of the art techniques to use only the most relevent snippets of files as part of its prompt. Saving you money!

Want help understanding a new codebase? Need to add a new feature? Refactor existing code? Amigo can do it!

# ⚙️ Setup

## Install

To install Amigo you will need Python 3.10 or later installed. Then it's easy!

```
python3 -m venv .venv && source .venv/bin/activate # Optional
python3 -m pip install git+https://github.com/AmigoAppAI/amigo-cli.git
```
### Add your OpenAI API Key

There are a few options to provide Amigo with your OpenAI API key:

1. Create a `.env` file with the line `OPENAI_API_KEY=<your-api-key>` in the directory you plan to run amigo in or in `~/.amigo/.env`
2. Run `export OPENAI_API_KEY=<your key here>` prior to running Amigo
3. Place the previous command in your `.bashrc` or `.zshrc` to export your key on every terminal startup

# 🚀 Usage

Run Amigo from within your project directory. Amigo uses git, so if your project doesn't already have git set up, run `git init`. Then you can run Amigo with:

`amigo <paths to files or directories>`

List the files you would like Amigo to read and edit as arguments. Amigo will add each of them to it's vector database. To add multiple files at once, you can also provide directories as arguments. When a directory is provided, Amigo will add all the contained files, except for ones ignored in your `.gitignore`. In addition to files and directories, you can use [glob patterns](https://docs.python.org/3/library/glob.html) to add multiple files at once.

Enjoy!
