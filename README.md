## Requirements

- Python 3.4 +
- OpenSSL (latest version)
- Pip

## Linux

If you are running on a Linux flavor, you’ll need a few extra packages before you start. You can download these packages by running:

```
$ sudo apt-get install python-dev libssl-dev
```

Instead of `python-dev` you may need to specify your Python version

```
$ sudo apt-get install python3.6-dev libssl-dev
```

## Windows

With windows you will need to have the latest OpenSSL version. Install OpenSSL [32-bit](http://slproweb.com/download/Win32OpenSSL-1_1_0h.exe) or [64-bit](http://slproweb.com/download/Win64OpenSSL-1_1_0h.exe)

## Mac

If you do not have the latest version of OpenSSL you will encounter some installation issues with creating new applications since we need to download a zip of the application via GitHub.

With Mac you can install OpenSSL through `brew`.

```
brew install openssl
```

Python 3.6 does not come preinstalled with certificates so you may need to install certificates with this command:

```
/Applications/Python\ 3.6/Install\ Certificates.command
```

You should now be good to install new Masonite application of Mac :)

### Python 3.7

If you are using [Python 3.7](https://www.python.org/downloads/windows/), add it to your PATH Environment variable.

Open Windows PowerShell and run: `pip install masonite-cli`

Add `C:\Users\%USERNAME%\.AppData\Programs\Python\Python37\Scripts\` to PATH Environment variable.

Note: PATH variables depend on your installation folder

## Installation:

```
    $ pip3 install masonite-cli :: (may need sudo if using UNIX) ::
    $ craft new project
    $ cd project
    $ craft install
    $ craft serve
```

Go to `http://localhost:8000/`

## License

The Masonite framework is open-sourced software licensed under the MIT license. 