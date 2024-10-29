public class Doctor {
    private String name;
    private String specialty;

    public Doctor(String name, String specialty) {
        this.name = name;
        this.specialty = specialty;
    }

    public String getName() {
        return name;
    }

    public String getSpecialty() {
        return specialty;
    }

    public void seePatient(Patient patient) {
        System.out.println("Doctor " + name + " is seeing patient " + patient.getName() + ".");
    }
}
