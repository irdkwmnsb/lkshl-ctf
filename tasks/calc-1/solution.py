import nclib
import sys

team_id = sys.argv[3]
nc = nclib.Netcat((sys.argv[1], int(sys.argv[2])), verbose = True)
nc.echo_recving = True
nc.echo_sending = True
nc.send_line(team_id.encode())
while True:
    s = ""
    while not s.startswith("What is"):
        s = nc.read_line().decode()
    eq = s[len("What is "):]
    result = str(eval(eq))
    nc.send_line(result.encode())
