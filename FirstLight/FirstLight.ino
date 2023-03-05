// Use if you want to force the software SPI subsystem to be used for some reason (generally, you don't)
// #define FASTLED_FORCE_SOFTWARE_SPI
// Use if you want to force non-accelerated pin access (hint: you really don't, it breaks lots of things)
// #define FASTLED_FORCE_SOFTWARE_SPI
// #define FASTLED_FORCE_SOFTWARE_PINS
#include <FastLED.h>

///////////////////////////////////////////////////////////////////////////////////////////
//
// Move a white dot along the strip of leds.  This program simply shows how to configure the leds,
// and then how to turn a single pixel white and then off, moving down the line of pixels.
// 

// How many leds are in the strip?
#define NUM_LEDS 60
uint8_t max_bright = 128;                                     // Overall brightness definition. It can be changed on the fly.

const byte resolution = 2;
//const byte numChars = NUM_

// For led chips like WS2812, which have a data line, ground, and power, you just
// need to define DATA_PIN.  For led chipsets that are SPI based (four wires - data, clock,
// ground, and power), like the LPD8806 define both DATA_PIN and CLOCK_PIN
// Clock pin only needed for SPI based chipsets when not using hardware SPI
#define DATA_PIN 13
// #define CLOCK_PIN 13
#define NUM_LEDS  60
// This is an array of leds.  One item for each led in your strip.
CRGB leds[NUM_LEDS];

// This function sets up the ledsand tells the controller about them
void setup() {
	// sanity check delay - allows reprogramming if accidently blowing power w/leds
    FastLED.addLeds<WS2812B, DATA_PIN, RGB>(leds, NUM_LEDS);  // GRB ordering is typical
    Serial.begin(9600);
  for(int i = 0; i < NUM_LEDS; i++)
  {
    leds[i] = 0x0000ff;
    FastLED.show();
    delay(5);
    leds[i] = 0x000000;
  }
  FastLED.show();
}

// This function runs over and over, and is where you do the magic to light
// your leds.

void loop() {
   // Move a single white led 
   if(Serial.available()){
    int data[181];
    for(int i=0;i<181;i++){
      int b = Serial.parseInt();
      data[i] = b;
    }  
    // int j=0;
    for(int j=0;j<60;j++){
      leds[j].g = (int)data[j*3+1];
      leds[j].r = (int)data[j*3+2];
      leds[j].b = (int)data[j*3+3];
      FastLED.show();
    }
      

   }

  // if(Serial.available()){
  //     for(int i = 0; i < NUM_LEDS; i++)
  //     {
  //       leds[i].g = Serial.parseInt();
  //       leds[i].b = Serial.parseInt();
  //       leds[i].r = Serial.parseInt();
  //     }
  //     FastLED.show();            
  // }

}
