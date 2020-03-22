from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

hostname_var = str(subprocess.run('hostname', 
                                  capture_output=True, 
                                  text=True).stdout).strip()

ip_var = str(subprocess.run(['hostname', '-I'], 
                            capture_output=True, 
                            text=True).stdout).strip()

ipv4_var = ip_var.split(" ", 1)[0]

cpus_var = str(subprocess.run(['nproc', '--all'], 
                                  capture_output=True, 
                                  text=True).stdout).strip()

cmd = "free -h | awk '/Mem\:/ {print $2}'"

mem_var = str(subprocess.run(cmd, 
                             shell=True,
                             capture_output=True, 
                             text=True).stdout).strip()

@app.route('/status')
def get_status():
    return jsonify(hostname=hostname_var,
                   ip_address=ipv4_var,
                   cpus=cpus_var,
                   memory=mem_var)
    
if __name__ == "__main__":
    app.run(port=8080)

