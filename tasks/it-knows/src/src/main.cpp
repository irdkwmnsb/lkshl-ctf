#include <iostream>
#include <string>

int main()
{
    std::string flag = "LKSHL{U5E_STR1NG5_UT1LITY_##########}";
    while (true) {
        std::cout << "Do you want the flag? [yes/no]" << std::endl;
        std::string ans;
        std::cin >> ans;
        if (ans == "yes") {
            std::cout << "I don't care" << std::endl;
            return 1; // Mhu-ha-ha-ha
            std::cout << flag << std::endl;
        } else if (ans == "no") {
            std::cout << "OK" << std::endl;
            return 1;
        } else {
            std::cout << "What did you say?" << std::endl;
        }
    }
}
