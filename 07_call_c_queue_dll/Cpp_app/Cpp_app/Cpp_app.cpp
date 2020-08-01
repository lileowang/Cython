// Cpp_app.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

//#include "pch.h"
#include <iostream>
#include "queue.h"

using namespace std;

int main()
{
    Queue * q = queue_new();

    queue_push_tail(q, (QueueValue)10);
    queue_push_tail(q, (QueueValue)20);

    cout << "peek head: " << (int)queue_peek_head(q) << endl;
    cout << "pop head: " << (int)queue_pop_head(q) << endl;
    cout << "pop head: " << (int)queue_pop_head(q) << endl;
    cout << "pop head: " << (int)queue_pop_head(q) << endl;

    if (q != NULL)
    {
        queue_free(q);
    }
}

