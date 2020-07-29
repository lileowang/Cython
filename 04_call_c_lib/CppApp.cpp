/// Author:     Li Leo Wang
/// Date:       2020-07-29
/// Description:
/// - Test c code to be used by Cython.
/// 
/// Notes:
/// - Project > properties > C/C++ > precompiled header:
///     not using
/// 


//#include "pch.h"
#include <iostream>
#include "fact.h"

using namespace std;

int main()
{
    cout << "factorial of 5 = " << fact(5) << endl;
}

