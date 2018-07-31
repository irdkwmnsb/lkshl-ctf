import multiprocessing
import socket
from typing import Tuple

import flags_and_teams

import random
def get_task() -> Tuple[str, str]:
    n1 = random.randint(-10, 10)
    n2 = random.randint(-10, 10)
    p = random.choice(["+", "-", "*"])
    s = f"{n1} {p} {n2}"
    return (s, str(int(eval(s))))

def handle(connection: socket.socket, address):
    import logging
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger("process-%r" % (address,))
    try:
        logger.debug("Connected %r at %r", connection, address)

        flag = "Something unexpected happened. If you see this message, please contact us"

        connection.sendall("Hello stranger, i don't identify you. Maybe you introduce yourself? ".encode())
        while True:
            data = connection.recv(1024)
            if data == "":
                logger.debug("Socket closed remotely")
                break

            team = data.decode('UTF-8') #type: str
            team = team.strip()
            flag = flags_and_teams.data.get(team, None)
            if flag:
                break
            else:
                connection.sendall("I still can't identify you. mb try again? ".encode())


        connection.sendall("Ok. Here is you task:\n".encode())
        for i in range(100):
            eq = get_task()
            logger.debug("Made problem: %s", eq)
            connection.sendall("What is ".encode())
            connection.sendall(eq[0].encode())
            connection.sendall("\n".encode())
            data = None
            try:
                connection.settimeout(3)
                data = connection.recv(1024)
            except:
                pass
            logger.debug("Received data %r", data)

            if not data:
                logger.debug("Timeout".encode())
                connection.sendall("Time is up!\n".encode())
                connection.close()
                break

            ans = data.decode().strip()
            logging.debug("Interpreting as %r", ans)
            if ans != eq[1]:
                logging.debug("Incorrect")
                connection.sendall("Incorrect\n".encode())
                connection.close()
                break
            else:
                connection.sendall("Correct\n".encode())
                logging.debug("Correct")
        else:
            connection.sendall("Congratulations! Your flag is %s \n".format(flag).encode())
    except:
        logger.exception("Problem handling request")
    finally:
        logger.debug("Closing socket")
        connection.close()

class Server(object):
    def __init__(self, hostname, port):
        import logging
        self.logger = logging.getLogger("server")
        self.hostname = hostname
        self.port = port

    def start(self):
        self.logger.debug("listening")
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.hostname, self.port))
        self.socket.listen(1)

        while True:
            conn, address = self.socket.accept()
            self.logger.debug("Got connection")
            process = multiprocessing.Process(target=handle, args=(conn, address))
            process.daemon = True
            process.start()
            self.logger.debug("Started process %r", process)

if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.DEBUG)
    server = Server("0.0.0.0", 73)
    try:
        logging.info("Listening")
        server.start()
    except:
        logging.exception("Unexpected exception")
    finally:
        logging.info("Shutting down")
        for process in multiprocessing.active_children():
            logging.info("Shutting down process %r", process)
            process.terminate()
            process.join()
    logging.info("All done")