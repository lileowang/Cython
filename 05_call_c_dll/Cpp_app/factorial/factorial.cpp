// factorial.cpp : Defines the exported functions for the DLL application.
//

#include "stdafx.h"
#include "factorial.h"

int fact(int val)
{
    if (val < 2)
    {
        return 1;
    }

    return val * fact(val - 1);
}

