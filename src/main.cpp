#include <Windows.h>
#include <iostream>
#include "roblox/memory.h"
#include "roblox/offsets.h"

int main() {
    if (!Memory::Initialize()) {
        std::cerr << "Failed to initialize memory!" << std::endl;
        return 1;
    }

    std::cout << "Jailbreak Roblox Trainer" << std::endl;
    std::cout << "Press F6 to toggle infinite money" << std::endl;

    while (true) {
        if (GetAsyncKeyState(VK_F6) & 1) {
            Memory::ToggleInfiniteMoney();
        }
        Sleep(100);
    }

    return 0;
}