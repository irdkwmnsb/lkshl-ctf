import uuid
import random
import string


random.seed("LKL1_2018_BROADCAST")
FLAG = "LKL{{y0u_h4ve_13arnt_w3bs0cket_m4gic_{}}}"
ALPHABET = string.ascii_letters + string.digits


def get_rand_uuid():
    return uuid.UUID(bytes=bytes(bytearray(random.getrandbits(8) for _ in range(16))))


def get_rand_text():
    return "".join(random.choice(ALPHABET) for _ in range(8))


if __name__ == '__main__':
    flags = {get_rand_uuid(): FLAG.format(get_rand_text()) for _ in range(500)}
    with open("flags_and_teams.py", mode="w") as flags_file:
        flags_file.writelines([
            "FLAGS = {\n",
            *["    \"{}\": \"{}\",\n".format(key, flags[key]) for key in sorted(flags)],
            "}"
        ])
