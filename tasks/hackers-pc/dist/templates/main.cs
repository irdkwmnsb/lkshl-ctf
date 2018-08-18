using System;
using System.Collections.Generic;

namespace LKSHL_CTF
{
    class Ctf
    {
        public static void Main(string[] args)
        {
            byte[] permittedKey = new byte[] {
                @@_PERMITTED_KEY_@@
            };

            Console.Write("Enter the access key: ");
            char[] input = Console.ReadLine().ToCharArray();

            if (input.Length != permittedKey.Length) {
                Console.WriteLine("Access Denied");
                return;
            }

            byte[] encrypted = new byte[input.Length];
            for (int i = 0; i < input.Length; ++i) {
                encrypted[i] = (byte)((byte)(((i + 143) * 185) % 253) ^ (byte)input[i]);
            }

            bool equal = true;
            for (int i = 0; i < input.Length; ++i) {
                if (encrypted[i] != permittedKey[i]) {
                    equal = false;
                }
            }

            if (equal) {
                Console.WriteLine("Access Granted");
                Console.WriteLine("The flag is {0}", new string(input));
            } else {
                Console.WriteLine("Access Denied");
            }
        }
    }
}
