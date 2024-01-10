// OOP is de succesvolle van programmeurs om de wereld zoals wij mensen
// die waarnemen om te zetten in broncode

// KLASSE             OBJECT
// blauwdruk          huis
// cakevorm           cakejes
// zandvormpje        zandvormpjes
// mal                uitgietsel

// kenmerken          waarde van kenmerken
// 1 hebben           oneindig veel

class Plant { // klasse
    int aantalbladeren; // fields, properties, attributen, objectvariabelen
    int hoogte;
    String soortnaam;

    Plant(String naam, int hoog){ // constructor
        soortnaam = naam;
        hoogte = hoog;

    }

    // methods 
    void groeien(int cm) {// void is return type
        hoogte = hoogte + cm;
        System.out.println("Ik, de "+soortnaam+" groei en ben nu " + hoogte);
    }
}

class PlantenWinkel {
    Plant kopen(int geld) {
        Plant gekochteplant = new Plant("Dahlia", 15);
        return gekochteplant;
    }

    Plant inruilen(Plant gekochteplant) {
        // gekochte
        Plant nieuweplant = new Plant("Bamboe",100);
        return nieuweplant;
    }
}

public class Demo {
    public static void main(String[] args) {
        System.out.println("DEMO doet het");

        Plant p = new Plant("Margriet",150);

        Plant q = new Plant("Tulp",20);

        System.out.println(p.soortnaam);
        System.out.println(q.soortnaam);

        p.groeien(5);
        q.groeien(30);

        // watere geven
        p.groeien(15);

        PlantenWinkel pw = new PlantenWinkel();

        Plant gekocht = pw.kopen(10);
        System.out.println("Ik heb een " + gekocht.soortnaam+" gekocht");

        Plant np = pw.inruilen(gekocht);
        System.out.println("Ik heb een " + gekocht.soortnaam+" ingeruild voor een "+ np.soortnaam);

    }
}