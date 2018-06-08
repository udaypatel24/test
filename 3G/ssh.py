import paramiko
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('enzenglobal.tk', port='48152', username='90070356', password='Ami@22222')
stdin, stdout, stderr=ssh.exec_command('touch thita1')

#output = stdout.readlines()
#print '\n'.join(output)

#for line in stdout.readines():
#        print line.strip()

ssh.close()
