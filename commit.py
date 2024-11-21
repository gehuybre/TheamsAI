import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print(result.stdout)

def git_add_commit_push():
    # Add all files to the staging area
    run_command("git add .")
    
    # Commit the changes
    run_command('git commit -m "Automated commit"')
    
    # Force push to the remote repository
    run_command("git push -u origin main --force")

if __name__ == "__main__":
    git_add_commit_push()