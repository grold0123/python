import subprocess
import datetime

# Generate a commit message with timestamp

def add():
    # Stage all changes
    subprocess.run(["git", "add", "."], check=True)
def push():
    # Push to remote (default branch)
    subprocess.run(["git", "push"], check=True)
def commit(commit_message):
    # Commit with message
    subprocess.run(["git", "commit", "-m", commit_message], check=True)



commit_message = f"Update on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
subprocesses_ = [(add,()),(commit,(commit_message,)),(push,())]

for (fn,args) in subprocesses_:
    fn(*args)