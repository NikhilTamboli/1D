//Arduino forum 2020 - https://forum.arduino.cc/index.php?topic=714968
#include <FastLED.h>

#define NUM_LEDS 20
uint8_t max_bright = 10;                                     // Overall brightness definition. It can be changed on the fly.

const byte resolution = 2;

#define DATA_PIN 13

CRGB leds[NUM_LEDS];

int myArray[NUM_LEDS]; //this value is the upgratable data
byte* ddata = reinterpret_cast<byte*>(&myArray); // pointer for transferData()
size_t pcDataLen = sizeof(myArray);
bool newData=false;

void setup() {
  Serial.begin(230400);//baudrate
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
     //here write the send data
    //  toPy(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60);
    }

void checkForNewData () {
    if (Serial.available() >= pcDataLen && newData == false) {
        byte inByte;
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
//           int g,int h,int i,int j,int k,int l,
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
  leds[11].g = l;
  leds[12].g = m;
  leds[13].g = n;
  leds[14].g = o;
  leds[15].g = o1;
  leds[16].g = o2;
  leds[17].g = o3;
  leds[18].g = o4;
  leds[19].g = o5;
  // leds[20].g = o6;
  // leds[21].g = o7;
  // leds[22].g = o8;
  // leds[23].g = o9;
  // leds[24].g = o10;
  // leds[25].g = o11;
  // leds[26].g = o12;
  // leds[27].g = o13;
  // leds[28].g = o14;
  // leds[29].g = o15;
  // leds[30].g = o16;
  // leds[31].g = o17;
  // leds[32].g = o18;
  // leds[33].g = o19;
  // leds[34].g = o20;
  // leds[35].g = o21;
  // leds[36].g = o22;
  // leds[37].g = o23;
  // leds[38].g = o24;
  // leds[39].g = o25;
  // leds[40].g = o26;
  // leds[41].g = o27;
  // leds[42].g = o28;
  // leds[43].g = o29;
  // leds[44].g = o30;
  // leds[45].g = o31;
  // leds[46].g = o32;
  // leds[47].g = o33;
  // leds[48].g = o34;
  // leds[49].g = o35;
  // leds[50].g = o36;
  // leds[51].g = o37;
  // leds[52].g = o38;
  // leds[53].g = o39;
  // leds[54].g = o40;
  // leds[55].g = o41;
  // leds[56].g = o42;
  // leds[57].g = o43;
  // leds[58].g = o44;
  // leds[59].g = o45;



  FastLED.show();
  // FastLED.setBrightness(OutVal);
  
}