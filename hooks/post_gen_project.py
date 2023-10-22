import subprocess

def main():
    print("Running 'git init'")
    subprocess.run(['git', 'init'], check=True)
    print("Initializing project")
    subprocess.run(['make', 'dev'], check=True)
    print("Project successfully initialized")
    return

if __name__ == "__main__":
    main()