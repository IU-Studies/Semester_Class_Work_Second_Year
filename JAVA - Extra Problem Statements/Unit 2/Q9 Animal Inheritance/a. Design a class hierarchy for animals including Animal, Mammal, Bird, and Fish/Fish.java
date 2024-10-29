public class Fish extends Animal {
    private boolean isSaltwater;

    public Fish(String name, int age, boolean isSaltwater) {
        super(name, age);
        this.isSaltwater = isSaltwater;
    }

    public void swim() {
        System.out.println(getName() + " is swimming.");
    }

    public void displayInfo() {
        System.out.println("Fish Name: " + getName() + ", Age: " + getAge() + ", Saltwater: " + isSaltwater);
    }
}
