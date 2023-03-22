// NeoPixel Ring simple sketch (c) 2013 Shae Erisson
// Released under the GPLv3 license to match the rest of the
// Adafruit NeoPixel library

#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
 #include <avr/power.h> // Required for 16 MHz Adafruit Trinket
#endif

// Which pin on the Arduino is connected to the NeoPixels?
#define PIN        13 
// On Trinket or Gemma, suggest changing this to 1

#define NUMPIXELS 20
uint8_t max_bright = 1;                                     // Overall brightness definition. It can be changed on the fly.

int myArray[NUMPIXELS]; //this value is the upgratable data
byte* ddata = reinterpret_cast<byte*>(&myArray); // pointer for transferData()
size_t pcDataLen = sizeof(myArray);
bool newData=false;


// How many NeoPixels are attached to the Arduino?

// When setting up the NeoPixel library, we tell it how many pixels,
// and which pin to use to send signals. Note that for older NeoPixel
// strips you might need to change the third parameter -- see the
// strandtest example for more information on possible values.
Adafruit_NeoPixel pixels(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

#define DELAYVAL 500 // Time (in milliseconds) to pause between pixels

void setup() {
  Serial.begin(230400);
  // These lines are specifically to support the Adafruit Trinket 5V 16 MHz.
  // Any other board, you can remove this part (but no harm leaving it):
#if defined(__AVR_ATtiny85__) && (F_CPU == 16000000)
  clock_prescale_set(clock_div_1);
#endif
  // END of Trinket-specific code.

  pixels.begin(); // INITIALIZE NeoPixel strip object (REQUIRED)
}

void loop() {
  pixels.clear(); // Set all pixel colors to 'off'

    checkForNewData();
    if (newData == true) {
        newData = false;
    }

    // test(myArray[0]);

    // toPy(myArray[0],myArray[1],myArray[2],myArray[3],myArray[4],myArray[5],myArray[6],myArray[7],myArray[8],
    // myArray[9],myArray[10],myArray[11],myArray[12],myArray[13],myArray[14],myArray[15],myArray[16],myArray[17],
    //  myArray[18],myArray[19]);
        toPy(myArray[0],myArray[1],myArray[2],myArray[3],myArray[4],myArray[5],myArray[6],myArray[7],myArray[8],
    myArray[9],myArray[10],myArray[11],myArray[12],myArray[13],myArray[14],myArray[15],myArray[16],myArray[17],myArray[18],myArray[19], myArray[20],myArray[21],myArray[22],myArray[23],myArray[24],
    myArray[25],myArray[26],myArray[27],myArray[28],myArray[29],myArray[30]);

  // The first NeoPixel in a strand is #0, second is 1, all the way up
  // to the count of pixels minus one.
  // for(int i=0; i<NUMPIXELS; i++) { // For each pixel...

  //   // pixels.Color() takes RGB values, from 0,0,0 up to 255,255,255
  //   // Here we're using a moderately bright green color:
  //   pixels.setPixelColor(i, pixels.Color(0, 150, 0));

  //   pixels.show();   // Send the updated pixel colors to the hardware.

  //   delay(DELAYVAL); // Pause before next pass through loop
  // }
  
}

void checkForNewData () {
    if (Serial.available() >= pcDataLen && newData == false) {
        // byte inByte;      
        for (byte n = 0; n < pcDataLen; n++) {
            ddata [n] = Serial.read();
        }
        // for(int i=0;i<31;i++){
        //   int a = int(Serial.read() | Serial.read() | Serial.read() | Serial.read());
        //   // int a = int(Serial.read());
        //   myArray[i]=a;
        // }

        while (Serial.available() > 0) { // now make sure there is no other data in the buffer
            byte dumpByte =  Serial.read();
            //  Serial.println(dumpByte);
        }
        newData = true;
    }

}

void toPy(int a,int b,int c,int d,int e,int f,
          int g,int h,int i,int j, int a1,int a2,int a3,int a4,int a5,int a6,int a7,int a8,int a9,int a10,
          int a11, int a12, int a13, int a14, int a15, int a16, int a17, int a18, int a19, int a20, int a21)
{

  pixels.setPixelColor(0, pixels.Color(0, a, 0));
  pixels.setPixelColor(1, pixels.Color(0, b, 0));
  pixels.setPixelColor(2, pixels.Color(0, c, 0));
  pixels.setPixelColor(3, pixels.Color(0, d, 0));
  pixels.setPixelColor(4, pixels.Color(0, e, 0));
  pixels.setPixelColor(5, pixels.Color(0, f, 0));
  pixels.setPixelColor(6, 0, g, 0);
  pixels.setPixelColor(7, pixels.Color(0, h, 0));
  pixels.setPixelColor(8, pixels.Color(0, i, 0));
  pixels.setPixelColor(9, pixels.Color(0, j, 0));
  pixels.setPixelColor(10, 0, a1, 0);
  pixels.setPixelColor(11, pixels.Color(0, a2, 0));
  pixels.setPixelColor(12, pixels.Color(0, a3, 0));
  pixels.setPixelColor(13, pixels.Color(0, a4, 0));
  pixels.setPixelColor(14, pixels.Color(0, a5, 0));
  pixels.setPixelColor(15, pixels.Color(0, a6, 0));
  pixels.setPixelColor(16, pixels.Color(0, a7, 0));
  pixels.setPixelColor(17, pixels.Color(0, a8, 0));
  pixels.setPixelColor(18, pixels.Color(0, a9, 0));
  pixels.setPixelColor(19, pixels.Color(0, a10, 0)); 
  pixels.setPixelColor(20, pixels.Color(0, a11, 0));
  pixels.setPixelColor(21, pixels.Color(0, a12, 0));
  pixels.setPixelColor(22, pixels.Color(0, a13, 0));
  pixels.setPixelColor(23, pixels.Color(0, a14, 0));
  pixels.setPixelColor(24, pixels.Color(0, a15, 0)); 
  pixels.setPixelColor(25, pixels.Color(0, a16, 0));
  pixels.setPixelColor(26, pixels.Color(0, a17, 0));
  pixels.setPixelColor(27, pixels.Color(0, a18, 0));
  pixels.setPixelColor(28, pixels.Color(0, a19, 0));
  pixels.setPixelColor(29, pixels.Color(0, a20, 0));
  pixels.setPixelColor(30, pixels.Color(255, a21, 0));
   


  pixels.show();
  
}


