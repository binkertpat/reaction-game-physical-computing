int schaltereins;
int schalterzwei;

int roteled = 6;
int ledspielereins = 7;
int ledspielerzwei = 5;

int spielereins = 2;
int spielerzwei = 4;

boolean sieg = false;

void setup() {
  pinMode(roteled, OUTPUT); //rote LED
  pinMode(ledspielereins, OUTPUT); //gruene LED Spieler 1
  pinMode(ledspielerzwei, OUTPUT); //gruene LED Spieler 2
  pinMode(spielereins, INPUT);
  pinMode(spielerzwei, INPUT);

  digitalWrite(roteled, HIGH);
  delay(random(1000,8000));                     
  digitalWrite(roteled, LOW);    
}

void spielereinssieg(){
  digitalWrite(ledspielereins, HIGH);
  Serial.println("Sieg für Spieler 1!");   
  sieg = true;
}

void spielerzweisieg(){
  digitalWrite(ledspielerzwei, HIGH);
  sieg = true;
}

void beidesieg(){
  digitalWrite(ledspielereins, HIGH);
  digitalWrite(ledspielerzwei, HIGH);
  sieg = true;
}

void loop() {    
 delay(10);
 schaltereins = digitalRead(spielereins);
 schalterzwei = digitalRead(spielerzwei);
 if(sieg == false){
    if (schaltereins == LOW ) {spielereinssieg();}
    if (schalterzwei == LOW ) {spielerzweisieg();}
    if (schaltereins == LOW && schalterzwei ==LOW) {beidesieg();}
  }
}
