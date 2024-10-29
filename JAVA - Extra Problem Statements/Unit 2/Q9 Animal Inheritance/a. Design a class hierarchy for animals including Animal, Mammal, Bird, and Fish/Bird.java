public class Bird extends Animal {
    private boolean canFly;

    public Bird(String name, int age, boolean canFly) {
        super(name, age);
        this.canFly = canFly;
    }

    public void layEggs() {
        System.out.println(getName() + " is laying eggs.");
    }

    public void displayInfo() {
        System.out.println("Bird Name: " + getName() + ", Age: " + getAge() + ", Can Fly: " + canFly);
    }
}
