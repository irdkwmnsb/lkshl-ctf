import multiprocessing
import socket
from typing import Tuple

import flags_and_teams

import random
class Calc2Task:
    def __init__(self):
        while True:
            try:
                n1 = random.randint(-10, 10)
                n2 = random.randint(-10, 10)
                n3 = random.randint(-10, 10)
                n4 = random.randint(-10, 10)
                p1 = random.choice(["+", "-", "*", "/"])
                p2 = random.choice(["+", "-", "*", "/"])
                p3 = random.choice(["+", "-", "*", "/"])
                bo = random.randint(1, 3)
                bc = random.randint(bo+1, 4)
                s = "(" if bo == 1 else ""
                s += f"{n1}"
                s += f" {p1} "
                s += "(" if bo == 2 else ""
                s += f"{n2}"
                s += ")" if bc == 2 else ""
                s += f" {p2} "
                s += "(" if bo == 3 else ""
                s += f"{n3}"
                s += ")" if bc == 3 else ""
                s += f" {p3} "
                s += f"{n4}"
                s += ")" if bc == 4 else ""
                self.task = s
                self.eth = float(eval(s))
                break
            except ZeroDivisionError:
                pass
    eps = 1e-4
    def check(self, answer: str):
        ans = float(answer)
        return abs(self.eth-ans)<self.eps



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
            T = Calc2Task()
            eq = T.task
            logger.debug("Made problem: %s", eq)
            connection.sendall("What is ".encode())
            connection.sendall(eq.encode())
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
                connection.shutdown(socket.SHUT_RDWR)
                break

            if T.check(data.decode()):
                connection.sendall("Correct\n".encode())
                logger.debug("Correct")
            else:
                logger.debug("Incorrect")
                connection.sendall("Incorrect\n".encode())
                connection.shutdown(socket.SHUT_RDWR)
                break
        else:
            logger.warning(f"Team {team} solved!")
            connection.sendall("Congratulations! Your flag is {0} \n".format(flag).encode())
    except:
        logger.exception("Problem handling request")
    finally:
        logger.debug("Closing socket")
        connection.shutdown(socket.SHUT_RDWR)
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
    server = Server("0.0.0.0", 74)
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