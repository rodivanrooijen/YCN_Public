package hotelreserveringen.hotel.rest;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import hotelreserveringen.hotel.model.klant;
import hotelreserveringen.hotel.persistence.KlantService;


	@RestController
	public class KlantEndpoint {
		
		@Autowired
		private KlantService ks;
	
		@GetMapping("/test")
		public void testmethode() {
		System.out.println("TEST");
		ks.slaKlantOp();
		//ks.slaKlantop
		}
		
		@GetMapping("/alleklanten")
		public Iterable<klant>alleklanten(){
			System.out.println("/alleklanten");
			return ks.alleKlanten();
		}
		
		@GetMapping("/deleteklant/{id}")
		public void deleteklant(@PathVariable Long id) {
			System.out.println("/deleteklant/" + id);
			ks.deleteklant(id);
		}
		
		@PostMapping("/postklant")
		public klant postklant(@RequestBody klant k) {
			return ks.postklant(k);
		}
		
}
