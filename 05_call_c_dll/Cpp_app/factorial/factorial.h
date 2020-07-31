#pragma once

// Avoid C++ name mangling with extern "C"
// Export from a DLL Using __declspec(dllexport)
#define EXTERN_DLL_EXPORT extern "C" __declspec(dllexport)

EXTERN_DLL_EXPORT int fact(int val);
