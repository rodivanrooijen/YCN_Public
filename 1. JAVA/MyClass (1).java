// 1 Naam                           Enscapsulation
// 2 Probleem  / Effect             Een field kan een ongewenste waarde hebben
// 3 OOP onderdelen ingezet         1 acces modifier 2 parameters 3 returntype
// 4 Programmeren
// 5 Use Cases                      Bank, leeftijd, nummerbord, postcode


public class MyClass {
    public static void main(String args[]) {
       Overboeking ov = new Overboeking();
        // ov.bedrag = -50;
        ov.setBedrag(-50);
        ov.overboeken();

      System.out.println("Demo werkt");
    }
}

class Overboeking{
    private int bedrag;
    void overboeken() {
        System.out.println("Bij mij gaat er "+bedrag+" af");
        System.out.println("Bij mij gaat er "+bedrag+" bij");
        
    }
    public void setBedrag(int amount) {
        if(amount < 0) {
            System.out.println("Dit is een illigale hoeveelheid");
        } 
        else{
        bedrag = amount;
        }
    }
}