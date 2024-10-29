import java.util.HashMap;
import java.util.Map;

public class RentalAgency {
    private Map<Car, Customer> rentedCars = new HashMap<>();

    public void rentCar(Car car, Customer customer) {
        if (!rentedCars.containsKey(car)) {
            rentedCars.put(car, customer);
            System.out.println(customer.getName() + " has rented a " + car.getMake() + " " + car.getModel() + ".");
        } else {
            System.out.println("Sorry, the car is already rented.");
        }
    }

    public void returnCar(Car car) {
        if (rentedCars.containsKey(car)) {
            Customer customer = rentedCars.remove(car);
            System.out.println(customer.getName() + " has returned the " + car.getMake() + " " + car.getModel() + ".");
        } else {
            System.out.println("This car was not rented from us.");
        }
    }

    public double calculateBill(Car car, int daysRented) {
        return car.getRentalPricePerDay() * daysRented;
    }
}
