package hotelreserveringen.hotel.persistence;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import hotelreserveringen.hotel.model.klant;

@Service
public class KlantService {
	@Autowired
	private KlantRepository kr;
	
	public void slaKlantOp() {
		kr.save(new klant());
	}
	
	public klant postklant(klant k) {
		System.out.println("postklant()");
		System.out.println(k.getVoornaam()+", " + k.getAchternaam());
		kr.save(k);
		return k;
	}
	public Iterable<klant> alleKlanten(){
		System.out.println("alleKlanten()");
		return kr.findAll();
	}
	public void deleteklant(long id) {
		kr.deleteById(id);
	}
}
