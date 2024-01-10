// POLYMORFISME


class Dier{
    
    void maakGeluid(){
        System.out.println("Dit is geluid in dier");
    }
}

class Kat extends Dier{
    void maakGeluid(){
        System.out.println("Miauw");
    }
}

class Hond extends Dier{
    void maakGeluid(){
        System.out.println("Blaf");
    }
}

public class Demo {
    public static void main(String args[]) {
      System.out.println("Demo werkt");
      
      Kat k = new Kat();
      k.maakGeluid();
      
      Hond h = new Hond();
      h.maakGeluid();
    }
}