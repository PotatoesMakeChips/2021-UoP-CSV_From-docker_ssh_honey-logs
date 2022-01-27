# CSV from Docker SSH Honeypot Logs
This code provides an automated method for converting the output logs from https://github.com/random-robbie/docker-ssh-honey to a CSV format for analysis.
Also included is further tools develouped for use as part of the university module "forensic investigation" and the dataset colected as part of the investigation. The tools have hard coded values for CSV files that are provided as part of the dataset, howerver ar not in the root of the project like the code expects. The code will have to be modified to point to your own file if you wish to provide one

### Method Used for Obtaing Log File
The command `docker logs ssh-honeypot > nyc3-ssh.log` was used to retreave the log from teh docker container `ssh-honeypot` should be changed to the name of your container and `nyc3-ssh.log` should be changed to the name of the file you wish to output the logs to. Check that there are no extra error lines in your ssh log and that each ssh access atempt has its own line. Multiple access atempts on one line will create errors.
