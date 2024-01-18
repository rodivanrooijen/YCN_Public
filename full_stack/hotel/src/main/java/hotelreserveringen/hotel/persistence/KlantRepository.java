package hotelreserveringen.hotel.persistence;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Component;
import hotelreserveringen.hotel.model.klant;

@Component
public interface KlantRepository extends CrudRepository<klant, Long> {

}
