import multiprocessing
import socket
from datetime import datetime
from typing import Tuple

import flags_and_teams

import random
class Calc2Task:
    def __init__(self):
        a = random.randint(0, 10)
        b = random.randint(0, 10)
        self.eth = a+b
        self.task = f"{a} + {b}"
        
    def check(self, answer: str):
        try:
            ans = float(answer)
            return ans == self.eth
        except ValueError:
            return False

import logging
def init_logger(logger):
    logger.setLevel(logging.DEBUG)
    
    log_formatter = logging.Formatter("[%(asctime)s] [%(name)8s:%(process)-6.6s] [%(levelname)-5.5s] --- %(message)s")

    file_handler = logging.FileHandler("./latest.log")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(log_formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(log_formatter)
    logger.addHandler(console_handler)
    
def handle(connection: socket.socket, address):
    try:
        logger = logging.getLogger("handler")
        init_logger(logger)
        logger.info("Connected at %r", address)

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
            if(i == 10):
                connection.sendall("Congratulations, you solved 10 problems! But the thing is that this task is from the PPC category. This means that you need to write a program to get the flag. In order to check who solves the problems, we put a limit of half a second, so do not try to solve it manually either. I advise you to use the sockets library in python\n".encode())
            connection.sendall("What is ".encode())
            connection.sendall(eq.encode())
            connection.sendall("\n".encode())
            data = None
            try:
                if(i>9):
                    connection.settimeout(0.5)
                data = connection.recv(1024)
                connection.settimeout(10)
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
            logger.warning(f"Team {team}{address} solved!")
            connection.sendall("Congratulations! Your flag is {0} \n".format(flag).encode())
    except:
        logger.exception("Problem handling request")
        connection.sendall(("Something wrong happent. If you see this, please contact admins with this timestamp: " + \
                                datetime.now().strftime("%D %X:%f")).encode())
    finally:
        logger.debug("Closing socket")
        connection.shutdown(socket.SHUT_RDWR)
        connection.close()

class Server(object):
    def __init__(self, hostname, port):
        self.logger = logging.getLogger("server")
        init_logger(self.logger)
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
    logger = logging.getLogger("main")
    init_logger(logger)
    import sys
    port = int(sys.argv[1])
    server = Server("0.0.0.0", port)
    try:
        logger.info("Listening")
        server.start()
    except:
        logger.exception("Unexpected exception")
    finally:
        logger.info("Shutting down")
        for process in multiprocessing.active_children():
            logger.info("Shutting down process %r", process)
            process.terminate()
            process.join()
    logger.info("All done")