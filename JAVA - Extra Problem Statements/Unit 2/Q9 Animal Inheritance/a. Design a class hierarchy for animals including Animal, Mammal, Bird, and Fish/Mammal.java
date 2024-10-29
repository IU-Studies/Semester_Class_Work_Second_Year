public class Mammal extends Animal {
    private boolean hasFur;

    public Mammal(String name, int age, boolean hasFur) {
        super(name, age);
        this.hasFur = hasFur;
    }

    public void giveBirth() {
        System.out.println(getName() + " is giving birth.");
    }

    public void displayInfo() {
        System.out.println("Mammal Name: " + getName() + ", Age: " + getAge() + ", Has Fur: " + hasFur);
    }
}
