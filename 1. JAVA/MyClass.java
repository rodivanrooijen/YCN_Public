//RELATIES

// HAS-A
// IS-A

class Persoon{
    String naam;
    Telefoon tel;
}

class Telefoon{
    
}

class Voertuig{
    int gewicht;
    int snelheid;
}

class Auto extends Voertuig { // IS-A relatie
    // stuur
    int aantalzitplaatsen;
    
}

public class MyClass {
    public static void main(String[] args) {
      System.out.println("Demo doet het");
      
      Persoon ivo = new Persoon();
      ivo.tel = new Telefoon(); // has-a relatie
      
      Auto a = new Auto();
      a.snelheid = 100;
      
      Auto a2 = new Auto();
      a2.aantalzitplaatsen = 5;
      
      // REFERENTIETYPE // OBJECT TYPE
      Voertuig v = new Auto();
      // v.aantalzitplaatsen = 3; // Kan niet
      
      
      
    }
}