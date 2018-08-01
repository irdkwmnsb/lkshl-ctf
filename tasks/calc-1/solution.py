import nclib

nc = nclib.Netcat(("localhost", 73), verbose = True)
nc.echo_recving = True
nc.echo_sending = True
nc.send_line("team_1".encode())
while True:
    s = ""
    while not s.startswith("What is"):
        s = nc.read_line().decode()
    eq = s[len("What is "):]
    result = str(eval(eq))
    nc.send_line(result.encode())