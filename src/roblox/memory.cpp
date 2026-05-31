#include "memory.h"
#include "offsets.h"
#include <iostream>

namespace Memory {
    HANDLE processHandle;
    DWORD processId;
    uintptr_t moduleBase;

    bool Initialize() {
        HWND hwnd = FindWindowA(NULL, "Roblox");
        if (!hwnd) return false;

        GetWindowThreadProcessId(hwnd, &processId);
        processHandle = OpenProcess(PROCESS_ALL_ACCESS, FALSE, processId);
        if (!processHandle) return false;

        moduleBase = (uintptr_t)GetModuleHandleA("RobloxPlayerBeta.exe");
        return moduleBase != 0;
    }

    void ToggleInfiniteMoney() {
        uintptr_t moneyAddr = moduleBase + Offsets::MONEY_OFFSET;
        int currentMoney = Read<int>(moneyAddr);
        Write<int>(moneyAddr, currentMoney + 10000);
    }

    template<typename T> T Read(uintptr_t address) {
        T value;
        ReadProcessMemory(processHandle, (LPCVOID)address, &value, sizeof(T), NULL);
        return value;
    }

    template<typename T> void Write(uintptr_t address, T value) {
        WriteProcessMemory(processHandle, (LPVOID)address, &value, sizeof(T), NULL);
    }
}