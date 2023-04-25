#include <avr/io.h> 			//This is a header file that includes I/O definitions of the AVR microcontroller used in the program.
#include <util/delay.h>		//This is a header file for the util delay library, which provides the delay functions that are used in the program.
#include <string.h>			//
#include <stdlib.h>			//provides several general-purpose functions, including `atof()`, which is used to convert strings to floating-point numbers.
#include <stdio.h>			// provides functions for input and output operations, including `sprintf()`, which could be used if the program needed to format strings for outputs; however, this program uses `dtostrf()` instead.


#define BAUDRATE 9600		//This is a macro used to define the baud rate used for serial communication.
#define F_CPU 16000000UL	// This macro defines the clock frequency of the microcontroller
#define BAUD_PRESCALER ((F_CPU/16/BAUDRATE)-1) 	//This macro calculates the value of UBRR register needed to set the desired baud rate.

void USART_init() {		//: This function initializes the USART module with the specified settings. This function sets the baud rate and the data frame structure, and enables transmission and reception.
    // Set baud rate
    UBRR0H = (uint8_t)(BAUD_PRESCALER>>8);
    UBRR0L = (uint8_t)(BAUD_PRESCALER);
   
   // Enable Rx and Tx
    UCSR0B = (1<<TXEN0)|(1<<RXEN0);
    // Set frame format: 8 data bits, 1 stop bit, no parity
    UCSR0C = (1<<UCSZ01)|(1<<UCSZ00);
}

char USART_receive() {
    // Wait for data to be received
    while(!(UCSR0A & (1<<RXC0)));

    // Get and return received data from buffer
    return UDR0;
}

void USART_transmit(char data) {	//This function sends a single character data over USART
    while (!(UCSR0A & (1<<UDRE0)));	//This code is used in the `USART_transmit()` function to wait for the USART data register to become empty before writing to it. // Wait for empty transmit buffer
    UDR0 = data;				// This code in the `USART_transmit()` function writes a character to the USART data register.
}

void USART_send_string(char *str) {	//This function sends a null-terminated string of characters over USART
    while (*str > 0) {
        USART_transmit(*str++);		//This code in the `USART_send_string` function transmits each character in the string, one at a time, by calling the `USART_transmit()` function
    }
}

int main(void) {
    USART_init();
    char test_string[] = "Hello World\r\n";
    char gps_data[82]; // maximum size of GPS message
    char lat_str[10], lng_str[10];
    double latitude, longitude;
    while (1) {
        //USART_send_string(test_string);
        //_delay_ms(500);
        char received_char = USART_receive();

        // Echo received character back
        USART_transmit(received_char);
	//  char buffer[256];
  //   int index = 0;

  //   // Wait for GPS data
  //   while(USART_receive() != '$');

  //   // Read in GPS data until end of message
  //   while(1)
  //   {
  //     char c = USART_receive();
  //     buffer[index++] = c;
  //     if(c == '\0') break;
  //   }

  //   // Print the GPS data
  //   buffer[index] = '\0';
  //   printf("%s\n", buffer);  
  //   USART_send_string(buffer);
    }
    return 0;
}