#pragma once
#include <Windows.h>

namespace Memory {
    bool Initialize();
    void ToggleInfiniteMoney();
    template<typename T> T Read(uintptr_t address);
    template<typename T> void Write(uintptr_t address, T value);
}