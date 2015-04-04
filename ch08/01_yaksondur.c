#include <wiringPi.h>
int main (void)
{
  //modulu aktif et
  wiringPiSetup();
  //4 Numaral WiringPi Pin'ini Out moda al ve çıkışa hazırla
  pinMode(0, OUTPUT);
  //Sonsuz Döngü
  for(;;)
  {
    //4 Numaralı Pin'e High değerini ver
    digitalWrite(4, HIGH);
    //500 milisaniye bekle
    delay(500);
    //4 Numaralı Pin'e Low değerini ver
    digitalWrite(4, LOW);
    //ve 500 ms bekle
    delay(500);
  }
  return 0;
}