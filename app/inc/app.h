#ifndef __APP_H
#define __APP_H

#include <stdio.h>
#include "main.h"
#include "cmsis_os2.h"

typedef enum {
    led_blink = 0,
    led_open,
    led_close
}LedState;

// #ifdef DEBUG
// #define debug(format,...) printf("[debug] "format"\r\n",##__VA_ARGS__)
// #else
// #define debug(format,...)
// #endif
 
#endif
