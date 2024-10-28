// Write a Java program to create a class hierarchy for items in a library. 
// The base class should be LibraryItem, with subclasses Book, Magazine, and DVD. 
// Each subclass should have properties such as title, author, publicationYear, and genre. 
// Implement methods for checking out items, returning items, and calculating late fees.

class LibraryItem {
    private String title;
    private String author;
    private int publicationYear;
    private String genre;
    private boolean isCheckedOut;

    public LibraryItem(String title, String author, int publicationYear, String genre) {
        this.title = title;
        this.author = author;
        this.publicationYear = publicationYear;
        this.genre = genre;
        this.isCheckedOut = false;
    }

    public void checkOut() {
        if (!isCheckedOut) {
            isCheckedOut = true;
            System.out.println(title + " has been checked out.");
        } else {
            System.out.println(title + " is already checked out.");
        }
    }

    public void returnItem() {
        if (isCheckedOut) {
            isCheckedOut = false;
            System.out.println(title + " has been returned.");
        } else {
            System.out.println(title + " was not checked out.");
        }
    }

    public double calculateLateFee(int daysLate) {
        return daysLate * 0.50; 
    }

    public String getTitle() {
        return title;
    }
}

class Book extends LibraryItem {
    public Book(String title, String author, int publicationYear, String genre) {
        super(title, author, publicationYear, genre);
    }
}

class Magazine extends LibraryItem {
    public Magazine(String title, String author, int publicationYear, String genre) {
        super(title, author, publicationYear, genre);
    }
}

class DVD extends LibraryItem {
    public DVD(String title, String author, int publicationYear, String genre) {
        super(title, author, publicationYear, genre);
    }
}

public class LibrarySystem {
    public static void main(String[] args) {
        Book book = new Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Fiction");
        Magazine magazine = new Magazine("National Geographic", "National Geographic Society", 2023, "Science");
        DVD dvd = new DVD("Inception", "Christopher Nolan", 2010, "Science Fiction");

        book.checkOut();
        book.returnItem();
        System.out.println("Late fee for 3 days: $" + book.calculateLateFee(3));
        
        System.out.println();

        magazine.checkOut();
        magazine.returnItem();
        System.out.println("Late fee for 5 days: $" + magazine.calculateLateFee(5));

        System.out.println();

        dvd.checkOut();
        dvd.returnItem();
        System.out.println("Late fee for 2 days: $" + dvd.calculateLateFee(2));
    }
}
