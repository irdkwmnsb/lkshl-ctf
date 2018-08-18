#include <iostream>

int main()
{
    std::string message = ENC_MESSAGE;
    for (char& c : message) {
        c = ~c;
    }
    std::cout << message << std::endl;
}
