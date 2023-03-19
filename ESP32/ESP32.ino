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

#define NUM_LEDS 20
uint8_t max_bright = 1;                                     // Overall brightness definition. It can be changed on the fly.

int myArray[NUM_LEDS]; //this value is the upgratable data
byte* ddata = reinterpret_cast<byte*>(&myArray); // pointer for transferData()
size_t pcDataLen = sizeof(myArray);
bool newData=false;


// How many NeoPixels are attached to the Arduino?
#define NUMPIXELS 20 // Popular NeoPixel ring size

// When setting up the NeoPixel library, we tell it how many pixels,
// and which pin to use to send signals. Note that for older NeoPixel
// strips you might need to change the third parameter -- see the
// strandtest example for more information on possible values.
Adafruit_NeoPixel pixels(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

#define DELAYVAL 500 // Time (in milliseconds) to pause between pixels

void setup() {
  Serial.begin(115200);
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
    // Serial.println("loop");
    // toPy(myArray[0],myArray[1],myArray[2],myArray[3],myArray[4],myArray[5],myArray[6],myArray[7],myArray[8],
    // myArray[9],myArray[10],myArray[11],myArray[12],myArray[13],myArray[14],myArray[15],myArray[16],myArray[17],
    // myArray[18],myArray[19],myArray[20],myArray[21],myArray[22],myArray[23],myArray[24],myArray[25],myArray[26],
    // myArray[27],myArray[28],myArray[29],myArray[30],myArray[31],myArray[32],myArray[33],myArray[34],myArray[35],
    // myArray[36],myArray[37],myArray[38],myArray[39],myArray[40],myArray[41],myArray[42],myArray[43],myArray[44],myArray[45],
    // myArray[46],myArray[47],myArray[48],myArray[49],myArray[50],myArray[51],myArray[52],myArray[53],myArray[54],myArray[55],
    // myArray[56],myArray[57],myArray[58],myArray[59]);
    toPy(myArray[0],myArray[1],myArray[2],myArray[3],myArray[4],myArray[5],myArray[6],myArray[7],myArray[8],
    myArray[9],myArray[10],myArray[11],myArray[12],myArray[13],myArray[14],myArray[15],myArray[16],myArray[17],
    myArray[18],myArray[19]);

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
        while (Serial.available() > 0) { // now make sure there is no other data in the buffer
            byte dumpByte =  Serial.read();
            //  Serial.println(dumpByte);
        }
        newData = true;
    }

}

// void toPy(int a,int b,int c,int d,int e,int f,
//           int r,int h,int i,int j,int k,int l,
//           int m,int n,int o,int o1,int o2,int o3,
//           int o4,int o5,int o6,int o7,int o8,int o9,
//           int o10,int o11,int o12,int o13,int o14,int o15,
//           int o16,int o17,int o18,int o19,int o20,int o21,
//           int o22,int o23,int o24,int o25,int o26,int o27,//19 datas
//           int o28,int o29,int o30,int o31,int o32,int o33,
//           int o34,int o35,int o36,int o37,int o38,int o39,
//           int o40,int o41,int o42,int o43,int o44,int o45)
void toPy(int a,int b,int c,int d,int e,int f,
          int g,int h,int i,int j,int k,int l,
          int m,int n,int o,int o1,int o2,int o3,
          int o4,int o5)
{

  // for(int z=0; z<15; z++){
  //   leds[z] = CRGB(255,255,255);
  // }  
  // Serial.println(a);
  pixels.setPixelColor(0, pixels.Color(0, a, 0));
  pixels.setPixelColor(1, pixels.Color(0, b, 0));
  pixels.setPixelColor(2, pixels.Color(0, c, 0));
  pixels.setPixelColor(3, pixels.Color(0, d, 0));
  pixels.setPixelColor(4, pixels.Color(0, e, 0));
  pixels.setPixelColor(5, pixels.Color(0, f, 0));
  pixels.setPixelColor(6, pixels.Color(0, g, 0));
  pixels.setPixelColor(7, pixels.Color(0, h, 0));
  pixels.setPixelColor(8, pixels.Color(0, i, 0));
  pixels.setPixelColor(9, pixels.Color(0, j, 0));
  pixels.setPixelColor(10, pixels.Color(0, k, 0));
  pixels.setPixelColor(11, pixels.Color(0, l, 0));
  pixels.setPixelColor(12, pixels.Color(0, m, 0));
  pixels.setPixelColor(13, pixels.Color(0, n, 0));
  pixels.setPixelColor(14, pixels.Color(0, o, 0));
  pixels.setPixelColor(15, pixels.Color(0, o1, 0));
  pixels.setPixelColor(16, pixels.Color(0, o2, 0));
  pixels.setPixelColor(17, pixels.Color(0, o3, 0));  
  pixels.setPixelColor(18, pixels.Color(0, o4, 0));
  pixels.setPixelColor(19, pixels.Color(0, o5, 0));
  pixels.show();
  // leds[0].r = 100;
  // leds[1].r = 100;
  // leds[2].r = 100;
  // leds[3].r = d;
  // leds[4].r = e;
  // leds[5].r = f;
  // leds[6].r = g;
  // leds[7].r = h;
  // leds[8].r = i;
  // leds[9].r = j;
  // leds[10].r = k;
  // leds[11].r = l;
  // leds[12].r = m;
  // leds[13].r = n;
  // leds[14].r = o;
  // leds[15].r = o1;
  // leds[16].r = o2;
  // leds[17].r = o3;
  // leds[18].r = o4;
  // leds[19].r = o5;
  // leds[20].r = o6;
  // leds[21].r = o7;
  // leds[22].r = o8;
  // leds[23].r = o9;
  // leds[24].r = o10;
  // leds[25].r = o11;
  // leds[26].r = o12;
  // leds[27].r = o13;
  // leds[28].r = o14;
  // leds[29].r = o15;
  // leds[30].r = o16;
  // leds[31].r = o17;
  // leds[32].r = o18;
  // leds[33].r = o19;
  // leds[34].r = o20;
  // leds[35].r = o21;
  // leds[36].r = o22;
  // leds[37].r = o23;
  // leds[38].r = o24;
  // leds[39].r = o25;
  // leds[40].r = o26;
  // leds[41].r = o27;
  // leds[42].r = o28;
  // leds[43].r = o29;
  // leds[44].r = o30;
  // leds[45].r = o31;
  // leds[46].r = o32;
  // leds[47].r = o33;
  // leds[48].r = o34;
  // leds[49].r = o35;
  // leds[50].r = o36;
  // leds[51].r = o37;
  // leds[52].r = o38;
  // leds[53].r = o39;
  // leds[54].r = o40;
  // leds[55].r = o41;
  // leds[56].r = o42;
  // leds[57].r = o43;
  // leds[58].r = o44;
  // leds[59].r = o45;



  // FastLED.show();
  // FastLED.setBrightness(OutVal);
  
}
