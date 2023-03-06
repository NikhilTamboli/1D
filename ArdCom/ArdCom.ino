//Arduino forum 2020 - https://forum.arduino.cc/index.php?topic=714968
#include <FastLED.h>

#define NUM_LEDS 15
uint8_t max_bright = 10;                                     // Overall brightness definition. It can be changed on the fly.

const byte resolution = 2;

#define DATA_PIN 13

CRGB leds[NUM_LEDS];

int myArray[15]; //this value is the upgratable data
byte* ddata = reinterpret_cast<byte*>(&myArray); // pointer for transferData()
size_t pcDataLen = sizeof(myArray);
bool newData=false;

void setup() {
  Serial.begin(115200);//baudrate
  FastLED.addLeds<WS2812B, DATA_PIN, GRB>(leds, NUM_LEDS);  // GRB ordering is typical
  for(int i = 0; i < NUM_LEDS; i++)
  {
    leds[i] = 0x0000ff;
    FastLED.show();
    delay(5);
    leds[i] = 0x000000;
  }
  FastLED.show();
}

void loop() {
    checkForNewData();
    if (newData == true) {
        newData = false;
    }
    // Serial.println("loop");
    toPy(myArray[0],myArray[1],myArray[2],myArray[3],myArray[4],myArray[5],myArray[6],myArray[7],myArray[8],
    myArray[9],myArray[10],myArray[11],myArray[12],myArray[13],myArray[14]); //here write the send data
    }

void checkForNewData () {
    if (Serial.available() >= pcDataLen && newData == false) {
        byte inByte;
        for (byte n = 0; n < pcDataLen; n++) {
            ddata [n] = Serial.read();
        }
        while (Serial.available() > 0) { // now make sure there is no other data in the buffer
             byte dumpByte =  Serial.read();
             Serial.println(dumpByte);
        }
        newData = true;
    }

}


void toPy(int a,int b,int c,int d,int e,int f,
          int g,int h,int i,int j,int k,int l,
          int m,int n,int o)//19 datas
{
  //rpidata="[1,2,3,4,5,6,7,8,9,10,111,0]";
// String data="["+String(a)+","+String(b)+","+String(c)+","+String(d)+","+String(e)+","+String(f)+","+String(g)+","+String(h)+","+String(i)+","+
// String(j)+","+String(k)+","+String(l)+","+String(m)+","+String(n)+","+String(o)+","+String(p)+","+String(q)+","+String(r)+","+String(s)+"]";
//   delay(50);
//   Serial.println(data);

  // for(int z=0; z<15; z++){
  //   leds[z] = CRGB(255, 255, 255);
  // }  
  leds[0].g = a;
  leds[1].g = b;
  leds[2].g = c;
  leds[3].g = d;
  leds[4].g = e;
  leds[5].g = f;
  leds[6].g = g;
  leds[7].g = h;
  leds[8].g = i;
  leds[9].g = j;
  leds[10].g = k;
  FastLED.show();
  // FastLED.setBrightness(OutVal);
  
}