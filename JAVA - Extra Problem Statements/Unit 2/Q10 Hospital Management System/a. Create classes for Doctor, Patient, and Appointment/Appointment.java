import java.time.LocalDateTime;

public class Appointment {
    private Patient patient;
    private Doctor doctor;
    private LocalDateTime dateTime;

    public Appointment(Patient patient, Doctor doctor, LocalDateTime dateTime) {
        this.patient = patient;
        this.doctor = doctor;
        this.dateTime = dateTime;
    }

    public void scheduleAppointment() {
        System.out.println("Appointment scheduled for patient " + patient.getName() + 
                           " with Doctor " + doctor.getName() + " on " + dateTime);
    }

    public void conductAppointment() {
        doctor.seePatient(patient);
        System.out.println("Appointment conducted successfully.");
    }
}
