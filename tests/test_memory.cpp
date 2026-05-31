#include "../src/roblox/memory.h"
#include <cassert>

void TestMemoryInitialization() {
    assert(Memory::Initialize() == false); // Should fail in test env
}

int main() {
    TestMemoryInitialization();
    return 0;
}