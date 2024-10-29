public class Main {
    public static void main(String[] args) {
        Mammal mammal = new Mammal("Lion", 5, true);
        Bird bird = new Bird("Eagle", 3, true);
        Fish fish = new Fish("Goldfish", 1, false);

        mammal.displayInfo();
        mammal.eat();
        mammal.giveBirth();
        mammal.sleep();
        System.out.println();

        bird.displayInfo();
        bird.eat();
        bird.layEggs();
        bird.sleep();
        System.out.println();

        fish.displayInfo();
        fish.eat();
        fish.swim();
        fish.sleep();
    }
}
