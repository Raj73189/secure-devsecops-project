import subprocess

# insecure code (bandit will detect)
subprocess.call("ls -l", shell=True)
