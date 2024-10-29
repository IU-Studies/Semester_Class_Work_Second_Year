public class Main {
    public static void main(String[] args) {
        Car car1 = new Car("Toyota", "Camry", 40.0);
        Car car2 = new Car("Honda", "Civic", 35.0);

        Customer customer1 = new Customer("Alice", "D123456789");
        Customer customer2 = new Customer("Bob", "D987654321");

        RentalAgency rentalAgency = new RentalAgency();

        rentalAgency.rentCar(car1, customer1);
        rentalAgency.rentCar(car2, customer2);

        int daysRented = 3;
        double bill1 = rentalAgency.calculateBill(car1, daysRented);
        double bill2 = rentalAgency.calculateBill(car2, daysRented);
        
        System.out.println("Bill for " + customer1.getName() + ": $" + bill1);
        System.out.println("Bill for " + customer2.getName() + ": $" + bill2);

        rentalAgency.returnCar(car1);
        rentalAgency.returnCar(car2);
    }
}
