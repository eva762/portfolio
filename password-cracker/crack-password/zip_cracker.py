import zipfile

def crack_zip(zip_path, wordlist_path):
    with zipfile.ZipFile(zip_path) as zf:
        with open(wordlist_path, 'r', encoding='latin-1') as f:
            for line in f:
                password = line.strip()
                try:
                    zf.extractall(pwd=bytes(password, 'utf-8'))
                    print(f'Success! Password is: {password}')
                    return password
                except:
                    print(f'Failed with password: {password}')
    print('No valid password found.')
    return None

crack_zip('secret.zip', 'wordlist.txt')