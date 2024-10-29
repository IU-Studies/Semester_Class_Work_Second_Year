import java.time.LocalDateTime;

public class Main {
    public static void main(String[] args) {
        Doctor doctor = new Doctor("Alice Smith", "Cardiologist");
        Patient patient = new Patient("John Doe", 30, "No known allergies");

        LocalDateTime appointmentDateTime = LocalDateTime.of(2024, 11, 1, 10, 30);
        Appointment appointment = new Appointment(patient, doctor, appointmentDateTime);

        appointment.scheduleAppointment();

        appointment.conductAppointment();
    }
}
