public class Customer {
    private String name;
    private String driverLicense;

    public Customer(String name, String driverLicense) {
        this.name = name;
        this.driverLicense = driverLicense;
    }

    public String getName() {
        return name;
    }

    public String getDriverLicense() {
        return driverLicense;
    }
}
